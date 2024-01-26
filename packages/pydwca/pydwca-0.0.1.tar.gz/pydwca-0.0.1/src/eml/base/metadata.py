from __future__ import annotations

import datetime as dt

from lxml.etree import Element, SubElement

from dwca.xml import XMLObject


class EMLGbifMetadata(XMLObject):
    def __init__(self) -> None:
        super().__init__()
        self.__date_stamp__ = None
        self.__hierarchy_level__ = None
        self.__citation__ = None
        self.__resource_logo_url__ = None

    def to_element(self) -> Element:
        root = Element("gbif")
        if self.__date_stamp__ is not None:
            date_stamp = SubElement(root, "dateStamp")
            date_stamp.text = self.__date_stamp__.isoformat()
            root.append(date_stamp)
        if self.__hierarchy_level__ is not None:
            hierarchy_level = SubElement(root, "hierarchyLevel")
            hierarchy_level.text = self.__hierarchy_level__
        if self.__citation__ is not None:
            citation = SubElement(root, "citation")
            citation.text = self.__citation__
        if self.__resource_logo_url__ is not None:
            resource_logo = SubElement(root, "resourceLogoUrl")
            resource_logo.text = self.__resource_logo_url__
        return root

    @classmethod
    def parse(cls, root: Element) -> EMLGbifMetadata:
        assert root.tag == 'gbif', "GBIF tag not included"
        gbif_metadata = EMLGbifMetadata()
        date_stamp = root.find("dateStamp")
        if date_stamp is not None:
            gbif_metadata.__date_stamp__ = dt.datetime.fromisoformat(date_stamp.text)
        hierarchy_level = root.find("hierarchyLevel")
        if hierarchy_level is not None:
            gbif_metadata.__hierarchy_level__ = hierarchy_level.text
        citation = root.find("citation")
        if citation is not None:
            gbif_metadata.__citation__ = citation.text
        resource_logo = root.find("resourceLogoUrl")
        if resource_logo is not None:
            gbif_metadata.__resource_logo_url__ = resource_logo.text
        return gbif_metadata


class EMLMetadata(XMLObject):
    def __init__(self) -> None:
        super().__init__()
        self.__gbif__ = None
        return

    @classmethod
    def parse(cls, root: Element) -> EMLMetadata:
        assert root.tag == "metadata", "Metadata tag not included"
        metadata = EMLMetadata()
        gbif_metadata = root.find("gbif")
        if gbif_metadata is not None:
            metadata.__gbif__ = EMLGbifMetadata.parse(gbif_metadata)
        return metadata

    def to_element(self) -> Element:
        root = Element("additionalMetadata")
        actual_root = Element("metadata")
        root.append(actual_root)
        if self.__gbif__ is not None:
            actual_root.append(self.__gbif__.to_element())
        return root
