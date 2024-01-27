from .IBase import MasterRepository
from tallyerp.config import TallyRequestTemplate
from tallyerp.providers.TallyRequest import TallyRequestProvider
from tallyerp.providers.TallyApi import TallyAPIProvider, TallyMasterImportResponse
from tallyerp.entities import Ledger
import xml


class LedgerRepository(MasterRepository):
    def __init__(self):
        self.reqBuilder = TallyRequestProvider()
        self.provider = TallyAPIProvider()

    def create(self, ledger: Ledger) -> TallyMasterImportResponse:
        request = self.reqBuilder.getRequest(
            reqType="Import", isMaster=True, ledgers=[ledger]
        )
        response = self.provider.masterImport(request)
        return response

