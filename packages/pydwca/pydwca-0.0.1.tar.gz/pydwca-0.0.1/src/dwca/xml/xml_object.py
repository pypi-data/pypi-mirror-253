from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Dict

import lxml.etree as et


class XMLObject(ABC):
    PRINCIPAL_TAG = "placeholder"
    NAMESPACE_TAG = None
    NAMESPACES = {
        "xml": "http://www.w3.org/XML/1998/namespace"
    }

    def __init__(self) -> None:
        self.__namespace__ = dict()
        for prefix, uri in self.NAMESPACES.items():
            self.__namespace__[prefix] = uri
        return

    @classmethod
    def from_xml(cls, file: str, encoding: str = "utf-8") -> XMLObject:
        with open(file, "r", encoding=encoding) as file:
            content = file.read()
        return cls.from_string(content)

    @classmethod
    def from_string(cls, text: str) -> XMLObject:
        root = et.fromstring(text)
        nsmap = dict()
        for prefix, uri in cls.NAMESPACES.items():
            nsmap[prefix] = uri
        for prefix, uri in root.nsmap.items():
            nsmap[prefix] = uri
        cls.check_principal_tag(root.tag, nsmap)
        xml_object = cls.parse(root, nsmap)
        xml_object.__namespace__ = nsmap
        return xml_object

    @classmethod
    @abstractmethod
    def parse(cls, element: et.Element, nmap: Dict) -> XMLObject | None:
        pass

    def to_xml(self) -> str:
        return et.tostring(self.to_element(), pretty_print=True).decode()

    @abstractmethod
    def to_element(self) -> et.Element:
        return et.Element(self.get_principal_tag(), nsmap=self.__namespace__)

    def get_principal_tag(self) -> str:
        if self.NAMESPACE_TAG is not None:
            return f"{{{self.__namespace__[self.NAMESPACE_TAG]}}}{self.PRINCIPAL_TAG}"
        if None in self.__namespace__:
            return f"{{{self.__namespace__[None]}}}{self.PRINCIPAL_TAG}"
        return self.PRINCIPAL_TAG

    @classmethod
    def check_principal_tag(cls, tag: str, nmap: Dict) -> None:
        if cls.NAMESPACE_TAG is not None:
            expected = f"{{{nmap[cls.NAMESPACE_TAG]}}}{cls.PRINCIPAL_TAG}"
        elif None in nmap:
            expected = f"{{{nmap[None]}}}{cls.PRINCIPAL_TAG}"
        else:
            expected = f"{cls.PRINCIPAL_TAG}"
        assert tag == expected, f"{tag} is not {expected}"

    def __str__(self) -> str:
        return self.to_xml()

    def __repr__(self) -> str:
        return f"<XMLObject tag={self.PRINCIPAL_TAG}>"
