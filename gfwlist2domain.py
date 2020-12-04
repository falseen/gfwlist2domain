#!/usr/bin/python
# -*- coding: utf-8 -*-

import pkgutil
from urllib.parse import urlparse,unquote
import json
import logging
from argparse import ArgumentParser
import base64
import requests

__all__ = ['main']


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('-i', '--input', dest='input',
                      help='path to gfwlist', metavar='GFWLIST', default='gfwlist.txt')
    parser.add_argument('-o', '--output', dest='output',
                      help='path to output pac', metavar='PAC', default='pac.conf')
    return parser.parse_args()


def decode_gfwlist(content):
    # decode base64 if have to
    try:
        return base64.b64decode(content).decode("utf-8")
    except:
        return content.decode("utf-8")


def get_hostname(something):
    try:
        # quite enough for GFW
        if not something.startswith('http:'):
            something = 'http://' + something
        r = urlparse(something)
        return r.hostname
    except Exception as e:
        logging.error(e) 
        return None


def add_domain_to_set(s, something):
    hostname = get_hostname(something)
    
    if hostname is not None:
        hostname = unquote(hostname)
        if hostname.startswith('.'):
            hostname = hostname.lstrip('.')
        if hostname.endswith('/'):
            hostname = hostname.rstrip('/')
        if hostname:
            if len(hostname.split("."))>1:
                s.add(hostname)
                print(hostname)
            else:
                ignorelist.append(hostname)


def parse_gfwlist(content):
    with open('builtin.txt',"r") as f:
        builtin_str = f.read()
    builtin_rules = builtin_str.splitlines(False)
    gfwlist = content.splitlines(False)
    domains = set(builtin_rules)
    for line in gfwlist:
        if line.find('.*') >= 0:
            continue
        elif line.find('*') >= 0:
            line = line.replace('*', '/')
        if line.startswith('!'):
            continue
        elif line.startswith('['):
            continue
        elif line.startswith('@'):
            # ignore white list
            continue
        elif line.startswith('||'):
            add_domain_to_set(domains, line.lstrip('||'))
        elif line.startswith('|'):
            add_domain_to_set(domains, line.lstrip('|'))
        elif line.startswith('.'):
            add_domain_to_set(domains, line.lstrip('.'))
        else:
            add_domain_to_set(domains, line)
    # TODO: reduce ['www.google.com', 'google.com'] to ['google.com']
    return '\n'.join(domains)


gfwlist_url = "https://raw.githubusercontent.com/gfwlist/gfwlist/master/gfwlist.txt"
ignorelist = []


def main():
    args = parse_args()
    # with open("gfwlist.txt", 'rb') as f:
    #     content = f.read()
    r = requests.get(gfwlist_url)
    content = r.text
    with open("gfwlist.txt", 'w') as f:
        f.write(content)
    content = decode_gfwlist(content)
    domains = parse_gfwlist(content)
    with open("domain.txt", 'w') as f:
        f.write(domains)
    print(f"忽略:{ignorelist}")
        

if __name__ == '__main__':
    main()
