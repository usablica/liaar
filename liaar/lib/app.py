'''
To retrieve and parse application setting and resources file
'''

from liaar.lib import path, parser, exception, logger, setting
import re
import os


# to hold all applications' configuration in memory
apps = {}


def add_app(app_name, version, setting):
    '''
    Add a new application to in-memory dictionary
    '''
    apps[app_name] = {}
    apps[app_name][version] = {}
    apps[app_name][version]['resources'] = {}
    apps[app_name][version]['setting'] = setting
    # add log
    logger.info('Adding application `%s`' % app_name)


def add_resource(app_name, version, resource_name):
    '''
    Add a new resource to in-memory dictionary
    '''
    if not apps.has_key(app_name):
        exception.handle('Undefined `app_name`, call `add_app` before `add_resource`')

    if not apps[app_name].has_key(version):
        exception.handle('Undefined app version')

    apps[app_name][version]['resources'][resource_name] = {}

    # add log
    logger.info('Adding resource `%s` to application `%s`' % (resource_name, app_name))


def add_method(app_name, version, resource_name, method_name, method_setting):
    '''
    Add a new method to in-memory dictionary
    '''
    if not apps.has_key(app_name):
        exception.handle('Undefined `app_name`, call `add_app` before `add_resource`')

    if not apps[app_name].has_key(version):
        exception.handle('Undefined app version')

    if not apps[app_name][version]['resources'].has_key(resource_name):
        exception.handle('Undefined resource name')

    apps[app_name][version]['resources'][resource_name][method_name] = method_setting

    # add log
    logger.info('Adding method `%s` to resource `%s`' % (method_name, resource_name))


def get_method(app_name, version, resource_name, method_name):
    '''
    Get method's setting
    '''
    try:
        return apps[app_name][version]['resources'][resource_name][method_name]
    except KeyError:
        exception.handle('No method found')


def get_apps():
    '''
    To get all available applications
    '''

    apps_list = []

    apps_path = os.path.abspath(setting.APPS_DIRECTORY)

    for app_item in os.listdir(apps_path):
        # check if it's a directory
        app_abs_path = os.path.join(apps_path, app_item)
        if os.path.isdir(app_abs_path):
            apps_list.append(app_item)

    return apps_list


def get_resources(app_name):
    '''
    Get the list of resource directories
    '''
    resources_list = []

    resources_path = path.get_resources_abs_path(app_name)

    # get all files and folders from resource directory
    for resource in os.listdir(resources_path):
        # check if it's a directory
        resource_abs_path = os.path.abspath(os.path.join(resources_path,
                                                         resource))
        if os.path.isdir(resource_abs_path):
            resources_list.append(resource)

    return resources_list


def get_methods(app_name, resource_name):
    '''
    Get all methods of given resource name
    '''
    methods_list = []

    resource_abs_path = path.get_resource_abs_path(app_name, resource_name)

    for method_name in os.listdir(resource_abs_path):
        name_re = re.match('^(.+)\.json$', method_name)
        if name_re:
            methods_list.append(name_re.group(1))

    return methods_list


def get_app_setting(app_name):
    '''
    Get application's setting
    '''
    parsed_file = parser.load_and_parse(path.get_app_setting_filename(app_name))
    # add application name to setting dictionary
    parsed_file['name'] = app_name
    return parsed_file
