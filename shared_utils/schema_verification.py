import json
import jsonschema
import logging
from jsonschema import validate

logger = logging.getLogger(f'logging_steps')

FILE_PATH_DATA = 'shared_utils/data/'
FILE_PATH_SCHEMA = 'shared_utils/configs/schema.json'

def get_schema():
    """
    This function loads the given schema available
    :param not expected any params
    :return the schema defined in the schema path
    """
    with open(f'{FILE_PATH_SCHEMA}', 'r') as file:
        schema = json.load(file)
    return schema


def get_number_lines(file_path):
    """
    This function returns the number of line in a given file
    :param a file path
    :return number of lines in that file
    """
    return len(open(file_path).readlines())


def validate_json(json_data):
    """
    REF: https://json-schema.org/ 
    This function given a defined schema from get_schema()
    the following will check if the parssed json data is valid or not
    :param json_data, in our case a line of the json file
    :return a dict of is_valid (True/False) the validation message and the paylod
    """
    # Describe what kind of json you expect.
    execute_api_schema = get_schema()
    try:
        validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError as err:
        logger.info(err)
        err = "Given JSON data is InValid"
        result = {
            'is_valid': False,
            'validation_message': err,
            'validated_payload': json_data
        }
    message = "Given JSON data is Valid"
    result = {
        'is_valid': True,
        'validation_message': message,
        'validated_payload': json_data
    }
    return result


def write_data_in_file(data):
    """
    This function will write the list to a json file, given the path
    :param the list of validated data
    :return the new file path
    """
    jsonObj = json.dumps(data)
    with open(f'{FILE_PATH_DATA}/validated_data.json', 'w') as file:
        file.write(jsonObj)


def validate_data():
    """
    This main function read the file and call the validator then write 
    in the list of JSON
    It wrties only the valid data and store them in a list
    Then write the list in a json file and stor it in FILE_PATH_DATA
    """
    validator_list = []
    with open(f'{FILE_PATH_DATA}/flink_data_engieering_sample_data.json', 'r') as sample:
        for line in sample:
            line = json.loads(line.strip())
            validation = validate_json(line)
            if validation.get('is_valid') == True:
                validator_list.append(validate_json(line))
    
    write_data_in_file(validator_list)

