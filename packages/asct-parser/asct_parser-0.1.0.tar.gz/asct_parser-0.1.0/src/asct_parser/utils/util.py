"""
Util functions for the package
"""
import json

import requests

ASCT_API = "https://apps.humanatlas.io/asctb-api/v2/"


def load_asctb(gid: str, sheet_id: str) -> dict:
    """
    Call ASCT_API with sheet_id and gid
    """
    data = requests.get(f"{ASCT_API}{sheet_id}/{gid}").text
    data = json.loads(data)["data"]

    return data


def save_csv(dataframe, output):
    """
    Save DataFrame into CSV file
    """
    dataframe.to_csv(output, index=False)
