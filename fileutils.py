import json
import os
import unicodecsv as csv


DEFAULT_OUTPUT_JSON_FILEPATH = 'output/data.json'
OUTPUT_JSON_FILEPATH = {}

DEFAULT_OUTPUT_CSV_FILEPATH = 'output/data.csv'
OUTPUT_CSV_FILEPATH = {}


def get_output_json_filepath():
    """
    Get the output JSON filepath from the user (or take the default).
    """
    if not OUTPUT_JSON_FILEPATH.get('filepath'):
        OUTPUT_JSON_FILEPATH['filepath'] = raw_input('Where would you like to output the JSON output? Default: %s' % DEFAULT_OUTPUT_JSON_FILEPATH) or DEFAULT_OUTPUT_JSON_FILEPATH
    return OUTPUT_JSON_FILEPATH['filepath']


def get_output_csv_filepath():
    """
    Get the output CSV filepath from the user (or take the default).
    """
    if not OUTPUT_CSV_FILEPATH.get('filepath'):
        OUTPUT_CSV_FILEPATH['filepath'] = raw_input('Where would you like to output the CSV output? Default: %s' % DEFAULT_OUTPUT_CSV_FILEPATH) or DEFAULT_OUTPUT_CSV_FILEPATH
    return OUTPUT_CSV_FILEPATH['filepath']


def read_parsed_data():
    """
    Read parsed data from the output JSON file.
    """
    try:
        f = open(get_output_json_filepath(), 'r')
    except IOError:
        print 'No output JSON file detected at %s - moving on' % get_output_json_filepath()
        data = {}
    else:
        data = f.read()
        data = json.loads(data)
        f.close()
    return data


def write_parsed_data(parsed_data):
    """
    Write parsed data to the output JSON file.
    """
    filepath = get_output_json_filepath()
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))
    f = open(get_output_json_filepath(), 'wb')
    f.truncate()
    f.seek(0)
    f.write(json.dumps(parsed_data))
    f.close()


def write_csv_data(data):
    """
    Write parsed data to the output JSON file.
    """
    filepath = get_output_csv_filepath()
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))

    f = open(filepath, 'wb')
    writer = csv.writer(f)

    for k, v in data.items():
        row = [v[k2] for k2 in sorted(v.keys())]
        writer.writerow(row)

    f.close()
