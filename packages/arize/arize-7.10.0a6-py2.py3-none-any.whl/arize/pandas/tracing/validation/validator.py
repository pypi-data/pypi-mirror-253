from datetime import datetime, timedelta
from itertools import chain
from typing import Any, Iterable, List, Optional, Union

import arize.pandas.tracing.columns as tracin_cols
import arize.pandas.tracing.constants as tracing_constants
import pandas as pd
import pyarrow as pa
from arize.pandas.tracing.types import StatusCodes
from arize.pandas.tracing.validation import errors as tracing_err
from arize.pandas.validation import errors as err
from arize.utils.constants import (
    MAX_EMBEDDING_DIMENSIONALITY,
    MAX_FUTURE_YEARS_FROM_CURRENT_TIME,
    MAX_PAST_YEARS_FROM_CURRENT_TIME,
)
from arize.utils.logging import logger
from arize.utils.types import is_array_of, is_dict_of, is_json_str, is_list_of
from arize.utils.utils import log_a_list
from pandas.api.types import is_bool_dtype, is_numeric_dtype


# TODO(Kiko): Must validate
# times in ns
# status code values either strings or ints
def validate_argument_types(
    dataframe: pd.DataFrame,
    model_id: str,
    dt_fmt: str,
    model_version: Optional[str] = None,
) -> List[err.ValidationError]:
    return list(
        chain(
            _check_field_convertible_to_str(model_id, model_version),
            _check_dataframe_type(dataframe),
            _check_datetime_format_type(dt_fmt),
        )
    )


def validate_dataframe_form(
    dataframe: pd.DataFrame,
) -> List[err.ValidationError]:
    _info_dataframe_extra_column_names(dataframe)
    return list(
        chain(
            _check_dataframe_index(dataframe),
            _check_dataframe_minimum_column_set(dataframe),
            _check_dataframe_for_duplicate_columns(dataframe),
            _check_dataframe_column_content_type(dataframe),
        )
    )


def validate_values(
    dataframe: pd.DataFrame,
    model_id: str,
    model_version: Optional[str] = None,
) -> List[err.ValidationError]:
    return list(
        chain(
            _check_invalid_model_id(model_id),
            _check_invalid_model_version(model_version),
            _check_span_root_field_values(dataframe),
            _check_span_attributes_values(dataframe),
        )
    )


# -------------------
# Direct Input Checks
# -------------------


def _check_field_convertible_to_str(
    model_id: str,
    model_version: str,
) -> List[err.InvalidFieldTypeConversion]:
    # converting to a set first makes the checks run a lot faster
    wrong_fields = []
    if model_id is not None and not isinstance(model_id, str):
        try:
            str(model_id)
        except Exception:
            wrong_fields.append("model_id")
    if model_version is not None and not isinstance(model_version, str):
        try:
            str(model_version)
        except Exception:
            wrong_fields.append("model_version")

    if wrong_fields:
        return [err.InvalidFieldTypeConversion(wrong_fields, "string")]
    return []


def _check_dataframe_type(
    dataframe: Any,
) -> List[tracing_err.InvalidTypeArgument]:
    if not isinstance(dataframe, pd.DataFrame):
        return [
            tracing_err.InvalidTypeArgument(
                wrong_arg=dataframe,
                arg_name="dataframe",
                arg_type="pandas DataFrame",
            )
        ]
    return []


def _check_datetime_format_type(
    dt_fmt: Any,
) -> List[tracing_err.InvalidTypeArgument]:
    if not isinstance(dt_fmt, str):
        return [
            tracing_err.InvalidTypeArgument(
                wrong_arg=dt_fmt,
                arg_name="dateTime format",
                arg_type="string",
            )
        ]
    return []


def _check_invalid_model_id(model_id: Optional[str]) -> List[err.InvalidModelId]:
    # assume it's been coerced to string beforehand
    if (not isinstance(model_id, str)) or len(model_id.strip()) == 0:
        return [err.InvalidModelId()]
    return []


def _check_invalid_model_version(
    model_version: Optional[str] = None,
) -> List[err.InvalidModelVersion]:
    if model_version is None:
        return []
    if not isinstance(model_version, str) or len(model_version.strip()) == 0:
        return [err.InvalidModelVersion()]

    return []


