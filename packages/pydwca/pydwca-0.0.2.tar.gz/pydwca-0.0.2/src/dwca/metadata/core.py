from __future__ import annotations

from typing import List, Union, Dict

from lxml import etree as et

from dwca.metadata import DataFile, Field


class Core(DataFile):
    PRINCIPAL_TAG = "core"

    def __init__(
            self,
            row_type: str,
            files: str,
            fields: List[Field],
            _id: str | int = None,
            encoding: str = "utf-8",
            lines_terminated_by: str = "\n",
            fields_terminated_by: str = ",",
            fields_enclosed_by: str = "",
            ignore_header_lines: Union[List[Union[int, str]], int, str] = 0
    ) -> None:
        super().__init__(
            row_type, files, fields,
            encoding, lines_terminated_by,
            fields_terminated_by, fields_enclosed_by,
            ignore_header_lines
        )
        self.__id__ = int(_id)
        return

    @classmethod
    def parse(cls, element: et.Element, nsmap: Dict) -> Core | None:
        if element is None:
            return None
        fields = list()
        for field_tree in element.findall("field", namespaces=nsmap):
            field = Field.parse(field_tree, nsmap=nsmap)
            field.__namespace__ = nsmap
            fields.append(field)
        assert len(fields) >= 1, "Core must contain at least one field"
        core = Core(
            element.get("rowType"),
            element.find("files", namespaces=nsmap).find("location", namespaces=nsmap).text,
            fields,
            element.find("id", namespaces=nsmap).get("index", None),
            element.get("encoding", "utf-8"),
            element.get("linesTerminatedBy", "\n"),
            element.get("fieldsTerminatedBy", ","),
            element.get("fieldsEnclosedBy", ""),
            element.get("ignoreHeaderLines", 0)
        )
        core.__namespace__ = nsmap
        return core

    def to_element(self) -> et.Element:
        element = super().to_element()
        id_element = self.object_to_element("id")
        id_element.set("index", str(self.__id__))
        element.append(id_element)
        return element
