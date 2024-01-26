import json

from octoflow.data.loader import dataloader

try:
    from pandas import read_csv as pd_read_csv
except ImportError:
    pd_read_csv = None


__all__ = [
    "read_csv",
]


@dataloader(
    "csv",
    extensions=[".csv"],
    wraps=pd_read_csv,
    path_arg="filepath_or_buffer",
)
def read_csv(*args, **kwargs):
    return pd_read_csv(*args, **kwargs)


@dataloader(
    "json",
    extensions=[".json"],
    wraps=open,
    path_arg="file",
)
def read_json(*args, **kwargs):
    with open(*args, **kwargs) as f:
        data = json.load(f)
        if isinstance(data, dict):
            data = [data]
        return data
