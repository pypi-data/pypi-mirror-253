from __future__ import annotations

from typing import Dict

import lxml.etree as et
from dwca.utils import Language
from dwca.xml import XMLObject
from eml.base import EMLDataset, EMLMetadata


class EML(XMLObject):
    PRINCIPAL_TAG = "eml"
    NAMESPACE_TAG = "eml"

    def __init__(self, package_id: str) -> None:
        super().__init__()
        self.__schema_location__ = ""
        self.__package__ = package_id
        self.__system__ = ""
        self.__scope__ = ""
        self.__lang__: Language = Language.ENG
        self.__dataset__ = EMLDataset()
        self.__metadata__ = EMLMetadata()
        return

    @classmethod
    def parse(cls, root: et.Element, nsmap: Dict) -> EML:
        assert root.get("packageId", None) is not None, "`packageId` attribute is not present in document"
        eml = EML(root.get("packageId"))
        eml.__schema_location__ = root.get(f"{{{nsmap['xsi']}}}schemaLocation", "")
        eml.__system__ = root.get("system", "")
        eml.__scope__ = root.get("scope", "")
        eml.__lang__ = Language.get_language(root.get(f"{{{nsmap['xml']}}}lang"))
        eml.__dataset__ = EMLDataset.parse(root.find("dataset"))
        eml.__metadata__ = EMLMetadata.parse(root.find("additionalMetadata").find("metadata"))
        return eml

    def to_element(self) -> et.Element:
        root = et.Element(self.get_principal_tag())
        root.set("packageId", self.__package__)
        root.set(f"{{{self.NAMESPACES['xsi']}}}schemaLocation", self.__schema_location__)
        root.set("system", self.__system__)
        root.set("scope", self.__scope__)
        root.set(f"{{{self.NAMESPACES['xml']}}}lang", self.__lang__.name.lower())
        root.append(self.__dataset__.to_element())
        root.append(self.__metadata__.to_element())
        return root

    @property
    def package_id(self) -> str:
        return self.__package__

    @property
    def language(self) -> Language:
        return self.__lang__
