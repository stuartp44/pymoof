import base64
import getpass

import requests


def query(username, password):
    API_URL = "https://my.vanmoof.com/api/v8"

    # This api key is distributed by the official Vanmoof
    # app and as far as I can tell is universally the same on everyone's phone.
    API_KEY = "fcb38d47-f14b-30cf-843b-26283f6a5819"

    headers = {
        "Api-Key": API_KEY,
        "Authorization": "Basic "
        + base64.b64encode((username + ":" + password).encode()).decode("ascii"),
    }

    result = requests.post(API_URL + "/authenticate", headers=headers)
    result = result.json()

    if "error" in result:
        raise Exception("error", result)

    token = result["token"]

    headers = {
        "Api-Key": API_KEY,
        "Authorization": "Bearer " + token,
    }

    result = requests.get(
        API_URL + "/getCustomerData",
        headers=headers,
        params={"includeBikeDetails": ""},
    )
    result = result.json()

    return result["bikeDetails"]