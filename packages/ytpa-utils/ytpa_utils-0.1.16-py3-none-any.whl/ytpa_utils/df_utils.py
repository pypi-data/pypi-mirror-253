""" Array, DataFrame, and SQL ops """

from typing import List, Optional, Dict
import datetime

import pandas as pd
import numpy as np

from .val_utils import is_subset, is_int_or_float
from .np_utils import resample_arr


pd.options.mode.chained_assignment = None



def join_on_dfs(df0: pd.DataFrame,
                df1: pd.DataFrame,
                index_keys: List[str],
                df0_keys_select: Optional[List[str]] = None,
                df1_keys_select: Optional[List[str]] = None) \
        -> pd.DataFrame:
    """
    Combine info from two DataFrames analogously to the SQL op:
        SELECT df0.col00, df0.col01, df1.col10 FROM df0 JOIN ON df0.index_key0 = df1.index_key0

    The index keys in df0 are treated like foreign keys into df1.

    A typical use case is where df0 has many records where groups of those records correspond to measurements of a
    single data source over time. The time-independent metadata/features for a data source is stored in a row of df1,
    which acts like a lookup table.
    """
    # make sure index keys exist in both DataFrames
    assert is_subset(index_keys, df0.columns)
    assert is_subset(index_keys, df1.columns)

    # make sure that no double-selection is happening
    if df0_keys_select and df1_keys_select:
        assert len(set(df0_keys_select).intersection(df1_keys_select)) == 0

    # perform select on df0
    if df0_keys_select is not None:
        df0_select = df0[df0_keys_select]
    else:
        df0_select = df0

    # turn index keys in df1 into multi-index
    df1_mindex = df1.set_index(index_keys, drop=True)

    # get index keys for all rows of df0
    ids_ = df0[index_keys].to_numpy().tolist()
    if len(index_keys) == 1:
        ids_ = [id_[0] for id_ in ids_]
    else:
        ids_ = [tuple(id_) for id_ in ids_]

    # perform select on df1
    assert is_subset(ids_, df1_mindex.index) # all ID keys in df0 must exist in df1's multi-index for the JOIN
    if df1_keys_select is not None:
        df1_select = df1_mindex.loc[ids_, df1_keys_select]
    else:
        df1_select = df1_mindex.loc[ids_]
    df1_select = df1_select.set_index(df0.index)

    # concatenate
    return pd.concat((df0_select, df1_select), axis=1)

def convert_mixed_df_to_array(df: pd.DataFrame,
                              cols: List[str]) \
        -> np.ndarray:
    """
    Convert DataFrame with mixed-type columns into a numpy array.
    Only converts numerical columns. Emits warning for non-numerical/list-type columns.
    """
    assert is_subset(cols, df.columns)

    data: List[np.ndarray] = []
    for col in cols:
        data_ = df[col]
        samp0 = data_.iloc[0]
        if is_int_or_float(samp0):
            data.append(data_.to_numpy()[:, np.newaxis])
        elif isinstance(samp0, list) and is_int_or_float(samp0[0]):
            data.append(np.array(list(data_)))
        else:
            raise Exception(f'convert_mixed_df_to_array() -> Column {col} has invalid data type {type(samp0)}.')

    return np.hstack(data)

def get_duplicate_idxs(df: pd.DataFrame,
                       colname: str) \
        -> pd.DataFrame:
    """
    Get duplicate indices for entries in a specified column of a DataFrame.

    Steps:
        - adds col with index values
        - group rows by specified column
        - aggregate rows into groups, add two cols with duplicate first appearance + row indices where duplicates appear
        - convert to DataFrame with index (first index) and one column (duplicate indices)
    """
    idxs = (df[[colname]].reset_index()
            .groupby([colname])['index']
            .agg(['first', tuple])
            .set_index('first')['tuple'])
    return idxs

def df_dt_codec(df: pd.DataFrame,
                opts: Dict[str, dict]):
    """
    In-place conversion of specified columns (keys of opts) between strings and datetimes with specified format.
    Input arg "opts" has a key for each column to be converted. For each column, the corresponding entry in "opts"
    is a dict with key 'func' that provides a conversion function for a DataFrame column.
    """
    for key, ops in opts.items():
        if key in df:
            df[key] = ops['func'](df[key])

def resample_one_df_in_time(df: pd.DataFrame,
                            period: int,  # seconds
                            cols_non_num: List[str],
                            cols_num: List[str],
                            col_ts: str,
                            max_ts_gap: Optional[float] = None,
                            omit_zeroes: bool = False) \
        -> pd.DataFrame:
    """
    Resample numerical values in one DataFrame.
    Each numerical column is resampled using cubic spline interpolation with the option to omit zeroes on a
    column-specific basis.
    """
    cols_non_data = cols_non_num + [col_ts]

    assert set(df) == set(cols_non_data + cols_num)

    # get time and numerical columns into ndarray format
    dt_start = df[col_ts].iloc[0]
    ts: np.ndarray = (df[col_ts] - dt_start).dt.total_seconds().to_numpy()  # timestamps in seconds
    data: np.ndarray = df.drop(columns=cols_non_data)[cols_num].to_numpy() # numerical data array

    assert ~np.any(np.isnan(data))  # NaNs cause undefined behavior in interp1d

    # interpolate
    ts_resamp, data_resamp = resample_arr(ts, data, period, max_ts_gap=max_ts_gap, omit_zeroes=omit_zeroes)

    # put together resampled DataFrame
    dt_resamp = dt_start + ts_resamp * datetime.timedelta(seconds=1)
    df_resamp = pd.concat((
        pd.DataFrame(data_resamp, columns=cols_num),
        pd.Series(dt_resamp, name=col_ts)
    ), axis=1)
    for col_id in cols_non_num:
        df_resamp[col_id] = df.iloc[0][col_id]

    return df_resamp