# ---------------------
# DataFrame Form Checks
# ---------------------


def _check_dataframe_index(dataframe: pd.DataFrame) -> List[err.InvalidDataFrameIndex]:
    if (dataframe.index != dataframe.reset_index(drop=True).index).any():
        return [err.InvalidDataFrameIndex()]
    return []


def _info_dataframe_extra_column_names(
    df: pd.DataFrame,
) -> None:
    extra_cols = [
        col for col in df.columns if col not in tracin_cols.SPAN_OPENINFERENCE_COLUMN_NAMES
    ]
    if extra_cols:
        logger.info(
            "The following columns are not part of the Open Inference Specification "
            f"and will be ignored: {log_a_list(list_of_str=extra_cols, join_word='and')}"
        )
    return None


def _check_dataframe_minimum_column_set(
    df: pd.DataFrame,
) -> List[tracing_err.InvalidDataFrameMissingColumns]:
    existing_columns = set(df.columns)
    missing_cols = []
    for col in tracin_cols.SPAN_OPENINFERENCE_REQUIRED_COLS:
        if col not in existing_columns:
            missing_cols.append(col)

    if missing_cols:
        return [tracing_err.InvalidDataFrameMissingColumns(missing_cols=missing_cols)]
    return []


def _check_dataframe_for_duplicate_columns(
    df: pd.DataFrame,
) -> List[tracing_err.InvalidDataFrameDuplicateColumns]:
    # Get the duplicated column names from the dataframe
    duplicate_columns = df.columns[df.columns.duplicated()]
    if not duplicate_columns.empty:
        return [tracing_err.InvalidDataFrameDuplicateColumns(duplicate_columns)]
    return []


