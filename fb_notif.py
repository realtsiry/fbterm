#!/usr/bin/python2

# Written by Tsiry Sandratraina

import sys
import xmltodict
import requests
from lxml import html
from colored import fg, attr

if len(sys.argv) == 1:
    print("Usage:")
    print("./fb_notif.py <facebook notifications RSS Feed URL>")
    exit()

xml = requests.get(sys.argv[1])
notifications = xmltodict.parse(xml.content)
rss = notifications['rss']['channel']['title']
print(fg(4) + attr(1) + (rss).encode('utf-8') + attr('reset'))
print('')

items = notifications['rss']['channel']['item']

for item in items:

    description = item['description']
    pubDate = item['pubDate']

    tree = html.fromstring("<div>" + description + "</div>")
    links = tree.xpath('//div//a/text()')
    div = tree.xpath('//div/text()')

    i = 0
    description = ""

    for link in links:
        description += fg(4) + attr(1) + link + attr('reset') + div[i]
        i += 1

    print(description.encode('utf-8'))
    print(pubDate.encode('utf-8'))
    print('')


