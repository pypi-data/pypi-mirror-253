from dataclasses import dataclass
from tallyerp.entities.masters.group import Group
from tallyerp.entities.api.response.masterImport import Envelope


@dataclass
class CreateGroupRequest:
    group: Group

@dataclass
class CreateGroupResponse:
    created: int
    altered: int
    deleted: int
