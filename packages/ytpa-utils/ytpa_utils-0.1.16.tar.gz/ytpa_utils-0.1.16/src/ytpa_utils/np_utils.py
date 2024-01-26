# TODO: add tests for this module


from typing import Optional

import numpy as np
from scipy.interpolate import interp1d


def resample_arr(ts: np.ndarray,
                 data: np.ndarray,
                 period: float,
                 max_ts_gap: Optional[float] = None,
                 omit_zeroes: bool = False):
    """Resample columns of an array individually, handling issues with large gaps and zero values."""
    ts_resamp = np.arange(np.min(ts), np.max(ts), period) # starts at 0

    num_samps_resamp = len(ts_resamp)
    num_cols = data.shape[1]
    data_resamp = np.zeros((num_samps_resamp, num_cols), dtype='float')
    for i in range(num_cols):
        # remove zeroes (always keep important values)
        if omit_zeroes:
            mask: np.ndarray = (data[:, i] != 0)
            mask[0] = True
            ts_i = ts[mask]
            data_i = data[mask, i]
        else:
            ts_i = ts
            data_i = data[:, i]

        # interpolate
        if len(ts_i) <= 1:
            continue
        kind = 'cubic' if len(ts_i) >= 4 else 'linear'
        f = interp1d(ts_i, data_i, kind=kind, axis=0, fill_value="extrapolate") # , assume_sorted=True)#, copy=False)
        data_resamp[:, i] = f(ts_resamp)

        # replace spline interp over long gaps with linear interp
        if max_ts_gap is not None:
            ts_diff = ts_i[1:] - ts_i[:-1]
            idxs_gap = np.where(ts_diff >= max_ts_gap)[0] # left indices at large gaps
            for j in idxs_gap:
                j_resamp_left = np.argmin(np.abs(ts_resamp - ts_i[j])) # closest left and right indices in ts_resamp
                j_resamp_right = np.argmin(np.abs(ts_resamp - ts_i[j + 1]))
                num_samps = j_resamp_right - j_resamp_left + 1
                ii = np.linspace(1, 0, num_samps)
                data_resamp[j_resamp_left:j_resamp_right + 1, i] = ii * data_i[j] + (1 - ii) * data_i[j + 1]

    return ts_resamp, data_resamp
