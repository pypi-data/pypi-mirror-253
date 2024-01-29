import requests

import xprompt
from xprompt.constants import get_backend_endpoint


def login(user_email: str, password: str):
    backend_endpoint = get_backend_endpoint(xprompt.debug)
    try:
        headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            "accept": "application/json",
        }
        response = requests.post(
            f"{backend_endpoint}/token",
            headers=headers,
            data={"username": user_email, "password": password},
        )

        return response.json()

    except Exception:
        raise
