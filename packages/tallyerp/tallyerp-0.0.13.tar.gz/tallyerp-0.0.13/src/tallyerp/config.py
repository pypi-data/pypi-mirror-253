import os
import xml.etree.ElementTree as gfg


tallyMasterImportBody = {
    "HEADER": {
        "VERSION": 1,
        "TALLYREQUEST": "Import",
        "TYPE": "Data",
        "ID": "All Masters",
    },
    "BODY": {
        "DESC": {"STATICVARIABLES": {"IMPORTDUPS": "@@DUPCOMBINE"}},
        "DATA": {"TALLYMESSAGE": {}},
    },
}


TALLY_URL_ENV_KEY = "TALLY_API_URL"


class TallyRequestTemplate:
    masterImport = tallyMasterImportBody
