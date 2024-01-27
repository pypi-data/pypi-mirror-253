from dataclasses import dataclass, field
from typing import Optional
from xsdata.formats.dataclass.serializers import XmlSerializer


@dataclass
class Ledger:
    name: str
    parent: str
    openingBalance: float
    _name: Optional[str] = field(
        default=None,
        metadata=dict(
            name="name",
            type="Attribute",
        ),
    )
    action: Optional[str] = field(
        default="Create",
        metadata=dict(
            name="action",
            type="Attribute",
        ),
    )

    def __post_init__(self):
        self._name = self.name

