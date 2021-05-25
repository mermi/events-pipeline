import json
import jsonschema
import logging
from jsonschema import validate

logger = logging.getLogger(f'logging_steps')

def get_schema():
    """This function loads the given schema available"""
    with open('shared_utils/configs/schema.json', 'r') as file:
        schema = json.load(file)
    return schema


def validate_json(json_data):
    """REF: https://json-schema.org/ """
    # Describe what kind of json you expect.
    execute_api_schema = get_schema()

    try:
        validate(instance=json_data, schema=execute_api_schema)
    except jsonschema.exceptions.ValidationError as err:
        logger.info(err)
        err = "Given JSON data is InValid"
        return False, err

    message = "Given JSON data is Valid"
    return True, message

def validate_data():
    with open('shared_utils/data/flink_data_engieering_sample_data.json', 'r') as sample:
        for line in sample:
            line = json.loads(line.strip())
            is_valid, msg = validate_json(line)
            logger.info(msg)
    return is_valid
