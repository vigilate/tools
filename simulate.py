#!/bin/python3

import argparse
import shutil
import os

PATH_BACKEND = "/home/exploit/backend/"

vuln_manager_src = 'vuln_manager_samples/%s.xml'
vuln_manager_dst = PATH_BACKEND + 'vulnerability_manager/nvd_db/nvdcve-2.0-Demo.xml'

rss_server_src = 'rss_server/entries_rss/%s.xml'
rss_server_dst = 'rss_server/enabled_entries_rss/%s.xml'

def simulate(test_name):
    os.makedirs('/'.join(vuln_manager_dst.split('/')[:-1]), True)
    shutil.copy(vuln_manager_src % (test_name), vuln_manager_dst)
    os.makedirs('/'.join(rss_server_dst.split('/')[:-1]), True)
    shutil.copy(rss_server_src % (test_name), rss_server_dst % (test_name))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('testName', type=str)

    args = parser.parse_args()
    simulate(args.testName)
