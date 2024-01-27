from .dto import CreateLedgerRequest, CreateLedgerResponse
from tallyerp.repositories.masters.Ledger import LedgerRepository


class CreateLedgerUseCase:
    def __init__(self, req: CreateLedgerRequest):
        self.request = req
        self.repo = LedgerRepository()

    def execute(self) -> CreateLedgerResponse:
        res = self.repo.create(self.request.ledger)
        if res.BODY.DATA.LINEERROR: 
            raise Exception(res.BODY.DATA.LINEERROR)
        return CreateLedgerResponse(
            created=res.BODY.DATA.IMPORTRESULT.CREATED,
            altered=res.BODY.DATA.IMPORTRESULT.ALTERED,
            deleted=res.BODY.DATA.IMPORTRESULT.DELETED,
        )
