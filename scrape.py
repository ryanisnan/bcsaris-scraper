# coding=utf-8

from fileutils import read_parsed_data
from fileutils import write_csv_data
from fileutils import write_parsed_data
from s3utils import get_s3_file_url
from s3utils import get_s3_task_file_keys
from scrapely import Scraper
from settings import TRAINING_DATA_KEY
from settings import TRAINING_FILE_KEY
import re
import requests


cleanr = re.compile('<.*?>')


def clean(text):
    """
    Remove html tags and whitespace from a piece of text.
    """
    text = text.strip(' \t\n\r')
    text = re.sub(cleanr, '', text)
    return text


scraper = Scraper()

training_file_url = get_s3_file_url(TRAINING_FILE_KEY)
training_data_file_url = get_s3_file_url(TRAINING_DATA_KEY)
training_data = requests.get(training_data_file_url).json()
scraper.train(training_file_url, training_data)


def main():
    data = read_parsed_data()

    file_keys = get_s3_task_file_keys()

    for file_key in file_keys:
        if file_key in data.keys():
            print 'Already parsed %s - skipping' % file_key
            continue

        url = get_s3_file_url(file_key)

        try:
            results = scraper.scrape(url)
        except:
            print 'Failed to scrape %s' % file_key
            continue
        else:
            print 'Scraped %s' % file_key

        task = {}
        for k, v in results[0].items():
            v = clean(v[0])

            if k == 'Task Number' and v.startswith('Task Number:&nbsp;'):
                v = v.replace('Task Number:&nbsp;', '')
                v = v.strip()

            task[k] = v

        data[file_key] = task

        write_parsed_data(data)

    write_csv_data(data)


main()
