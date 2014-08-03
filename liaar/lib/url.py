'''
To produce URLs for resources, apps, etc.
'''

from liaar.lib import setting


def app_url(app_setting):
    '''
    Get the application's URL
    '''
    return setting.APP_URL_FORMAT.format('v' + app_setting['version'], app_setting['name'])


def resource_url(resource_name, app_setting):
    '''
    Get the resource's URL
    '''
    return app_url(app_setting) + setting.APP_RESOURCE_URL_FORMAT.format(resource_name)


def method_url(method_name, resource_name, app_setting):
    '''
    Get the method's URL
    '''
    return resource_url(resource_name, app_setting) + setting.APP_METHOD_URL_FORMAT.format(method_name)