# TODO(Kiko): Performance improvements
# We should try using:
# - Pandas any() and all() functions together with apply(), or
# - A combination of the following type checker functions from Pandas, i.e,
#   is_float_dtype. See link below
# https://github.com/pandas-dev/pandas/blob/f538741432edf55c6b9fb5d0d496d2dd1d7c2457/pandas/core/dtypes/common.py
def _check_dataframe_column_content_type(
    df: pd.DataFrame,
) -> List[tracing_err.InvalidDataFrameColumnContentTypes]:
    # We let this values be in the dataframe and don't use them to verify type
    # They will be serialized by arrow and understood as missing values
    wrong_lists_of_dicts_cols = []
    wrong_dicts_cols = []
    wrong_numeric_cols = []
    wrong_bools_cols = []
    wrong_timestamp_cols = []
    wrong_JSON_cols = []
    wrong_string_cols = []
    # TODO(Kiko): Must also skip the NaN values, not just None
    for col in tracin_cols.SPAN_OPENINFERENCE_COLUMN_NAMES:
        if col not in df.columns:
            continue
        if col in tracin_cols.SPAN_OPENINFERENCE_LIST_OF_DICT_COLS:
            for row in df[col]:
                if (
                    not isinstance(row, Iterable)
                    and row in tracing_constants.ASSUMED_MISSING_VALUES
                ):
                    continue
                if not (is_list_of(row, dict) or is_array_of(row, dict)) or not all(
                    is_dict_of(val, key_allowed_types=str) for val in row
                ):
                    wrong_lists_of_dicts_cols.append(col)
                    break
        elif col in tracin_cols.SPAN_OPENINFERENCE_DICT_COLS:
            if not all(
                True
                if row in tracing_constants.ASSUMED_MISSING_VALUES
                else is_dict_of(row, key_allowed_types=str)
                for row in df[col]
            ):
                wrong_dicts_cols.append(col)
        elif col in tracin_cols.SPAN_OPENINFERENCE_NUM_COLS:
            if not is_numeric_dtype(df[col]):
                wrong_numeric_cols.append(col)
        elif col in tracin_cols.SPAN_OPENINFERENCE_BOOL_COLS:
            if not is_bool_dtype(df[col]):
                wrong_bools_cols.append(col)
        elif col in tracin_cols.SPAN_OPENINFERENCE_TIME_COLS:
            # Accept strings and datetime objects
            if not all(
                True
                if row in tracing_constants.ASSUMED_MISSING_VALUES
                else isinstance(row, (str, datetime, pd.Timestamp))
                for row in df[col]
            ):
                wrong_timestamp_cols.append(col)
        elif col in tracin_cols.SPAN_OPENINFERENCE_JSON_STR_COLS:
            # We check the correctness of the JSON strings when we check the values
            # of the data in the dataframe
            if not all(
                True if row in tracing_constants.ASSUMED_MISSING_VALUES else isinstance(row, str)
                for row in df[col]
            ):
                wrong_JSON_cols.append(col)
        else:
            # if not all(isinstance(row, str) if row not in skip_values else True for row in df[col]):
            if not all(
                True if row in tracing_constants.ASSUMED_MISSING_VALUES else isinstance(row, str)
                for row in df[col]
            ):
                wrong_string_cols.append(col)

    errors = []
    if wrong_lists_of_dicts_cols:
        errors.append(
            tracing_err.InvalidDataFrameColumnContentTypes(
                invalid_type_cols=wrong_lists_of_dicts_cols,
                expected_type="lists of dictionaries with string keys",
            ),
        )
    if wrong_dicts_cols:
        errors.append(
            tracing_err.InvalidDataFrameColumnContentTypes(
                invalid_type_cols=wrong_dicts_cols,
                expected_type="dictionaries with string keys",
            ),
        )
    if wrong_numeric_cols:
        errors.append(
            tracing_err.InvalidDataFrameColumnContentTypes(
                invalid_type_cols=wrong_numeric_cols,
                expected_type="ints or floats",
            ),
        )
    if wrong_bools_cols:
        errors.append(
            tracing_err.InvalidDataFrameColumnContentTypes(
                invalid_type_cols=wrong_bools_cols,
                expected_type="bools",
            ),
        )
    if wrong_timestamp_cols:
        errors.append(
            tracing_err.InvalidDataFrameColumnContentTypes(
                invalid_type_cols=wrong_timestamp_cols,
                expected_type="datetime objects or formatted strings",
            ),
        )
    if wrong_JSON_cols:
        errors.append(
            tracing_err.InvalidDataFrameColumnContentTypes(
                invalid_type_cols=wrong_JSON_cols,
                expected_type="JSON strings",
            ),
        )
    if wrong_string_cols:
        errors.append(
            tracing_err.InvalidDataFrameColumnContentTypes(
                invalid_type_cols=wrong_string_cols,
                expected_type="strings",
            ),
        )
    return errors


# -----------------------
# DataFrame Values Checks
# -----------------------


def _check_span_root_field_values(
    dataframe: pd.DataFrame,
) -> List[err.ValidationError]:
    return list(
        chain(
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_SPAN_ID_COL_NAME,
                min_len=tracing_constants.SPAN_ID_MIN_STR_LENGTH,
                max_len=tracing_constants.SPAN_ID_MAX_STR_LENGTH,
                allow_nulls=False,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_TRACE_ID_COL_NAME,
                min_len=tracing_constants.SPAN_ID_MIN_STR_LENGTH,
                max_len=tracing_constants.SPAN_ID_MAX_STR_LENGTH,
                allow_nulls=False,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_PARENT_SPAN_ID_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_ID_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_NAME_COL_NAME,
                min_len=tracing_constants.SPAN_NAME_MIN_STR_LENGTH,
                max_len=tracing_constants.SPAN_NAME_MAX_STR_LENGTH,
                allow_nulls=False,
            ),
            _check_string_column_allowed_values(
                df=dataframe,
                col_name=tracin_cols.SPAN_STATUS_CODE_COL_NAME,
                allowed_values=StatusCodes.list_codes(),
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_STATUS_MESSAGE_COL_NAME,
                min_len=tracing_constants.SPAN_STATUS_MSG_MIN_STR_LENGTH,
                max_len=tracing_constants.SPAN_STATUS_MSG_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_value_columns_start_end_time(
                df=dataframe,
            ),
            _check_event_column_value(df=dataframe),
        )
    )


