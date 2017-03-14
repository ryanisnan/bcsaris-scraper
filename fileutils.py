import json


DEFAULT_OUTPUT_JSON_FILEPATH = 'output/data.json'
OUTPUT_JSON_FILEPATH = None

DEFAULT_OUTPUT_CSV_FILEPATH = 'output/data.csv'
OUTPUT_CSV_FILEPATH = None


def get_output_json_filepath():
    """
    Get the output JSON filepath from the user (or take the default).
    """
    if OUTPUT_JSON_FILEPATH is None:
        OUTPUT_JSON_FILEPATH = raw_input('Where would you like to output the JSON output? Default: %s' % DEFAULT_OUTPUT_JSON_FILEPATH) or DEFAULT_OUTPUT_JSON_FILEPATH
    return OUTPUT_JSON_FILEPATH


def get_output_csv_filepath():
    """
    Get the output CSV filepath from the user (or take the default).
    """
    if OUTPUT_CSV_FILEPATH is None:
        OUTPUT_CSV_FILEPATH = raw_input('Where would you like to output the CSV output? Default: %s' % DEFAULT_OUTPUT_CSV_FILEPATH) or DEFAULT_OUTPUT_CSV_FILEPATH
    return OUTPUT_CSV_FILEPATH


def read_parsed_data():
    """
    Read parsed data from the output JSON file.
    """
    f = open(get_output_json_filepath(), 'r')
    data = f.read()
    if not data:
        return {}
    json.loads(data)
    f.close()
    return data


def write_parsed_data(parsed_data):
    """
    Write parsed data to the output JSON file.
    """
    f = open(get_output_json_filepath(), 'rw')
    f.truncate()
    f.seek(0)
    f.write(json.dumps(parsed_data))
    f.close()
