from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Union, List

from lxml import etree as et

from dwca.metadata import Field
from dwca.xml import XMLObject


class DataFile(XMLObject, ABC):
    def __init__(
            self,
            row_type: str,
            files: str,
            fields: List[Field],
            encoding: str = "utf-8",
            lines_terminated_by: str = "\n",
            fields_terminated_by: str = ",",
            fields_enclosed_by: str = "",
            ignore_header_lines: Union[List[Union[int, str]], int, str] = 0
    ) -> None:
        super().__init__()
        self.__row_type_url__ = row_type
        self.__files__ = files
        self.__fields__ = fields
        self.__encoding__ = encoding
        self.__lines_end__ = lines_terminated_by
        self.__fields_end__ = fields_terminated_by
        self.__fields_enclosed__ = fields_enclosed_by
        if isinstance(ignore_header_lines, List):
            self.__ignore_header_lines__ = [int(i) for i in ignore_header_lines]
        else:
            self.__ignore_header__ = [int(ignore_header_lines)]
        return

    def to_element(self) -> et.Element:
        element = super().to_element()
        element.set("rowType", self.__row_type_url__)
        element.set("encoding", self.__encoding__)
        element.set("linesTerminatedBy", self.__lines_end__)
        element.set("fieldsTerminatedBy", self.__fields_end__)
        element.set("fieldsEnclosedBy", self.__fields_enclosed__)
        element.set("ignoreHeaderLines", self.__ignore_header__)
        files = et.Element("files")
        files.append(et.Element("location", text=self.__files__))
        element.append(files)
        for field in self.__fields__:
            field_element = et.Element("field")
            field_element.text = field
            element.append(field_element)
        return element
