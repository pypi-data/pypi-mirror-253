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
