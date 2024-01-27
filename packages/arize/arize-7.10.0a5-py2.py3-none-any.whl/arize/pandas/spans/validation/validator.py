from datetime import datetime, timedelta
from itertools import chain
from typing import Any, Iterable, List, Optional, Union

import pandas as pd
import pyarrow as pa
from arize.pandas.spans.columns import (
    SPAN_END_TIME_COL_NAME,
    SPAN_NAME_COL_NAME,
    SPAN_OPENINFERENCE_BOOL_COLS,
    SPAN_OPENINFERENCE_COLUMN_NAMES,
    SPAN_OPENINFERENCE_DICT_COLS,
    SPAN_OPENINFERENCE_JSON_STR_COLS,
    SPAN_OPENINFERENCE_LIST_OF_DICT_COLS,
    SPAN_OPENINFERENCE_NUM_COLS,
    SPAN_OPENINFERENCE_REQUIRED_COLS,
    SPAN_OPENINFERENCE_TIME_COLS,
    SPAN_PARENT_SPAN_ID_COL_NAME,
    SPAN_SPAN_ID_COL_NAME,
    SPAN_START_TIME_COL_NAME,
    SPAN_STATUS_CODE_COL_NAME,
    SPAN_STATUS_MESSAGE_COL_NAME,
    SPAN_TRACE_ID_COL_NAME,
)
from arize.pandas.spans.constants import (
    ASSUMED_MISSING_VALUES,
    SPAN_ID_MAX_STR_LENGTH,
    SPAN_ID_MIN_STR_LENGTH,
    SPAN_NAME_MAX_STR_LENGTH,
    SPAN_NAME_MIN_STR_LENGTH,
    SPAN_STATUS_MSG_MAX_STR_LENGTH,
    SPAN_STATUS_MSG_MIN_STR_LENGTH,
)
from arize.pandas.spans.types import StatusCodes
from arize.pandas.spans.validation import errors as span_err
from arize.pandas.validation import errors as err
from arize.utils.constants import (
    MAX_FUTURE_YEARS_FROM_CURRENT_TIME,
    MAX_PAST_YEARS_FROM_CURRENT_TIME,
)
from arize.utils.logging import logger
from arize.utils.types import is_array_of, is_dict_of, is_list_of
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
    _warning_dataframe_extra_column_names(dataframe)
    return list(
        chain(
            _check_dataframe_index(dataframe),
            _check_dataframe_minimum_column_set(dataframe),
            _check_dataframe_for_duplicate_columns(dataframe),
            _check_dataframe_column_content_type(dataframe),
        )
    )


def validate_dataframe_values(
    dataframe: pd.DataFrame,
) -> List[err.ValidationError]:
    return list(
        chain(
            _check_string_value_length(
                df=dataframe,
                col_name=SPAN_SPAN_ID_COL_NAME,
                min_len=SPAN_ID_MIN_STR_LENGTH,
                max_len=SPAN_ID_MAX_STR_LENGTH,
                allow_nulls=False,
            ),
            _check_string_value_length(
                df=dataframe,
                col_name=SPAN_TRACE_ID_COL_NAME,
                min_len=SPAN_ID_MIN_STR_LENGTH,
                max_len=SPAN_ID_MAX_STR_LENGTH,
                allow_nulls=False,
            ),
            _check_string_value_length(
                df=dataframe,
                col_name=SPAN_PARENT_SPAN_ID_COL_NAME,
                min_len=0,
                max_len=SPAN_ID_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_string_value_length(
                df=dataframe,
                col_name=SPAN_NAME_COL_NAME,
                min_len=SPAN_NAME_MIN_STR_LENGTH,
                max_len=SPAN_NAME_MAX_STR_LENGTH,
                allow_nulls=False,
            ),
            _check_string_allowed_values(
                df=dataframe,
                col_name=SPAN_STATUS_CODE_COL_NAME,
                allowed_values=StatusCodes.list_codes(),
                allow_nulls=True,
            ),
            _check_string_value_length(
                df=dataframe,
                col_name=SPAN_STATUS_MESSAGE_COL_NAME,
                min_len=SPAN_STATUS_MSG_MIN_STR_LENGTH,
                max_len=SPAN_STATUS_MSG_MAX_STR_LENGTH,
                allow_nulls=True,
            ),
            _check_value_start_end_time(
                df=dataframe,
            ),
        )
    )


def validate_arrow_types(
    pyarrow_schema: pa.Schema,
) -> List[err.ValidationError]:
    logger.warning("validate_arrow_types is not implemented")
    return list(chain())


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
) -> List[span_err.InvalidTypeArgument]:
    if not isinstance(dataframe, pd.DataFrame):
        return [
            span_err.InvalidTypeArgument(
                wrong_arg=dataframe,
                arg_name="dataframe",
                arg_type="pandas DataFrame",
            )
        ]
    return []


