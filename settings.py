import os


# AWS Settings
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
AWS_S3_BUCKET_NAME = os.environ.get('AWS_S3_BUCKET_NAME')

# AWS File keys for training data
TRAINING_FILE_KEY = os.environ.get('TRAINING_FILE_KEY', 'Training/example.html')
TRAINING_DATA_KEY = os.environ.get('TRAINING_DATA_KEY', 'Training/data.json')
