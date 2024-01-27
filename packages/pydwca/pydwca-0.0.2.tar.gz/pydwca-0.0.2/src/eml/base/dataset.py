from __future__ import annotations

from typing import Dict

import lxml.etree as et

from dwca.utils import Language
from dwca.xml import XMLObject
from eml.types import StringI18n
from eml.types.responsible_party import ResponsibleParty


class EMLTitle(StringI18n):
    PRINCIPAL_TAG = "title"

    def to_element(self) -> et.Element:
        return super().to_element()

    @classmethod
    def initialize(cls, text: str, lang: Language = Language.ENG) -> EMLTitle:
        return EMLTitle(text, lang)


class EMLDataset(XMLObject):
    PRINCIPAL_TAG = "dataset"

    def __init__(self) -> None:
        super().__init__()
        self.__title__ = None
        self.__creator__ = None
        self.__metadata_provider__ = None
        return

    @property
    def title(self) -> str:
        if self.__title__ is not None:
            return self.__title__.text
        else:
            return ""

    @classmethod
    def parse(cls, element: et.Element, nmap: Dict) -> EMLDataset:
        eml_dataset = EMLDataset()
        title = element.find("title")
        if title is not None:
            eml_dataset.__title__ = EMLTitle.parse(title)
        creator = element.find("creator")
        if creator is not None:
            eml_dataset.__creator__ = ResponsibleParty.parse(creator)
        metadata_provider = element.find("metadataProvider")
        if metadata_provider is not None:
            eml_dataset.__metadata_provider__ = ResponsibleParty.parse(metadata_provider)
        return eml_dataset

    def to_element(self) -> et.Element:
        dataset = super().to_element()
        if self.__title__ is not None:
            dataset.append(self.__title__.to_element())
        if self.__creator__ is not None:
            dataset.append(self.__creator__.to_element())
        if self.__metadata_provider__ is not None:
            dataset.append(self.__metadata_provider__.to_element())
        return dataset
