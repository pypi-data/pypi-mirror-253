from __future__ import annotations

from typing import Dict

from lxml import etree as et

from dwca.xml import XMLObject


class Extension(XMLObject):
    PRINCIPAL_TAG = "extension"

    def __init__(self, encoding: str = "utf-8") -> None:
        super().__init__()
        self.__encoding__ = encoding
        return

    @classmethod
    def parse(cls, element: et.Element, nsmap: Dict) -> Extension | None:
        if element is None:
            return None
        extension = Extension(encoding=element.get("encoding", "utf-8"))
        return extension

    def to_element(self) -> et.Element:
        element = super().to_element()
        return element
