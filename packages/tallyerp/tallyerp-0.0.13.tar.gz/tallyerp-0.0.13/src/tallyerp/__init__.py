from tallyerp.gateways.tally import TallyGateway
from tallyerp.config import TALLY_URL_ENV_KEY
import os

def connect(tallyURL: str = "http://localhost:9000"):
    if tallyURL:
        os.environ[TALLY_URL_ENV_KEY] = tallyURL
    return TallyGateway()