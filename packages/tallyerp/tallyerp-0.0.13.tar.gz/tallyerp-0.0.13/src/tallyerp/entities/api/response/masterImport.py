from dataclasses import dataclass, field
from typing import Optional, List
from tallyerp.entities import Ledger
from tallyerp.entities.masters.group import Group
from .common import *


@dataclass
class ImportResult:
    CREATED: int
    ALTERED: int
    DELETED: int


@dataclass
class Data:
    LINEERROR: Optional[str] = None
    IMPORTRESULT: ImportResult = None


@dataclass
class Desc:
    CMPINFO: CompInfo
    CMPINFOEX: CmpInfoEx


@dataclass
class Body:
    DATA: Data
    DESC: Desc = None


@dataclass
class Header:
    VERSION: int
    STATUS: str


@dataclass
class Envelope:
    HEADER: Header
    BODY: Body