def _check_datetime_format_type(
    dt_fmt: Any,
) -> List[span_err.InvalidTypeArgument]:
    if not isinstance(dt_fmt, str):
        return [
            span_err.InvalidTypeArgument(
                wrong_arg=dt_fmt,
                arg_name="dateTime format",
                arg_type="string",
            )
        ]
    return []


# ---------------------
# DataFrame Form Checks
# ---------------------


def _check_dataframe_index(dataframe: pd.DataFrame) -> List[err.InvalidDataFrameIndex]:
    if (dataframe.index != dataframe.reset_index(drop=True).index).any():
        return [err.InvalidDataFrameIndex()]
    return []


def _warning_dataframe_extra_column_names(
    df: pd.DataFrame,
) -> None:
    extra_cols = [col for col in df.columns if col not in SPAN_OPENINFERENCE_COLUMN_NAMES]
    if extra_cols:
        logger.warning(
            "The following columns are not part of the Open Inference Specification "
            f"and will be ignored: {log_a_list(list_of_str=extra_cols, join_word='and')}"
        )
    return None


def _check_dataframe_minimum_column_set(
    df: pd.DataFrame,
) -> List[span_err.InvalidDataFrameMissingColumns]:
    existing_columns = set(df.columns)
    missing_cols = []
    for col in SPAN_OPENINFERENCE_REQUIRED_COLS:
        if col not in existing_columns:
            missing_cols.append(col)

    if missing_cols:
        return [span_err.InvalidDataFrameMissingColumns(missing_cols=missing_cols)]
    return []


def _check_dataframe_for_duplicate_columns(
    df: pd.DataFrame,
) -> List[span_err.InvalidDataFrameDuplicateColumns]:
    # Get the duplicated column names from the dataframe
    duplicate_columns = df.columns[df.columns.duplicated()]
    if not duplicate_columns.empty:
        return [span_err.InvalidDataFrameDuplicateColumns(duplicate_columns)]
    return []


# TODO(Kiko): Performance improvements
# We should try using:
# - Pandas any() and all() functions together with apply(), or
# - A combination of the following type checker functions from Pandas, i.e,
#   is_float_dtype. See link below
# https://github.com/pandas-dev/pandas/blob/f538741432edf55c6b9fb5d0d496d2dd1d7c2457/pandas/core/dtypes/common.py
def _check_dataframe_column_content_type(
    df: pd.DataFrame,
) -> List[span_err.InvalidDataFrameColumnContentTypes]:
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
    for col in SPAN_OPENINFERENCE_COLUMN_NAMES:
        if col not in df.columns:
            continue
        if col in SPAN_OPENINFERENCE_LIST_OF_DICT_COLS:
            for row in df[col]:
                if not isinstance(row, Iterable) and row in ASSUMED_MISSING_VALUES:
                    continue
                if not (is_list_of(row, dict) or is_array_of(row, dict)) or not all(
                    is_dict_of(val, key_allowed_types=str) for val in row
                ):
                    wrong_lists_of_dicts_cols.append(col)
                    break
        elif col in SPAN_OPENINFERENCE_DICT_COLS:
            if not all(
                True if row in ASSUMED_MISSING_VALUES else is_dict_of(row, key_allowed_types=str)
                for row in df[col]
            ):
                wrong_dicts_cols.append(col)
        elif col in SPAN_OPENINFERENCE_NUM_COLS:
            if not is_numeric_dtype(df[col]):
                wrong_numeric_cols.append(col)
        elif col in SPAN_OPENINFERENCE_BOOL_COLS:
            if not is_bool_dtype(df[col]):
                wrong_bools_cols.append(col)
        elif col in SPAN_OPENINFERENCE_TIME_COLS:
            # Accept strings and datetime objects
            if not all(
                True
                if row in ASSUMED_MISSING_VALUES
                else isinstance(row, (str, datetime, pd.Timestamp))
                for row in df[col]
            ):
                wrong_timestamp_cols.append(col)
        elif col in SPAN_OPENINFERENCE_JSON_STR_COLS:
            # We check the correctness of the JSON strings when we check the values
            # of the data in the dataframe
            if not all(
                True if row in ASSUMED_MISSING_VALUES else isinstance(row, str) for row in df[col]
            ):
                wrong_JSON_cols.append(col)
        else:
            # if not all(isinstance(row, str) if row not in skip_values else True for row in df[col]):
            if not all(
                True if row in ASSUMED_MISSING_VALUES else isinstance(row, str) for row in df[col]
            ):
                wrong_string_cols.append(col)

    errors = []
    if wrong_lists_of_dicts_cols:
        errors.append(
            span_err.InvalidDataFrameColumnContentTypes(
                invalid_type_cols=wrong_lists_of_dicts_cols,
                expected_type="lists of dictionaries with string keys",
            ),
        )
    if wrong_dicts_cols:
        errors.append(
            span_err.InvalidDataFrameColumnContentTypes(
                invalid_type_cols=wrong_dicts_cols,
                expected_type="dictionaries with string keys",
            ),
        )
    if wrong_numeric_cols:
        errors.append(
            span_err.InvalidDataFrameColumnContentTypes(
                invalid_type_cols=wrong_numeric_cols,
                expected_type="ints or floats",
            ),
        )
    if wrong_bools_cols:
        errors.append(
            span_err.InvalidDataFrameColumnContentTypes(
                invalid_type_cols=wrong_bools_cols,
                expected_type="bools",
            ),
        )
    if wrong_timestamp_cols:
        errors.append(
            span_err.InvalidDataFrameColumnContentTypes(
                invalid_type_cols=wrong_timestamp_cols,
                expected_type="datetime objects or formatted strings",
            ),
        )
    if wrong_JSON_cols:
        errors.append(
            span_err.InvalidDataFrameColumnContentTypes(
                invalid_type_cols=wrong_JSON_cols,
                expected_type="JSON strings",
            ),
        )
    if wrong_string_cols:
        errors.append(
            span_err.InvalidDataFrameColumnContentTypes(
                invalid_type_cols=wrong_string_cols,
                expected_type="strings",
            ),
        )
    return errors


