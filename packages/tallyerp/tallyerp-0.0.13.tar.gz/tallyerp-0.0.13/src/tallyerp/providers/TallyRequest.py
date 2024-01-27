from tallyerp.entities.masters.group import Group
from tallyerp.entities.api.request.masterImport import *
from xsdata.formats.dataclass.serializers import XmlSerializer


class TallyRequestProvider:
    def __init__(self):
        ...

    def getRequest(
        self, reqType: str, isMaster: bool, ledgers: List[Ledger] = [], groups: List[Group] = []
    ):
        tallyMessage = TallyMessage()
        for ledger in ledgers:
            tallyMessage.ledger.append(ledger)
        for group in groups:
            tallyMessage.group.append(group)
        data = Data(tallyMessage=tallyMessage)
        importDups = ImportDups()
        desc = Desc(StaticVariables=StaticVariables(importDups))
        body = Body(desc=desc, data=data)
        header = Header()
        # header.type = reqType
        if isMaster:
            header.id = "All Masters"
        envelope = Envelope(header=header, body=body)
        serializer = XmlSerializer()
        data = serializer.render(envelope)
        return data
    

