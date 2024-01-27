from tallyerp.entities.api.response.masterImport import Envelope
from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.context import XmlContext
from xsdata.formats.dataclass.parsers.config import ParserConfig


config = ParserConfig(
    base_url=None,
    load_dtd=False,
    process_xinclude=False,
    fail_on_unknown_properties=False,
    fail_on_unknown_attributes=False,
    fail_on_converter_warnings=False,
)


class TallyResponseProvider:
    def __init__(self):
        ...

    def getResponse(self, xmlData: str) -> Envelope:
        with open("/tmp/tallyresponse.xml", "w") as f:
            f.write(xmlData)
        parser = XmlParser(context=XmlContext(), config=config)
        response = parser.parse("/tmp/tallyresponse.xml", Envelope)
        return response
