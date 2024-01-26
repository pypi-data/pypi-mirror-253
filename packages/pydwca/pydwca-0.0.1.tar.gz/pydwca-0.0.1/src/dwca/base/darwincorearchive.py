from __future__ import annotations

import zipfile

from dwca.metadata import Metadata
from dwca.utils import Language


class DarwinCoreArchive:
    """
    Base class of this package. Represent a Darwin Core Archive file with all its elements
    """

    def __init__(self, title: str = "", language: str = "eng") -> None:
        super().__init__()
        self.__title__ = title
        self.__metadata__ = Metadata("eml.xml")
        for lang in Language:
            if lang.name.lower() == language.lower():
                self.__lang__ = lang
        return

    def get_title(self) -> str:
        return self.__title__

    def has_metadata(self) -> bool:
        return self.__metadata__.__metadata__ is not None

    def extensions(self) -> int:
        return len(self.__metadata__.__extensions__)

    @classmethod
    def from_archive(cls, path_to_archive: str) -> DarwinCoreArchive:
        archive = zipfile.ZipFile(path_to_archive, "r")
        index_file = archive.read("meta.xml")
        darwin_core = DarwinCoreArchive()
        darwin_core.__metadata__ = Metadata.from_string(index_file.decode(encoding="utf-8"))
        archive.close()
        return darwin_core

    def __repr__(self) -> str:
        return f"<Darwin Core Archive ({self.__title__} [{self.__lang__.name.lower()}])>"

    def __str__(self) -> str:
        return f"{self.__title__} [{self.__lang__.name.lower()}]"
