from typing import Any, List

from arize.pandas.validation.errors import ValidationError
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


class InvalidDataFrameColumnNames(ValidationError):
    def __repr__(self) -> str:
        return "Invalid_DataFrame_Column_Names"

    def __init__(self, column_names: Any) -> None:
        self.column_names = column_names

    def error_message(self) -> str:
        raise NotImplementedError
        return (f"Found {type(self.column_names)}",)


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


# -----------------------
# DataFrame Values Checks
# -----------------------

# -----------------------
# Arrow Types Checks
# -----------------------
