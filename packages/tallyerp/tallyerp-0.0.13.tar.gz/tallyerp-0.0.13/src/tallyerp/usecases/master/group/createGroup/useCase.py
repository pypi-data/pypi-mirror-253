from .dto import CreateGroupRequest, CreateGroupResponse
from tallyerp.repositories.masters.Group import GroupRepository


class CreateGroupUseCase:
    def __init__(self, req: CreateGroupRequest):
        self.request = req
        self.repo = GroupRepository()

    def execute(self) -> CreateGroupResponse:
        res = self.repo.create(self.request.group)
        if res.BODY.DATA.LINEERROR: 
            raise Exception(res.BODY.DATA.LINEERROR)
        return CreateGroupResponse(
            created=res.BODY.DATA.IMPORTRESULT.CREATED,
            altered=res.BODY.DATA.IMPORTRESULT.ALTERED,
            deleted=res.BODY.DATA.IMPORTRESULT.DELETED,
        )
