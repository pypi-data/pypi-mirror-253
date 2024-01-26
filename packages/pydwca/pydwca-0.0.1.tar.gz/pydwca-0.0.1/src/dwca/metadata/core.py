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
        # TODO: Must have one field
        for field in element.findall("field", namespaces=nsmap):
            fields.append(Field.parse(field, nsmap=nsmap))
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
        return core

    def to_element(self) -> et.Element:
        element = super().to_element()
        return element
