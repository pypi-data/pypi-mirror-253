from __future__ import annotations

from abc import ABC, abstractmethod

import lxml.etree as et

from dwca.utils import Language
from dwca.xml import XMLObject


class StringI18n(XMLObject, ABC):
    def __init__(self, text: str, lang: Language = Language.ENG) -> None:
        super().__init__()
        self.__text__ = text
        self.__lang__ = lang
        return

    @classmethod
    def parse(cls, root: et.Element) -> StringI18n:
        text = root.text
        lang = Language.get_language(root.get("lang", "eng"))
        return cls.initialize(text, lang=lang)

    @classmethod
    @abstractmethod
    def initialize(cls, text: str, lang: Language = Language.ENG) -> StringI18n:
        pass

    def to_element(self) -> et.Element:
        string_i18n = super().to_element()
        string_i18n.text = self.__text__
        string_i18n.set(f"{{{self.NAMESPACES['xml']}}}lang", self.__lang__.name.lower())
        return string_i18n
