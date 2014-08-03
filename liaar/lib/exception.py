'''
In order to manage and handle exceptions and errors
'''


def handle(message, exception_detail=None):
    '''
    Raises an exception
    '''
    if exception_detail is not None:
        raise Exception(message + ' - %s' % exception_detail)
    else:
        raise Exception(message)
