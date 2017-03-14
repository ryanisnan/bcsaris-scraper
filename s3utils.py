from settings import AWS_ACCESS_KEY_ID
from settings import AWS_SECRET_ACCESS_KEY
from settings import AWS_S3_BUCKET_NAME
import boto3


_s3_client = None


def get_s3_client():
    """
    Return an S3 client. Uses the singleton pattern.
    """
    if _s3_client is None:
        _s3_client = boto3.client(
            's3',
            aws_access_key_id=AWS_ACCESS_KEY_ID,
            aws_secret_access_key=AWS_SECRET_ACCESS_KEY
        )

    return _s3_client


def get_s3_file_url(file_key):
    """
    Generate a pre-signed URL for the given file key on S3. The URL
    is only valid for a small period of time.
    """
    s3_client = get_s3_client()
    return s3_client.generate_presigned_url('get_object', {'Bucket': AWS_S3_BUCKET_NAME, 'Key': file_key})


def get_s3_task_file_keys():
    """
    Return a list of task file keys from S3. This command ignores any files that
    start with the phrase Training (case insensitive).
    """
    s3_client = get_s3_client()
    objects = s3_client.list_objects(Bucket=AWS_S3_BUCKET_NAME)
    file_keys = [x['Key'] for x in objects['Contents'] if not x['Key'].lower().startswith('training')]
    return file_keys