def _check_span_attributes_values(
    dataframe: pd.DataFrame,
) -> List[err.ValidationError]:
    # group of fields that must be valid json with character limit
    # json_str_limit_checks = [
    #     _check_string_column_value_length(
    #         df=dataframe,
    #         col_name=col_name,
    #         min_len=0,
    #         max_len=max_limit,
    #         allow_nulls=True,
    #         must_be_json=True,
    #     )
    #     for col_name, max_limit in [
    #         (
    #             tracin_cols.SPAN_ATTRIBUTES_LLM_INVOCATION_PARAMETERS_COL_NAME,
    #             tracing_constants.JSON_STRING_MAX_STR_LENGTH,
    #         ),
    #         (
    #             tracin_cols.SPAN_ATTRIBUTES_LLM_PROMPT_TEMPLATE_VARIABLES_COL_NAME,
    #             tracing_constants.SPAN_LLM_PROMPT_TEMPLATE_VARIABLES_MAX_STR_LENGTH,
    #         ),
    #         (
    #             tracin_cols.SPAN_ATTRIBUTES_TOOL_PARAMETERS_COL_NAME,
    #             tracing_constants.SPAN_TOOL_PARAMETERS_MAX_STR_LENGTH,
    #         ),
    #     ]
    # ]
    return list(
        chain(
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_KIND_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_ID_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_EXCEPTION_MESSAGE_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_EXCEPTION_MESSAGE_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_EXCEPTION_STACKTRACE_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_EXCEPTION_STACK_TRACE_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_INPUT_VALUE_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_IO_VALUE_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_OUTPUT_VALUE_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_IO_VALUE_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_INPUT_MIME_TYPE_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_IO_MIME_TYPE_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_OUTPUT_MIME_TYPE_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_IO_MIME_TYPE_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_EMBEDDING_MODEL_NAME_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_EMBEDDING_NAME_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_LLM_MODEL_NAME_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_LLM_MODEL_NAME_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_LLM_PROMPT_TEMPLATE_TEMPLATE_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_LLM_PROMPT_TEMPLATE_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_LLM_PROMPT_TEMPLATE_VERSION_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_LLM_PROMPT_TEMPLATE_VERSION_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_TOOL_NAME_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_TOOL_NAME_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_TOOL_DESCRIPTION_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_TOOL_DESCRIPTION_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_RERANKER_QUERY_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_RERANKER_QUERY_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_RERANKER_MODEL_NAME_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_RERANKER_MODEL_NAME_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_LLM_INVOCATION_PARAMETERS_COL_NAME,
                min_len=0,
                max_len=tracing_constants.JSON_STRING_MAX_STR_LENGTH,
                allow_nulls=True,
                must_be_json=True,
            ),
            _check_string_column_value_length(
                df=dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_TOOL_PARAMETERS_COL_NAME,
                min_len=0,
                max_len=tracing_constants.SPAN_TOOL_PARAMETERS_MAX_STR_LENGTH,
                allow_nulls=True,
                must_be_json=True,
            ),
            _check_embeddings_column_value(dataframe),
            _check_LLM_IO_messages_column_value(
                dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_LLM_INPUT_MESSAGES_COL_NAME,
            ),
            _check_LLM_IO_messages_column_value(
                dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_LLM_OUTPUT_MESSAGES_COL_NAME,
            ),
            _check_documents_column_value(
                dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_RETRIEVAL_DOCUMENTS_COL_NAME,
            ),
            _check_documents_column_value(
                dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_RERANKER_INPUT_DOCUMENTS_COL_NAME,
            ),
            _check_documents_column_value(
                dataframe,
                col_name=tracin_cols.SPAN_ATTRIBUTES_RERANKER_OUTPUT_DOCUMENTS_COL_NAME,
            ),
        )
    )


