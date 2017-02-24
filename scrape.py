# coding=utf-8

from scrapely import Scraper
import boto3
import os
import re
import requests


# AWS Settings
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME')

# AWS File keys for training data
TRAINING_FILE_KEY = os.environ.get('TRAINING_FILE_KEY', 'Training/example.html')
TRAINING_DATA_KEY = os.environ.get('TRAINING_DATA_KEY', 'Training/data.json')


cleanr = re.compile('<.*?>')


def clean(text):
    """
    Remove html tags and whitespace from a piece of text.
    """
    text = text.strip()
    text = re.sub(cleanr, '', text)
    return text

scraper = Scraper()
s3client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

training_file_url = s3client.generate_presigned_url('get_object', {'Bucket': AWS_S3_BUCKET_NAME, 'Key': TRAINING_FILE_KEY})
training_data_file_url = s3client.generate_presigned_url('get_object', {'Bucket': AWS_S3_BUCKET_NAME, 'Key': TRAINING_DATA_KEY})
training_data = requests.get(training_data_file_url).json()
scraper.train(training_file_url, training_data)

objects = s3client.list_objects(Bucket=AWS_S3_BUCKET_NAME)
file_keys = [x['Key'] for x in objects['Contents']]

tasks = []
for file_key in file_keys:
    url = s3client.generate_presigned_url('get_object', {'Bucket': AWS_S3_BUCKET_NAME, 'Key': file_key})

    try:
        results = scraper.scrape(url)
    except:
        print 'Failed to scrape %s' % file_key
        continue
    else:
        print 'Scraped %s' % file_key

    task = {}
    for k, v in results[0].items():
        task[k] = clean(v[0])

    tasks.append(task)
