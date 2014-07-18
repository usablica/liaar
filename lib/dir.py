import os
import settings


# validate and return the resource directory
def get_resources_abs_path(app_name):
    abs_resources_dir = os.path.abspath(os.path.join(get_app_abs_path(app_name),
                                                     settings.RESOURCES_DIRECTORY))

    if os.path.isdir(abs_resources_dir):
        return abs_resources_dir
    else:
        raise Exception('Invalid resources directory: %s' % abs_resources_dir)


# get the list of resource directories
def get_resources_list(app_name):
    resources_list = []

    resources_path = get_resources_abs_path(app_name)

    # get all files and folders from resource directory
    for resource in os.listdir(resources_path):
        # check if it's a directory
        resource_abs_path = os.path.abspath(os.path.join(resources_path,
                                                         resource))
        if os.path.isdir(resource_abs_path):
            resources_list.append(tuple([resource, resource_abs_path]))

    return resources_list


# check directory and JSON get resource file
def get_resource_file(resource_object):
    pass


# get application absolute path
def get_app_abs_path(app_name):
    app_abs_path = os.path.abspath(os.path.join(settings.APPS_DIRECTORY,
                                                app_name))

    if os.path.isdir(app_abs_path):
        return app_abs_path
    else:
        raise Exception('Invalid application directory: %s' % app_abs_path)


# get filename + application file extension
def get_app_file(filename):
    return filename + '.' + settings.APP_FILE_EXTENSION


# get application setting filename
def get_app_setting_filename(app_name):
    app_abs_path = get_app_abs_path(app_name)

    app_setting_filename = os.path.join(app_abs_path,
                                        get_app_file(settings.APP_SETTING_FILENAME))

    if os.path.isfile(app_setting_filename):
        return app_setting_filename
    else:
        raise Exception('The given application doesn\'t have setting file: %s' %
                        get_app_file(settings.APP_SETTING_FILENAME))
