from tallyerp.entities.masters.ledger import Ledger
from tallyerp.entities.masters.group import Group
from tallyerp.usecases import *


class MasterGateway:
    def __init__(self):
        ...

    def createLedger(self, ledgerName:str, parent: str, openingBalance: int) -> CreateLedgerResponse:
        dto =  CreateLedgerRequest(
            ledger = Ledger(
                name = ledgerName,
                parent = parent,
                openingBalance = openingBalance,
                action="Create"
            )
        )
        useCase = CreateLedgerUseCase(dto)
        return useCase.execute()
    
    def createGroup(self, groupName: str, parent: str):
        dto = CreateGroupRequest(
            group=Group(
                name=groupName,
                parent=parent,
                action="Create"
            )
        )
        useCase = CreateGroupUseCase(dto)
        return useCase.execute()