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

    if args.resource:
        resources_dir = args.resource

    abs_resources_dir = dir.get_abs_path(resources_dir)

    print dir.get_resources_list(abs_resources_dir)

    print resources_dir

if __name__ == '__main__':
    main()
