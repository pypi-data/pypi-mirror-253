from typing import Any, List

from arize.pandas.validation.errors import ValidationError
from arize.utils.constants import (
    MAX_FUTURE_YEARS_FROM_CURRENT_TIME,
    MAX_PAST_YEARS_FROM_CURRENT_TIME,
)
from arize.utils.utils import log_a_list

# -------------------
# Direct Argument Checks
# -------------------


class InvalidTypeArgument(ValidationError):
    def __repr__(self) -> str:
        return "Invalid_Type_Argument"

    def __init__(self, arg_name: str, arg_type: str, wrong_arg: Any) -> None:
        self.arg_name = arg_name
        self.arg_type = arg_type
        self.wrong_arg = wrong_arg

    def error_message(self) -> str:
        return (
            f"The {self.arg_name} must be a {self.arg_type}. ",
            f"Found {type(self.wrong_arg)}",
        )


class InvalidDateTimeFromatType(ValidationError):
    def __repr__(self) -> str:
        return "Invalid_DateTime_Format_Type"

    def __init__(self, wrong_input: Any) -> None:
        self.wrong_input = wrong_input

    def error_message(self) -> str:
        return (
            "The date time format must be a string. ",
            f"Found {type(self.wrong_input)}",
        )


# ---------------------
# DataFrame Form Checks
# ---------------------


class InvalidDataFrameDuplicateColumns(ValidationError):
    def __repr__(self) -> str:
        return "Invalid_DataFrame_Duplicate_Columns"

    def __init__(self, duplicate_cols: List[str]) -> None:
        self.duplicate_cols = duplicate_cols

    def error_message(self) -> str:
        return (
            f"The following columns have duplicates in the dataframe: "
            f"{log_a_list(self.duplicate_cols, 'and')}"
        )


class InvalidDataFrameMissingColumns(ValidationError):
    def __repr__(self) -> str:
        return "Invalid_DataFrame_Missing_Columns"

    def __init__(self, missing_cols: List[str]) -> None:
        self.missing_cols = missing_cols

    def error_message(self) -> str:
        return (
            f"The following columns are missing in the dataframe and are required: "
            f"{log_a_list(self.missing_cols, 'and')}"
        )


class InvalidDataFrameColumnContentTypes(ValidationError):
    def __repr__(self) -> str:
        return "Invalid_DataFrame_Column_Content_Types"

    def __init__(self, invalid_type_cols: List[str], expected_type: str) -> None:
        self.invalid_type_cols = invalid_type_cols
        self.expected_type = expected_type

    def error_message(self) -> str:
        return (
            "Found dataframe columns containing the wrong data type. "
            f"The following columns should contain {self.expected_type}: "
            f"{log_a_list(self.invalid_type_cols, 'and')}"
        )


# -----------------------
# DataFrame Values Checks
# -----------------------


class InvalidMissingValueInColumn(ValidationError):
    def __repr__(self) -> str:
        return "Invalid_Missin_Value_In_Column"

    def __init__(self, col_name: str) -> None:
        self.col_name = col_name

    def error_message(self) -> str:
        return (
            f"The column '{self.col_name}' has at least one missing value. "
            "This column must not have missing values"
        )


class InvalidStringLengthInColumn(ValidationError):
    def __repr__(self) -> str:
        return "Invalid_String_Length_In_Column"

    def __init__(self, col_name: str, min_length: int, max_length: int) -> None:
        self.col_name = col_name
        self.min_length = min_length
        self.max_length = max_length

    def error_message(self) -> str:
        return (
            f"The column '{self.col_name}' contains invalid string values, "
            f"their length must be between {self.min_length} and {self.max_length}."
        )


class InvalidStringValueNotAllowedInColumn(ValidationError):
    def __repr__(self) -> str:
        return "Invalid_String_Value_Not_Allowed_In_Column"

    def __init__(self, col_name: str, allowed_values: List[str]) -> None:
        self.col_name = col_name
        self.allowed_values = allowed_values

    def error_message(self) -> str:
        return (
            f"The column '{self.col_name}' contains invalid string values. "
            f"Allowed values are {log_a_list(self.allowed_values,'and')}"
        )


class InvalidTimestampValueInColumn(ValidationError):
    def __repr__(self) -> str:
        return "Invalid_Timestamp_Value_In_Column"

    def __init__(self, timestamp_col_name: str) -> None:
        self.timestamp_col_name = timestamp_col_name

    def error_message(self) -> str:
        return (
            f"At least one timestamp in the column '{self.timestamp_col_name}' is out of range. "
            f"Timestamps must be within {MAX_FUTURE_YEARS_FROM_CURRENT_TIME} year "
            f"in the future and {MAX_PAST_YEARS_FROM_CURRENT_TIME} years in the past from "
            "the current time."
        )


class InvalidStartAndEndTimeValuesInColumn(ValidationError):
    def __repr__(self) -> str:
        return "Invalid_Start_And_End_Time_Values_In_Column"

    def __init__(self, greater_col_name: str, less_col_name: str) -> None:
        self.greater_col_name = greater_col_name
        self.less_col_name = less_col_name

    def error_message(self) -> str:
        return (
            f"Invalid span times. Values in column '{self.greater_col_name}' "
            f"should be greater than values in column '{self.less_col_name}'"
        )


# -----------------------
# Arrow Types Checks
# -----------------------