# -----------------------
# DataFrame Values Checks
# -----------------------


def _check_string_value_length(
    df: pd.DataFrame,
    col_name: str,
    min_len: int,
    max_len: int,
    allow_nulls: bool,
) -> List[Union[span_err.InvalidMissingValueInColumn, span_err.InvalidStringLengthInColumn]]:
    if col_name not in df.columns:
        return []

    errors = []
    if not allow_nulls and df[col_name].isnull().any():
        errors.append(
            span_err.InvalidMissingValueInColumn(
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
            span_err.InvalidStringLengthInColumn(
                col_name=col_name,
                min_length=min_len,
                max_length=max_len,
            )
        )
    return errors


def _check_string_allowed_values(
    df: pd.DataFrame,
    col_name: str,
    allowed_values: List[str],
    allow_nulls: bool,
) -> List[
    Union[span_err.InvalidMissingValueInColumn, span_err.InvalidStringValueNotAllowedInColumn]
]:
    if col_name not in df.columns:
        return []

    errors = []
    if not allow_nulls and df[col_name].isnull().any():
        errors.append(
            span_err.InvalidMissingValueInColumn(
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
            span_err.InvalidStringValueNotAllowedInColumn(
                col_name=col_name,
                allowed_values=allowed_values,
            )
        )
    return errors


def _check_value_start_end_time(
    df: pd.DataFrame,
) -> List[
    Union[
        span_err.InvalidMissingValueInColumn,
        span_err.InvalidTimestampValueInColumn,
        span_err.InvalidStartAndEndTimeValuesInColumn,
    ]
]:
    errors = []
    errors += _check_value_timestamp(
        df=df,
        col_name=SPAN_START_TIME_COL_NAME,
        allow_nulls=False,
    )
    errors += _check_value_timestamp(
        df=df,
        col_name=SPAN_END_TIME_COL_NAME,
        allow_nulls=True,
    )
    if (
        SPAN_START_TIME_COL_NAME in df.columns
        and SPAN_END_TIME_COL_NAME in df.columns
        and (df[SPAN_START_TIME_COL_NAME] > df[SPAN_END_TIME_COL_NAME]).any()
    ):
        errors.append(
            span_err.InvalidStartAndEndTimeValuesInColumn(
                greater_col_name=SPAN_END_TIME_COL_NAME,
                less_col_name=SPAN_START_TIME_COL_NAME,
            )
        )
    return errors


def _check_value_timestamp(
    df: pd.DataFrame,
    col_name: str,
    allow_nulls: bool,
) -> List[Union[span_err.InvalidMissingValueInColumn, span_err.InvalidTimestampValueInColumn]]:
    # This check expects that timestamps have previously been converted to nanoseconds
    if col_name not in df.columns:
        return []

    errors = []
    if not allow_nulls and df[col_name].isnull().any():
        errors.append(
            span_err.InvalidMissingValueInColumn(
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
        return [span_err.InvalidTimestampValueInColumn(timestamp_col_name=col_name)]

    return []


# -----------------------
# Arrow Types Checks
# -----------------------
