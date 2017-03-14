Basic scraper for BCSARIS that extracts task information from BCSARIS files.

#Installation
To get this thing running you need Python 2.7+

    pip install requirements.txt

You must also set the following environment variables:

    AWS_ACCESS_KEY_ID
    AWS_SECRET_ACCESS_KEY
    AWS_S3_BUCKET_NAME

    TRAINING_FILE_KEY
    TRAINING_DATA_KEY

The files must currently be hosted on AWS S3, and `TRAINING_FILE_KEY` and `TRAINING_DATA_KEY` must correspond to keys that contain training data for the scraper.

#running
To run the scraper, simply run:

    python scrape.py

It currently oututs the contents into a JSON file on your local drive as well as a CSV file containing the data.
