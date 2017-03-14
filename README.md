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

#How it works
Step 1) Save the task files from BCSARIS as .html files

The task files themselves can either be manually saved, or automatically saved as HTML file using a link crawler while authenticated to the BCSARIS system. The integration with the BCSARIS system is outside the current scope for this project, and does not directly deal with exporting the HTML files from BCSARIS.

Step 2) Upload the files to S3 (Keep them private)

The project uses the [scrapely HTML scraping engine](https://github.com/scrapy/scrapely) to intelligently extract relevant data from the HTML files. Because of this dependency, this project requires that the HTML files be accessed online, hence using S3 as an intermediary file storage. Access through S3 is done through secure file access so the files need not (and should not) be made public under any circumstances.

Step 3) Create a training HTML file and training JSON data set

Scrapely doesn't work like most HTML/XML parsers in that it doesn't require the authors to manually specify where to extract data from. Rather it "trains" itself using an input HTML file and a corresponding JSON file that indicates what data to extract. A training file, for example might look like this:

```
{
    "Task Number": "55555",
    "SAR Manager": "Justin Trudeau",
    "Search Techniques Used": "01 - Vigorous flapping of the arms"
}
```

In this example training file, 3 attributes would be extracted from each task file. The training HTML file that you use must contain the data defined in the training JSON data. Note that only the values ("55555", "Justin Trudeau", "01 - Vigorous flapping of the arms") must exist in the training HTML file. The attribute names as defined in the training JSON file are arbitrary and only labeled sensibly for usability.

Step 4) Upload the training files to your S3 bucket.

Step 5) Set your environment variables (see [settings.py](https://github.com/ryanisnan/bcsaris-scraper/master/settings.py))

Step 6) Install the requirements using `pip install -r requirements.txt`

Step 7) Run the scraper with `python scrape.py`

It currently oututs the contents into a JSON file on your local drive as well as a CSV file containing the data. It will allow you to choose your output destinations, and will persist data between successive runs.
