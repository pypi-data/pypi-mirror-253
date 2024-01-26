"""Utils for file I/O"""

import json
from typing import Union, List, Any
import pickle


def save_json(path: str,
              obj: Union[List[dict], dict],
              mode: str = 'w'):
    """Save object to JSON-formatted file."""
    with open(path, mode) as fp:
        json.dump(obj, fp, indent=4)

def load_json(fpath: str) -> Union[dict, list]:
    """Load from JSON-formatted file"""
    with open(fpath, 'r') as fp:
        return json.load(fp)

def save_pickle(fpath: str,
                obj: Any):
    """Save Python object to a pickle file"""
    with open(fpath, 'wb') as handle:
        pickle.dump(obj, handle, protocol=pickle.HIGHEST_PROTOCOL)

def load_pickle(fpath: str):
    """Load a Python object from a pickle file"""
    with open(fpath, 'rb') as handle:
        return pickle.load(handle)
