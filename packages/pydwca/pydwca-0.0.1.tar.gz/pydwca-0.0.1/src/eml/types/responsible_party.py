from __future__ import annotations

from lxml.etree import Element

from dwca.xml import XMLObject


class IndividualName(XMLObject):
    PRINCIPAL_TAG = "individualName"

    def __init__(self, given_name: str, sur_name: str) -> None:
        super().__init__()
        self.__given_name__ = given_name
        self.__sur_name__ = sur_name
        return

    @classmethod
    def parse(cls, root: Element) -> IndividualName:
        assert root.tag == cls.PRINCIPAL_TAG, "Individual name tag missing"
        return IndividualName(
            given_name=root.find("givenName").text,
            sur_name=root.find("surName").text
        )

    def to_element(self) -> Element:
        individual_name = super().to_element()
        given_name = Element("givenName")
        given_name.text = self.__given_name__
        sur_name = Element("surName")
        sur_name.text = self.__sur_name__
        individual_name.append(given_name)
        individual_name.append(sur_name)
        return individual_name

    def __str__(self) -> str:
        return f"{self.__sur_name__}, {self.__given_name__[0]}."

    def __repr__(self) -> str:
        return f"<IndividualName ({self})>"


class Address(object):
    def __init__(self) -> None:
        return


class ResponsibleParty(XMLObject):
    def __init__(self, tag: str, individual_name: IndividualName = None, organization_name: str = None) -> None:
        super().__init__()
        assert (
                individual_name is not None or
                organization_name is not None
        ), "Contributor must have an organization or individual name"
        self.PRINCIPAL_TAG = tag
        self.__individual_name__ = individual_name
        self.__organization_name__ = organization_name
        self.__mail__ = ""
        self.__address__ = None
        self.__url__ = ""
        return

    @classmethod
    def parse(cls, root: Element) -> ResponsibleParty:
        individual_name = None
        if root.find("individualName") is not None:
            individual_name = IndividualName.parse(root.find("individualName"))
        return ResponsibleParty(
            tag=root.tag,
            individual_name=individual_name,
            organization_name=root.find("organizationName").text,
        )

    def to_element(self) -> Element:
        responsible = super().to_element()
        if self.__organization_name__ is not None:
            organization_name = Element("organizationName")
            organization_name.text = self.__organization_name__
            responsible.append(organization_name)
        if self.__individual_name__ is not None:
            responsible.append(self.__individual_name__.to_element())
        return responsible

    def __str__(self) -> str:
        if self.__individual_name__ is not None:
            return str(self.__individual_name__)
        return self.__organization_name__

    def __repr__(self) -> str:
        return f"<Contributor ({self})>"
