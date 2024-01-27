from dataclasses import dataclass, field


@dataclass
class CompInfo:
    COMPANY: str
    GROUP: int
    LEDGER: int
    STOCKITEM: int
    
@dataclass
class IdInfo:
    LASTCREATEDVCHID: str

@dataclass
class CmpInfoEx:
    IDINFO: IdInfo

    