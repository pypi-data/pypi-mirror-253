from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Group:
    name: str
    parent: str
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