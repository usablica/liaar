'''
To parse and get the path of all parts
'''

import os
from liaar.lib import exception, setting


def get_resources_abs_path(app_name):
    '''
    Validate and return the resource directory
    '''
    abs_resources_dir = os.path.abspath(os.path.join(get_app_abs_path(app_name),
                                                     setting.RESOURCES_DIRECTORY))

    if os.path.isdir(abs_resources_dir):
        return abs_resources_dir
    else:
        exception.handle('Invalid resources directory: %s' % abs_resources_dir)


def get_resource_abs_path(app_name, resource_name):
    resource_abs_path = '%s/%s' % (get_resources_abs_path(app_name), resource_name)

    if os.path.isdir(resource_abs_path):
        return resource_abs_path
    else:
        exception.handle('Resource path does not exist: %s' % resource_name)


def get_app_abs_path(app_name):
    '''
    Get application absolute path
    '''
    app_abs_path = os.path.abspath(os.path.join(setting.APPS_DIRECTORY,
                                                app_name))

    if os.path.isdir(app_abs_path):
        return app_abs_path
    else:
        exception.handle('Invalid application directory: %s' % app_abs_path)


def get_app_file(filename):
    '''
    Get filename + application file extension
    '''
    return filename + '.' + setting.APP_FILE_EXTENSION


def get_method_filename(app_name, resource_name, method_name):
    method_abs_path = '%s/%s' % (get_resource_abs_path(app_name, resource_name), get_app_file(method_name))
    if os.path.isfile(method_abs_path):
        return method_abs_path
    else:
        exception.handle('Method file does not exist: %s' % method_name)


def get_app_setting_filename(app_name):
    '''
    Get application setting filename
    '''
    app_abs_path = get_app_abs_path(app_name)

    app_setting_filename = os.path.join(app_abs_path,
                                        get_app_file(setting.APP_SETTING_FILENAME))

    if os.path.isfile(app_setting_filename):
        return app_setting_filename
    else:
        exception.handle('The given application doesn\'t have setting file: %s' %
                        get_app_file(setting.APP_SETTING_FILENAME))
