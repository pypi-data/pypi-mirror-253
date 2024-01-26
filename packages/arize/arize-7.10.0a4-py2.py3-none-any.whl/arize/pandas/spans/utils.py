import json
from datetime import datetime
from typing import Any, Dict, Iterable, List, Optional, Union

import numpy as np
import pandas as pd
from arize.pandas.spans.constants import ASSUMED_MISSING_VALUES
from arize.utils.logging import logger

from .columns import DICT_COLS, LIST_OF_DICT_COLS, TIME_COLS

# NOTE(Kiko): This is a bit of a mess, some fields have dictionaries, some
# others have json strings...
# "attributes.embedding.embeddings",
# "attributes.llm.input_messages",
# "attributes.llm.output_messages",
# "attributes.retrieval.documents",
# "attributes.reranker.input_documents"
# "attributes.reranker.output_documents"
# And, inside each message
# "message.tool_calls", fortunately seems like it can be jsonifyed automatically
# as long as there is no numpy arrays

# INDETERMINE_MATH_VALUES = [
#     # pd.NA,
#     np.nan,
#     np.inf,
#     -np.inf,
# ]
#
#
# def replace_indetermine_math_values_with_none(df: pd.DataFrame) -> pd.DataFrame:
#     wrong_cols = [col for col in df.columns if df[col].isin(INDETERMINE_MATH_VALUES).any()]
#     if not wrong_cols:
#         return df
#
#     logger.warning(
#         "The following columns contain indetermined values (i.e., pd.NA, np.nan, np.inf, -np.inf) "
#         f"that will be replaced by None: {log_a_list(list_of_str=wrong_cols, join_word='and')}"
#     )
#     # return df.fillna(None)
#     replace_dict = {}
#     for val in INDETERMINE_MATH_VALUES:
#         replace_dict[val] = None
#     return df.replace(replace_dict)


def convert_timestamps(df: pd.DataFrame, fmt: str = "") -> pd.DataFrame:
    for col in TIME_COLS:
        df[col] = df[col].apply(lambda dt: _datetime_to_ns(dt, fmt))
    return df


def _datetime_to_ns(dt: Union[str, datetime], fmt: str) -> int:
    if isinstance(dt, str):
        try:
            ts = int(datetime.timestamp(datetime.strptime(dt, fmt)) * 1e9)
        except Exception as e:
            logger.error(
                f"Error parsing string '{dt}' to timestamp in nanoseconds "
                f"using the format '{fmt}': {e}"
            )
            raise e
        return ts
    elif isinstance(dt, datetime):
        try:
            ts = int(datetime.timestamp(dt) * 1e9)
        except Exception as e:
            logger.error(f"Error converting datetime object to nanoseconds: {e}")
            raise e
        return ts
    elif isinstance(dt, pd.Timestamp) or isinstance(pd.DatetimeIndex):
        try:
            ts = int(datetime.timestamp(dt.to_pydatetime()) * 1e9)
        except Exception as e:
            logger.error(f"Error converting pandas Timestamp to nanoseconds: {e}")
            raise e
        return ts
    elif isinstance(dt, (int, float)):
        # Assume value already in nanoseconds,
        # validate timestamps in validate_values
        return dt
    else:
        e = TypeError(f"Cannot convert type {type(dt)} to nanoseconds")
        logger.error(f"Error converting pandas Timestamp to nanoseconds: {e}")
        raise e


# NOTE(Kiko): Yet another problem: np arrays are not json serializable.
# Hence, I will assume the embeddings come as lists, not arrays
def jsonify_dictionaries(df: pd.DataFrame) -> pd.DataFrame:
    for col_name in DICT_COLS:
        if col_name not in df.columns:
            logger.debug(f"passing on {col_name}")
            continue
        logger.debug(f"jsonifying {col_name}")
        df[col_name] = df[col_name].apply(lambda d: _jsonify_dict(d))

    for col_name in LIST_OF_DICT_COLS:
        if col_name not in df.columns:
            logger.debug(f"passing on {col_name}")
            continue
        logger.debug(f"jsonifying {col_name}")
        df[col_name] = df[col_name].apply(
            lambda list_of_dicts: _jsonify_list_of_dicts(list_of_dicts)
        )
    return df


def _jsonify_list_of_dicts(
    list_of_dicts: Optional[Iterable[Dict[str, Any]]],
) -> Optional[List[str]]:
    if not isinstance(list_of_dicts, Iterable) and list_of_dicts in ASSUMED_MISSING_VALUES:
        return None
    list_of_json = []
    for d in list_of_dicts:
        list_of_json.append(_jsonify_dict(d))
    return list_of_json


def _jsonify_dict(d: Optional[Dict[str, Any]]) -> Optional[str]:
    if d in ASSUMED_MISSING_VALUES:
        return None
    # NOTE(Kiko): Do we need a new dictionary here?
    # new_d = {}
    # for k, v in d.items():
    #     if isinstance(v, np.ndarray):
    #         new_d[k] = v.tolist()
    #     else:
    #         new_d[k] = v
    for k, v in d.items():
        if isinstance(v, np.ndarray):
            d[k] = v.tolist()
    return json.dumps(d, ensure_ascii=False)
