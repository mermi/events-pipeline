def get_query(query_path, extension='sql'):
    """
    Parse the query based on the path
    :param query_path: str, path of the query
    :param extension: str, query extension
    :return: str, sql query
    """
    query_location = f'{query_path}.{extension}'
    with open(query_location, 'r+') as f:
        return f.read()
