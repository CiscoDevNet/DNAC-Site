#!/usr/bin/env python

from __future__ import print_function
import json
import logging
import time
import calendar
import csv
from datetime import datetime
from argparse import ArgumentParser, REMAINDER
from util import get_url, post_sync, delete


def site2id(fqsn):
    parts = fqsn.split("/")
    path = '/'.join(parts[:-1])
    site = parts[-1]
    url="group?groupType=SITE&groupName={}".format(site)
    response = get_url(url)
    # cope with names

    for site in response['response']:

        if site['groupNameHierarchy'] == fqsn:
            return site['id']
    raise ValueError("No site {} found".format(fqsn))


def assign_devices(site_id, sites):
    devices = [{"ip" : ip} for ip in sites]
    print(devices)
    payload = {
    "device": devices
    }
    print(payload)
    response = post_sync("dna/intent/api/v1/site/{}/device".format(site_id), payload)
    print (json.dumps(response, indent=2))

if __name__ == "__main__":
    parser = ArgumentParser(description='Select options.')


    parser.add_argument('--site', type=str,
                        help="site name")
    parser.add_argument('rest', nargs=REMAINDER)
    parser.add_argument('-v', action='store_true',
                        help="verbose")
    args = parser.parse_args()
    if args.v:
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    if args.site:
        site_id = site2id(args.site)
        print(site_id)
        assign_devices(site_id, args.rest)
