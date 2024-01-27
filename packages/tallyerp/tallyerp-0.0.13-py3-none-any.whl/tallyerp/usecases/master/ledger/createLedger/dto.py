from dataclasses import dataclass

from tallyerp.entities.masters.ledger import Ledger
from tallyerp.entities.api.response.masterImport import Envelope


@dataclass
class CreateLedgerRequest:
    ledger: Ledger

@dataclass
class CreateLedgerResponse:
    created: int
    altered: int
    deleted: int
