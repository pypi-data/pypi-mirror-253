import re
from collections import OrderedDict
from typing import Optional, List
from xml.etree import ElementTree
from xml.etree.ElementTree import Element

namespaces = {
    'c': 'http://midpoint.evolveum.com/xml/ns/public/common/common-3',
}


class MidpointObject(OrderedDict):
    def get_oid(self) -> Optional[str]:
        return self['OID']

    def get_name(self) -> Optional[str]:
        return self['Name']


class MidpointObjectList(List[MidpointObject]):

    def find_object(self, search_reference) -> Optional[MidpointObject]:
        for mp_obj in self:
            if search_reference in [mp_obj.get_oid(), mp_obj.get_name()]:
                return mp_obj

        return None


class MidpointTask(MidpointObject):

    def __init__(self, xml_entity: Element):
        super().__init__()
        self['OID'] = xml_entity.attrib['oid']
        self['Name'] = xml_entity.find('c:name', namespaces).text

        execution_status_entity = xml_entity.find('c:executionStatus', namespaces)

        # Execution status is renamed executionState since Midpoint 4.4
        if execution_status_entity is None:
            execution_status_entity = xml_entity.find('c:executionState', namespaces)

        self['Execution Status'] = execution_status_entity.text if execution_status_entity is not None else 'n/a'

        # Midpoint before version 4.2

        rs = xml_entity.find('c:resultStatus', namespaces)

        # As of Midpoint 4.2, the result has moved

        if rs is None:
            rs = xml_entity.find('c:operationExecution/c:status', namespaces)

        self['Result Status'] = rs.text if rs is not None else ''
        progress = xml_entity.find('c:progress', namespaces)
        self['Progress'] = progress.text if progress is not None else ''
        total = xml_entity.find('c:expectedTotal', namespaces)
        self['Expected Total'] = total.text if total is not None else ''


class MidpointResource(MidpointObject):

    def __init__(self, xml_entity: Element):
        super().__init__()
        self['OID'] = xml_entity.attrib['oid']
        self['Name'] = xml_entity.find('c:name', namespaces).text
        self['Availability Status'] = optional_text(
            xml_entity.find('c:operationalState/c:lastAvailabilityStatus', namespaces))


class MidpointUser(MidpointObject):

    def __init__(self, xml_entity: Element):
        super().__init__()
        self['OID'] = xml_entity.attrib['oid']
        self['Name'] = xml_entity.find('c:name', namespaces).text
        self['Title'] = optional_text(xml_entity.find('c:title', namespaces))
        self['FullName'] = optional_text(xml_entity.find('c:fullName', namespaces))
        self['Status'] = xml_entity.find('c:activation/c:effectiveStatus', namespaces).text
        self['EmpNo'] = optional_text(xml_entity.find('c:employeeNumber', namespaces))
        self['Email'] = optional_text(xml_entity.find('c:emailAddress', namespaces))
        self['OU'] = optional_text(xml_entity.find('c:organizationalUnit', namespaces))

        extfields = xml_entity.find('c:extension', namespaces)

        if extfields is not None:
            for extfield in extfields:
                self[re.sub(r'{.*}', '', extfield.tag)] = extfield.text


class MidpointOrganization(MidpointObject):

    def __init__(self, xml_entity: Element):
        super().__init__()
        self['OID'] = xml_entity.attrib['oid']
        self['Name'] = xml_entity.find('c:name', namespaces).text
        self['DisplayName'] = xml_entity.find('c:displayName', namespaces).text
        self['Status'] = xml_entity.find('c:activation/c:effectiveStatus', namespaces).text
        parentorg = xml_entity.find('c:parentOrgRef', namespaces)
        self['Parent'] = None if parentorg is None else parentorg.attrib['oid']


endpoints = {
    "ConnectorType": "connectors",
    "ConnectorHostType": "connectorHosts",
    "GenericObjectType": "genericObjects",
    "ResourceType": "resources",
    "UserType": "users",
    "ObjectTemplateType": "objectTemplates",
    "SystemConfigurationType": "systemConfigurations",
    "TaskType": "tasks",
    "ShadowType": "shadows",
    "RoleType": "roles",
    "ValuePolicyType": "valuePolicies",
    "OrgType": "orgs",
    "FunctionLibraryType": "functionLibraries"
}


def optional_text(node: ElementTree):
    return node.text if node is not None else None
