from io_gcs.utils import err_responses


def validate_data_structure(data, schema):
    ''' スキーマチェック '''
    # dictのチェック
    if isinstance(data, dict) and isinstance(schema, dict):
        # スキーマに定義されたkeyがdataにあること
        return all(k in data and validate_data_structure(data[k], schema[k]) for k in schema)
    # listのチェック
    if isinstance(data, list) and isinstance(schema, list):
        # list内の要素をチェック
        return all(validate_data_structure(d, schema[0]) for d in data)
    # dict, list以外の型チェック
    elif isinstance(type(data), type):
        return isinstance(data, schema)
    else:
        return False


def return_err_msg_if_invalid_data_structure(post_data, post_request_schema):
    if validate_data_structure(post_data, post_request_schema):
        return None
    else:
        loc_list = ['request body']
        msg = 'invalid request body.'
        err_type = 'invalid schema.'
        response = err_responses.response_with_err(loc_list, msg, err_type)
        return response
