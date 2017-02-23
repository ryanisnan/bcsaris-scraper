# coding=utf-8

from scrapely import Scraper
import re

cleanr = re.compile('<.*?>')


def strip_html(text):
    """
    RemoveHTML tags from a piece of text.
    """
    text = re.sub(cleanr, '', text)
    return text


def clean(text):
    """
    Remove html tags and whitespace from a piece of text.
    """
    text = text.strip()
    text = strip_html(text)
    return text

s = Scraper()

url1 = 'https://s3-us-west-2.amazonaws.com/bcsaris/2007/AutoSave_10.htm'
data = {
    'Task Number': '074566',
    'SAR Manager': 'Ron Royston',
    'Reporting SAR Group': 'North Shore Rescue',
    'Contact Phone #': '604-443-2122',
    'Incident Location': 'Mount Seymour, North Vancouver',
    'Incident Province': 'British Columbia',
    'RCMP Number': '2007-087',
    'Tasking agency': 'File or response number',
    'Incident Occured': '2007/01/01 12:00',
    'First Response': '2007/01/01 12:09',
    'Resolved': '2007/01/01 22:10',
    # 'Latitude': '49 ° 23.28\' N HDD.DDD',
    # 'Longitude': '\r\n122 ° 56.53\' W HDD.DDD'
}
s.train(url1, data)

url2 = 'https://s3-us-west-2.amazonaws.com/bcsaris/2007/AutoSave_11.htm'
results = s.scrape(url2)

for k, v in results[0].items():
    print '%s: %s' % (k, clean(v[0]))
