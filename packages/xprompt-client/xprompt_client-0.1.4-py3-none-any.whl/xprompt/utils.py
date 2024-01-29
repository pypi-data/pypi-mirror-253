import time
from typing import Any

import requests

import xprompt
from xprompt.constants import get_backend_endpoint
from xprompt_common.errors import TryAgain


def exclude_json_none(json_dict: dict[str, Any]) -> dict[str, Any]:
    """
    Delete keys with the value ``None`` in a dictionary, recursively.

    This alters the input so you may wish to ``copy`` the dict first.
    """
    # For Python 3, write `list(d.items())`; `d.items()` won’t work
    # For Python 2, write `d.items()`; `d.iteritems()` won’t work
    for key, value in list(json_dict.items()):
        if value is None:
            del json_dict[key]
        elif isinstance(value, dict):
            exclude_json_none(value)
    return json_dict


def send_request_with_json(
    json_payload: dict[str, Any], endpoint: str, timeout: int = 10
):
    start = time.time()
    backend_endpoint = get_backend_endpoint(xprompt.debug)
    while True:
        try:
            headers = {
                "Content-Type": "application/json; charset=utf-8",
                "Authorization": f"Bearer {xprompt.api_key}",
            }

            response = requests.post(
                f"{backend_endpoint}/{endpoint}", headers=headers, json=json_payload
            )
            if response.status_code == 409:
                raise TryAgain("failed with conflict")

            if response.status_code >= 300:
                raise RuntimeError(response.text)

            return response
        except TryAgain:
            if timeout is not None and time.time() > start + timeout:
                raise
            time.sleep(1)


def send_request_with_file(file_paths: list[str], endpoint: str, timeout: int = 10):
    start = time.time()
    backend_endpoint = get_backend_endpoint(xprompt.debug)
    while True:
        try:
            headers = {
                "Authorization": f"Bearer {xprompt.api_key}",
            }

            files = [("files", open(fp, "rb")) for fp in file_paths]
            response = requests.post(
                f"{backend_endpoint}/{endpoint}", headers=headers, files=files
            )
            if response.status_code == 409:
                raise TryAgain("failed with conflict")

            if response.status_code >= 300:
                raise RuntimeError(response.text)

            break
        except TryAgain:
            if timeout is not None and time.time() > start + timeout:
                raise
            time.sleep(1)

    return response.json()
