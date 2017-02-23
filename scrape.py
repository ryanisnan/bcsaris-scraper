# coding=utf-8

from scrapely import Scraper
import boto3
import re
import os

cleanr = re.compile('<.*?>')

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME')


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
s3client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY
)

training_url = s3client.generate_presigned_url('get_object', {'Bucket': AWS_S3_BUCKET_NAME, 'Key': '2007/AutoSave_10.htm'})
training_data = {
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
s.train(training_url, training_data)

objects = s3client.list_objects(Bucket=AWS_S3_BUCKET_NAME)
file_keys = [x['Key'] for x in objects['Contents']]

for file_key in file_keys:
    url = s3client.generate_presigned_url('get_object', {'Bucket': AWS_S3_BUCKET_NAME, 'Key': file_key})
    results = s.scrape(url)

    for k, v in results[0].items():
        print '%s: %s' % (k, clean(v[0]))
