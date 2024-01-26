from datetime import datetime
from itertools import chain
from typing import Any, Iterable, List, Optional

import pandas as pd
import pyarrow as pa
from arize.pandas.spans.columns import (
    BOOL_COLS,
    DICT_COLS,
    JSON_STR_COLS,
    LIST_OF_DICT_COLS,
    NUM_COLS,
    SPAN_OPEN_INFERENCE_COLUMN_NAMES,
    SPAN_OPEN_INFERENCE_REQUIRED_COLS,
    TIME_COLS,
)
from arize.pandas.spans.constants import ASSUMED_MISSING_VALUES
from arize.pandas.spans.validation import errors as span_err
from arize.pandas.validation import errors as err
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
    _warning_dataframe_column_names(dataframe)
    return list(
        chain(
            _check_dataframe_index(dataframe),
            _check_dataframe_minimum_column_set(dataframe),
            _check_dataframe_column_content_type(dataframe),
        )
    )


def validate_dataframe_values(
    dataframe: pd.DataFrame,
) -> List[err.ValidationError]:
    logger.warning("validate_dataframe_values is not implemented")
    return list(chain())


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


def _warning_dataframe_column_names(
    df: pd.DataFrame,
) -> None:
    extra_cols = [col for col in df.columns if col not in SPAN_OPEN_INFERENCE_COLUMN_NAMES]
    if extra_cols:
        logger.warning(
            "The following columns are not part of the Open Inference Specification "
            f"and will be ignored: {log_a_list(list_of_str=extra_cols, join_word='and')}"
        )
    return None


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
    for col in SPAN_OPEN_INFERENCE_COLUMN_NAMES:
        if col not in df.columns:
            continue
        if col in LIST_OF_DICT_COLS:
            for row in df[col]:
                if not isinstance(row, Iterable) and row in ASSUMED_MISSING_VALUES:
                    continue
                if not (is_list_of(row, dict) or is_array_of(row, dict)) or not all(
                    is_dict_of(val, key_allowed_types=str) for val in row
                ):
                    wrong_lists_of_dicts_cols.append(col)
                    break
        elif col in DICT_COLS:
            if not all(
                True if row in ASSUMED_MISSING_VALUES else is_dict_of(row, key_allowed_types=str)
                for row in df[col]
            ):
                wrong_dicts_cols.append(col)
        elif col in NUM_COLS:
            if not is_numeric_dtype(df[col]):
                wrong_numeric_cols.append(col)
        elif col in BOOL_COLS:
            if not is_bool_dtype(df[col]):
                wrong_bools_cols.append(col)
        elif col in TIME_COLS:
            # Accept strings and datetime objects
            if not all(
                True
                if row in ASSUMED_MISSING_VALUES
                else isinstance(row, (str, datetime, pd.Timestamp))
                for row in df[col]
            ):
                wrong_timestamp_cols.append(col)
        elif col in JSON_STR_COLS:
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


def _check_dataframe_minimum_column_set(
    df: pd.DataFrame,
) -> List[span_err.InvalidDataFrameMissingColumns]:
    existing_columns = set(df.columns)
    missing_cols = []
    for col in SPAN_OPEN_INFERENCE_REQUIRED_COLS:
        if col not in existing_columns:
            missing_cols.append(col)

    if missing_cols:
        return [span_err.InvalidDataFrameMissingColumns(missing_cols=missing_cols)]
    return []


# -----------------------
# DataFrame Values Checks
# -----------------------

# -----------------------
# Arrow Types Checks
# -----------------------
