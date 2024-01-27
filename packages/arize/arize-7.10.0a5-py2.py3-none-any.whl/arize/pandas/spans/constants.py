import numpy as np

# The defualt format used to parse datetime objects from strings
DEFAULT_DATETIME_FMT = "%Y-%m-%dT%H:%M:%S.%f+00:00"
# List of values to be interpret as missing values through our logic
ASSUMED_MISSING_VALUES = (
    # pd.NA, -- Does not work when checking booleans
    None,
    np.nan,
    np.inf,
    -np.inf,
)
# Minumum/Maximum number of characters for ids in spans
SPAN_ID_MIN_STR_LENGTH = 12
SPAN_ID_MAX_STR_LENGTH = 128
# Minumum/Maximum number of characters for span name
SPAN_NAME_MIN_STR_LENGTH = 1
SPAN_NAME_MAX_STR_LENGTH = 50
# Minumum/Maximum number of characters for span name
SPAN_STATUS_MSG_MIN_STR_LENGTH = 0
SPAN_STATUS_MSG_MAX_STR_LENGTH = 10_000
