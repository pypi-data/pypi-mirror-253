from __future__ import annotations

from typing import List, Dict

import lxml.etree as et

from dwca.metadata import Core, Extension
from dwca.xml import XMLObject


class Metadata(XMLObject):
    PRINCIPAL_TAG = "archive"

    def __init__(self, metadata: str = None) -> None:
        super().__init__()
        self.__metadata__ = metadata
        self.__core__ = None
        self.__extensions__: List[Extension] = list()
        return

    @classmethod
    def parse(cls, element: et.Element, nsmap: Dict) -> Metadata:
        metadata = Metadata(element.get("metadata", None))
        core = Core.parse(element.find(f"{{{nsmap[None]}}}core"), nsmap=nsmap)
        metadata.__core__ = core
        for extension in element.findall(f"{{{nsmap[None]}}}extension"):
            metadata.__extensions__.append(Extension.parse(extension, nsmap=nsmap))
        return metadata

    def to_element(self) -> et.Element:
        element = super().to_element()
        element.set("metadata", self.__metadata__)
        return element
