'''
 Liaar v0.1.0
 By Afshin Mehrabani (@afshinmeh) - 2014
'''
from lib import settings, bootstrap, dir


# main
def main():
    # bootstrap
    args = bootstrap.intro()

    # source directory
    resources_dir = settings.RESOURCES_DIRECTORY

    # applications directory
    apps_dir = settings.APPS_DIRECTORY

    # applications file extension
    app_file_ext = settings.APP_FILE_EXTENSION

    # application's setting liaar
    app_setting_filename = settings.APP_SETTING_FILENAME

    print dir.get_resources_list(args.app_name)

    print dir.get_app_setting_filename(args.app_name)

    print resources_dir, apps_dir, app_file_ext, app_setting_filename

if __name__ == '__main__':
    main()
