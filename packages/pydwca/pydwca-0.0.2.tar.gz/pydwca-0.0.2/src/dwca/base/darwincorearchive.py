from __future__ import annotations

import zipfile
from typing import List

from dwca.metadata import Metadata, Core, Extension
from dwca.utils import Language
from eml import EML


class DarwinCoreArchive:
    """
    Base class of this package. Represent a Darwin Core Archive file with all its elements
    """
    def __init__(self, title: str = "", language: str = "eng") -> None:
        super().__init__()
        self.__title__ = title
        self.__metadata__ = Metadata("meta.xml")
        for lang in Language:
            if lang.name.lower() == language.lower():
                self.__lang__ = lang
        self.__eml__ = None
        return

    @property
    def title(self) -> str:
        """
        str : The title of the Darwin Core Archive, equivalent to the
              title of the dataset in the EML metadata
        """
        return self.__title__

    @property
    def language(self) -> Language:
        """
        Language : Language of the Darwin Core
        """
        return self.__lang__

    def has_metadata(self) -> bool:
        """
        If the archive has a metadata file (eml.xml)

        Returns
        -------
        bool
            True if the archive has metadata, False otherwise
        """
        return self.__metadata__.metadata_filename is not None

    @property
    def core(self) -> Core:
        """
        Core : The file with the core of the archive
        """
        return self.__metadata__.__core__

    @property
    def extensions(self) -> List[Extension]:
        """
        List[Extension] : A list with the extension of the archive
        """
        return self.__metadata__.__extensions__

    @classmethod
    def from_archive(cls, path_to_archive: str) -> DarwinCoreArchive:
        archive = zipfile.ZipFile(path_to_archive, "r")
        index_file = archive.read("meta.xml")
        darwin_core = DarwinCoreArchive()
        darwin_core.__metadata__ = Metadata.from_string(index_file.decode(encoding="utf-8"))
        metadata_file = darwin_core.__metadata__.metadata_filename
        if metadata_file is not None:
            darwin_core.__eml__ = EML.from_string(archive.read(metadata_file).decode(encoding="utf-8"))
            darwin_core.__title__ = darwin_core.__eml__.title
            darwin_core.__lang__ = darwin_core.__eml__.language
        archive.close()
        return darwin_core

    def __repr__(self) -> str:
        return f"<Darwin Core Archive ({self.__title__} [{self.__lang__.name.lower()}])>"

    def __str__(self) -> str:
        return f"{self.__title__} [{self.__lang__.name.lower()}]"
