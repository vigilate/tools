#!/bin/python3

import os
import glob
import xml.etree.ElementTree as etree
from bottle import route, run, template

NS = {
    "rdf": "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "dc": "http://purl.org/dc/elements/1.1/"
}

for key in NS:
    etree.register_namespace(key, NS[key])

def add_samples(rss_root):
    entries = glob.glob("enabled_entries_rss/*.xml")
    for entry_file in entries:
        new_tree = etree.parse(entry_file)
        new_root = new_tree.getroot()
        new_entry_elem = new_root.getchildren()[0]
        rss_root.append(new_entry_elem)

@route('/download/nvd-rss.xml')
def index():
    tree = etree.parse("nvd-rss.xml")
    root = tree.getroot()
    add_samples(root)
    tree.write("new-rss.xml", xml_declaration=True, encoding='utf-8',method="xml")

    return open("new-rss.xml", "r").read()


if not os.path.isdir("enabled_entries_rss"):
    os.mkdir("entries_rss")
os.system("wget https://nvd.nist.gov/download/nvd-rss.xml")
    
run(host='localhost', port=8080)
