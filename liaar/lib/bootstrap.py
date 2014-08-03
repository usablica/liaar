import argparse
from liaar.lib import app, path, parser


# to print the tool manual and other messages
def greeting():
    print """
 _      _
| |    (_)
| |     _  __ _  __ _ _ __
| |    | |/ _` |/ _` | '__|
| |____| | (_| | (_| | |
|______|_|\__,_|\__,_|_|
"""


def intro():
    # show greeting message
    greeting()

    # config arguments
    parser = argparse.ArgumentParser(description='Liaar creates a fake REST API using JSON files')

    return parser.parse_args()


def init_apps():
    '''
    To initialize and add all applications
    '''
    apps_list = app.get_apps()
    # add apps
    for app_name in apps_list:
        app_setting = app.get_app_setting(app_name)
        app.add_app(app_name, app_setting['version'], app_setting)

        # add resources
        resources_list = app.get_resources(app_name)
        for resource_name in resources_list:
            app.add_resource(app_name, app_setting['version'], resource_name)

            methods_list = app.get_methods(app_name, resource_name)

            # add methods
            for method_name in methods_list:
                method_filename = path.get_method_filename(app_name,
                                                           resource_name,
                                                           method_name)
                method_json = parser.load_and_parse(method_filename)
                app.add_method(app_name,
                               app_setting['version'],
                               resource_name,
                               method_name,
                               method_json)