def _check_string_column_value_length(
    df: pd.DataFrame,
    col_name: str,
    min_len: int,
    max_len: int,
    allow_nulls: bool,
    must_be_json: bool = False,
) -> List[Union[tracing_err.InvalidMissingValueInColumn, tracing_err.InvalidStringLengthInColumn]]:
    if col_name not in df.columns:
        return []

    errors = []
    if not allow_nulls and df[col_name].isnull().any():
        errors.append(
            tracing_err.InvalidMissingValueInColumn(
                col_name=col_name,
            )
        )

    if not (
        # Check that the non-None values of the desired colum have a
        # string length between min_len and max_len
        # Does not check the None values
        df[~df[col_name].isnull()][col_name]
        .astype(str)
        .str.len()
        .between(min_len, max_len)
        .all()
    ):
        errors.append(
            tracing_err.InvalidStringLengthInColumn(
                col_name=col_name,
                min_length=min_len,
                max_length=max_len,
            )
        )
    if must_be_json and not df[~df[col_name].isnull()][col_name].apply(is_json_str).all():
        errors.append(tracing_err.InvalidJsonStringInColumn(col_name=col_name))

    return errors


def _check_string_column_allowed_values(
    df: pd.DataFrame,
    col_name: str,
    allowed_values: List[str],
    allow_nulls: bool,
) -> List[
    Union[tracing_err.InvalidMissingValueInColumn, tracing_err.InvalidStringValueNotAllowedInColumn]
]:
    if col_name not in df.columns:
        return []

    errors = []
    if not allow_nulls and df[col_name].isnull().any():
        errors.append(
            tracing_err.InvalidMissingValueInColumn(
                col_name=col_name,
            )
        )

    # We compare in lowercase
    allowed_values_lowercase = [v.lower() for v in allowed_values]
    if not (
        # Check that the non-None values of the desired colum have a
        # string length between min_len and max_len
        # Does not check the None values
        df[~df[col_name].isnull()][col_name]
        .astype(str)
        .str.lower()
        .isin(allowed_values_lowercase)
        .all()
    ):
        errors.append(
            tracing_err.InvalidStringValueNotAllowedInColumn(
                col_name=col_name,
                allowed_values=allowed_values,
            )
        )
    return errors


def _check_value_columns_start_end_time(
    df: pd.DataFrame,
) -> List[
    Union[
        tracing_err.InvalidMissingValueInColumn,
        tracing_err.InvalidTimestampValueInColumn,
        tracing_err.InvalidStartAndEndTimeValuesInColumn,
    ]
]:
    errors = []
    errors += _check_value_timestamp(
        df=df,
        col_name=tracin_cols.SPAN_START_TIME_COL_NAME,
        allow_nulls=False,
    )
    errors += _check_value_timestamp(
        df=df,
        col_name=tracin_cols.SPAN_END_TIME_COL_NAME,
        allow_nulls=True,
    )
    if (
        tracin_cols.SPAN_START_TIME_COL_NAME in df.columns
        and tracin_cols.SPAN_END_TIME_COL_NAME in df.columns
        and (
            df[tracin_cols.SPAN_START_TIME_COL_NAME] > df[tracin_cols.SPAN_END_TIME_COL_NAME]
        ).any()
    ):
        errors.append(
            tracing_err.InvalidStartAndEndTimeValuesInColumn(
                greater_col_name=tracin_cols.SPAN_END_TIME_COL_NAME,
                less_col_name=tracin_cols.SPAN_START_TIME_COL_NAME,
            )
        )
    return errors


def _check_value_timestamp(
    df: pd.DataFrame,
    col_name: str,
    allow_nulls: bool,
) -> List[
    Union[tracing_err.InvalidMissingValueInColumn, tracing_err.InvalidTimestampValueInColumn]
]:
    # This check expects that timestamps have previously been converted to nanoseconds
    if col_name not in df.columns:
        return []

    errors = []
    if not allow_nulls and df[col_name].isnull().any():
        errors.append(
            tracing_err.InvalidMissingValueInColumn(
                col_name=col_name,
            )
        )

    now_t = datetime.now()
    lbound, ubound = (
        (now_t - timedelta(days=MAX_PAST_YEARS_FROM_CURRENT_TIME * 365)).timestamp() * 1e9,
        (now_t + timedelta(days=MAX_FUTURE_YEARS_FROM_CURRENT_TIME * 365)).timestamp() * 1e9,
    )

    # faster than pyarrow compute
    stats = df[col_name].agg(["min", "max"])

    ta = pa.Table.from_pandas(stats.to_frame())
    min_, max_ = ta.column(0)
    if max_.as_py() > now_t.timestamp() * 1e9:
        logger.warning(
            f"Detected future timestamp in column '{col_name}'. "
            "Caution when sending spans with future timestamps. "
            "Arize only stores 2 years worth of data. For example, if you sent spans "
            "to Arize from 1.5 years ago, and now send spans with timestamps of a year in "
            "the future, the oldest 0.5 years will be dropped to maintain the 2 years worth of data "
            "requirement."
        )

    if min_.as_py() < lbound or max_.as_py() > ubound:
        return [tracing_err.InvalidTimestampValueInColumn(timestamp_col_name=col_name)]

    return []


