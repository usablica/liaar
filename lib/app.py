'''
To retrieve and parse application setting and resources file
'''

from lib import path, parser


def get_app_setting(app_name):
    '''
    Get application's setting
    '''
    parsed_file = parser.load_and_parse(path.get_app_setting_filename(app_name))
    # add application name to setting dictionary
    parsed_file['name'] = app_name
    return parsed_file


def get_app_resources(app_name):
    pass
