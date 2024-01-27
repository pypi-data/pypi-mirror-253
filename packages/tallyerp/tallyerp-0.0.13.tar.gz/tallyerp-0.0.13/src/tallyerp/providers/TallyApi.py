import requests
import os
from tallyerp.config import TallyRequestTemplate, TALLY_URL_ENV_KEY
from .TallyResponse import TallyResponseProvider
from dataclasses import dataclass
from tallyerp.entities.api.response.masterImport import (
    Envelope as TallyMasterImportResponse,
)


class TallyAPIProvider:
    def __init__(self):
        self.url = os.environ[TALLY_URL_ENV_KEY]
        self.headers = {
            "Content-Type": "text/xml, UTF-8, UTF-16, ASCII",
            "Content-Type": "application/xml",
        }

    def masterImport(self, request: str) -> TallyMasterImportResponse:
        res = requests.request(
            "POST", self.url, data=request.encode("utf-8"), headers=self.headers
        )
        data = TallyResponseProvider().getResponse(res.text)
        if res.status_code != 200:
            raise Exception("Error while calling API")
        return TallyMasterImportResponse(BODY=data.BODY, HEADER=data.HEADER)