def _check_event_column_value(
    df: pd.DataFrame,
) -> List[tracing_err.InvalidEventValueInColumn]:
    col_name = tracin_cols.SPAN_EVENTS_COL_NAME
    if col_name not in df.columns:
        return []

    wrong_name_found, wrong_time_found, wrong_attrs_found = False, False, False
    for row in df[col_name]:
        for event in row:
            # validate name
            name = event.get(tracin_cols.SPAN_EVENT_NAME_KEY)
            if (
                name
                and not wrong_name_found
                and len(name) > tracing_constants.SPAN_EVENT_NAME_MAX_STR_LENGTH
            ):
                wrong_name_found = True
            # validate time
            time = event.get(tracin_cols.SPAN_EVENT_TIME_KEY)
            if time and not wrong_time_found and time < 0:
                wrong_time_found = True
            # validate attributes
            attrs = event.get(tracin_cols.SPAN_EVENT_ATTRIBUTES_KEY)
            if (
                attrs
                and not wrong_attrs_found
                and (
                    len(attrs) > tracing_constants.SPAN_EVENT_ATTRS_MAX_STR_LENGTH
                    or not is_json_str(attrs)
                )
            ):
                wrong_attrs_found = True
        if wrong_name_found and wrong_time_found and wrong_attrs_found:
            break

    if wrong_name_found or wrong_time_found or wrong_attrs_found:
        return [
            tracing_err.InvalidEventValueInColumn(
                col_name=col_name,
                wrong_name=wrong_name_found,
                wrong_time=wrong_time_found,
                wrong_attrs=wrong_attrs_found,
            )
        ]
    return []


def _check_embeddings_column_value(
    df: pd.DataFrame,
) -> List[tracing_err.InvalidEmbeddingValueInColumn]:
    col_name = tracin_cols.SPAN_ATTRIBUTES_EMBEDDING_EMBEDDINGS_COL_NAME
    if col_name not in df.columns:
        return []

    wrong_vector_found, wrong_text_found = False, False
    for row in df[~df[col_name].isnull()][col_name]:
        for emb_object in row:
            # validate vector
            vector = emb_object.get(tracin_cols.SPAN_ATTRIBUTES_EMBEDDING_VECTOR_KEY)
            if (
                vector is not None
                and not wrong_vector_found
                and (len(vector) > MAX_EMBEDDING_DIMENSIONALITY or len(vector) == 1)
            ):
                wrong_vector_found = True
            # validate text
            text = emb_object.get(tracin_cols.SPAN_ATTRIBUTES_EMBEDDING_TEXT_KEY)
            if text and len(text) > tracing_constants.SPAN_EMBEDDING_TEXT_MAX_STR_LENGTH:
                wrong_text_found = True
        if wrong_vector_found and wrong_text_found:
            break

    if wrong_vector_found or wrong_text_found:
        return [
            tracing_err.InvalidEmbeddingValueInColumn(
                col_name=col_name,
                wrong_vector=wrong_vector_found,
                wrong_text=wrong_text_found,
            )
        ]
    return []


