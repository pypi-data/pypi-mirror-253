from .IBase import MasterRepository
from tallyerp.config import TallyRequestTemplate
from tallyerp.providers.TallyRequest import TallyRequestProvider
from tallyerp.providers.TallyApi import TallyAPIProvider, TallyMasterImportResponse
from tallyerp.entities import Group
import xml


class GroupRepository(MasterRepository):
    def __init__(self):
        self.reqBuilder = TallyRequestProvider()
        self.provider = TallyAPIProvider()

    def create(self, group: Group) -> TallyMasterImportResponse:
        request = self.reqBuilder.getRequest(
            reqType="Import", isMaster=True, groups=[group]
        )
        response = self.provider.masterImport(request)
        return response

