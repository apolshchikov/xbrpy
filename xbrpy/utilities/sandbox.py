import xml.etree.ElementTree as ET
import lxml as lx
import re
from lxml import etree


def parse_xml(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    for child in root:
        try:
            print(child.tag, child.attrib['id'], child.text)
        except KeyError:
            pass

if __name__ == "__main__":
    xml_path = "../../resources/example/apa-20151231.xml"
    xsd_path = "../../resources/example/apa-20151231.xsd"