def _check_LLM_IO_messages_column_value(
    df: pd.DataFrame,
    col_name: str,
) -> List[tracing_err.InvalidLLMMessageValueInColumn]:
    if col_name not in df.columns:
        return []

    wrong_role_found, wrong_content_found, wrong_tool_calls_found = False, False, False
    for row in df[~df[col_name].isnull()][col_name]:
        for message in row:
            # validate role
            role = message.get(tracin_cols.SPAN_ATTRIBUTES_MESSAGE_ROLE_KEY)
            if (
                role
                and not wrong_role_found
                and len(role) > tracing_constants.SPAN_LLM_MESSAGE_ROLE_MAX_STR_LENGTH
            ):
                wrong_role_found = True
            # validate content
            content = message.get(tracin_cols.SPAN_ATTRIBUTES_MESSAGE_CONTENT_KEY)
            if (
                content
                and not wrong_content_found
                and len(content) > tracing_constants.SPAN_LLM_MESSAGE_CONTENT_MAX_STR_LENGTH
            ):
                wrong_content_found = True
            # validate tool calls
            tool_calls = message.get(tracin_cols.SPAN_ATTRIBUTES_MESSAGE_TOOL_CALLS_KEY)
            if tool_calls and not wrong_tool_calls_found:
                for tc in tool_calls:
                    function_name = tc.get(
                        tracin_cols.SPAN_ATTRIBUTES_MESSAGE_TOOL_CALLS_FUNCTION_NAME_KEY
                    )
                    if (
                        function_name
                        and len(function_name)
                        > tracing_constants.SPAN_LLM_TOOL_CALL_FUNCTION_NAME_MAX_STR_LENGTH
                    ):
                        wrong_tool_calls_found = True
                        break
                    function_args = tc.get(
                        tracin_cols.SPAN_ATTRIBUTES_MESSAGE_TOOL_CALLS_FUNCTION_ARGUMENTS_KEY
                    )
                    if function_args and (
                        len(function_args) > tracing_constants.JSON_STRING_MAX_STR_LENGTH
                        or not is_json_str(function_args)
                    ):
                        wrong_tool_calls_found = True
                        break
        if wrong_role_found and wrong_content_found and wrong_tool_calls_found:
            break

    if wrong_role_found or wrong_content_found or wrong_tool_calls_found:
        return [
            tracing_err.InvalidLLMMessageValueInColumn(
                col_name=col_name,
                wrong_role=wrong_role_found,
                wrong_content=wrong_content_found,
                wrong_tool_calls=wrong_tool_calls_found,
            )
        ]
    return []


def _check_documents_column_value(
    df: pd.DataFrame,
    col_name: str,
) -> List[tracing_err.InvalidDocumentValueInColumn]:
    if col_name not in df.columns:
        return []

    wrong_id_found, wrong_content_found, wrong_metadata_found = False, False, False
    for row in df[~df[col_name].isnull()][col_name]:
        for doc in row:
            # validate id
            id = doc.get(tracin_cols.SPAN_ATTRIBUTES_DOCUMENT_ID_KEY)
            if (
                id
                and not wrong_id_found
                and len(id) > tracing_constants.SPAN_DOCUMENT_ID_MAX_STR_LENGTH
            ):
                wrong_id_found = True
            # validate content
            content = doc.get(tracin_cols.SPAN_ATTRIBUTES_DOCUMENT_CONTENT_KEY)
            if (
                content
                and not wrong_content_found
                and len(content) > tracing_constants.SPAN_DOCUMENT_CONTENT_MAX_STR_LENGTH
            ):
                wrong_content_found = True
            # validate metadata
            metadata = doc.get(tracin_cols.SPAN_ATTRIBUTES_DOCUMENT_METADATA_KEY)
            if (
                metadata
                and not wrong_metadata_found
                and (
                    len(metadata) > tracing_constants.JSON_STRING_MAX_STR_LENGTH
                    or not is_json_str(metadata)
                )
            ):
                wrong_metadata_found = True
        if wrong_id_found and wrong_content_found and wrong_metadata_found:
            break

    if wrong_id_found or wrong_content_found or wrong_metadata_found:
        return [
            tracing_err.InvalidDocumentValueInColumn(
                col_name=col_name,
                wrong_id=wrong_id_found,
                wrong_content=wrong_content_found,
                wrong_metadata=wrong_metadata_found,
            )
        ]
    return []


# -----------------------
# Arrow Types Checks
# -----------------------
