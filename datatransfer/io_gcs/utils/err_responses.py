
def response_with_err(loc_list, msg, err_type):
    response_body = {
        "detail": [
            {
                "loc": loc_list,
                "msg": msg,
                "type": err_type
            }
        ]
    }
    return response_body


def err_500_response(file_loc, exception):
    ''' internal error用 err msg.
        args:
            file_loc: 呼び出し元の__name__
    '''
    loc_list = file_loc,
    msg = 'internal error. {}'.format(exception)
    err_type = '500 internal error'
    return response_with_err(loc_list, msg, err_type)