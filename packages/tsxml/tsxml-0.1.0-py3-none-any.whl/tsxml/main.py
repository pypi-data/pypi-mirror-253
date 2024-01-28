""" Module for parsing TestStand XML to Python dictionary"""

import xmltodict

from .types import container, array, string, number, boolean


def parse(xml: str) -> dict:
    """Converts the given TestStand XML string to Python dictionary

    Args:
        xml (str): TestStand XML string of a variable.
        Eg:<?TS version="2019 (19.0.0.170)"?>
        <Prop Name='MyNumber' Type='Number' Flags='0x0'>
        <Value>0</Value>
        </Prop>

    Returns:
        dict: Python dictionary corresponding to the XML
    """
    tsxml_dict = xmltodict.parse(xml, postprocessor=postprocessor)
    return tsxml_dict


def postprocessor(path, key, value):
    """
    Post processor callback of xmltodict, which we use to further process the TestStand XML.

    This would be called several times while parsing the XML.
    We are only interested in manipulating the data when we get the key as "Prop"
    """
    # Initialize
    result = {"key": key, "value": value}

    if key == "Prop":
        data_type = value["@Type"]
        if data_type in ["String"]:
            result = string.parse(path, key, value)
        elif data_type in ["Number"]:
            result = number.parse(path, key, value)
        elif data_type in ["Boolean"]:
            result = boolean.parse(path, key, value)
        elif data_type in ["Obj"]:
            result = container.parse(path, key, value)
        elif data_type in ["Array"]:
            result = array.parse(path, key, value)

    return result["key"], result["value"]
