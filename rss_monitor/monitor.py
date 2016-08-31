#!/bin/python3

import os
import time
import feedparser
import requests

from dateutil.parser import parse as parse_date

PATH_BACKEND = "/home/exploit/backend/"

#f = feedparser.parse('http://nvd.nist.gov/download/nvd-rss.xml')
f = feedparser.parse('http://127.0.0.1:8080/download/nvd-rss.xml')

def get_value_meta(meta_content, key):
    for line in meta_content.split("\n"):
        k,v = line.split(":", 1)
        if k == key:
            return v
    return ""

def check_uptodate(last_date):
    path = PATH_BACKEND + "vulnerability_manager/nvd_db/"

    for target in ["Recent", "Modified"]:
        meta_file = "nvdcve-2.0-%s.meta" % target
        if not os.path.isfile(path + meta_file):
            return True
        meta_content = open(path + meta_file, "r").read()
        local_updated_date = parse_date(get_value_meta(meta_content, "lastModifiedDate"))
        if last_date > local_updated_date:
            return True
    return False

def do_update():
    requests.get("http://127.0.0.1/update_recent_cve")


def check():
    dates = []
    
    for v in f["entries"]:
        dates.append(parse_date(v["updated"]))
    dates.sort()

    if check_uptodate(dates[-1]):
        print("updating")
        do_update()
    else:
        print("no update", dates[-1])

if __name__ == "__main__":
    while True:
        print("checking")
        check()
        time.sleep(5)
