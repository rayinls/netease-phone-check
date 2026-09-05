
import requests

from .crypto import eapi
from .session import NeteaseSession


BASE_URL = "https://music.163.com"


class NeteaseClient:
    def __init__(self):
        self.session = NeteaseSession()

    def cellphone_existence_check(
        self,
        phone: str,
        countrycode: str = "86",
    ):
        path = "/api/cellphone/existence/check"

        payload = {
            "cellphone": phone,
            "countrycode": countrycode,
        }

        encrypted = eapi(
            path,
            payload,
        )

        response = self.session.post(
            BASE_URL + "/eapi/cellphone/existence/check",
            data=encrypted,
            headers={
                "Content-Type": (
                    "application/x-www-form-urlencoded"
                ),
            },
        )

        response.raise_for_status()

        return response.json()
