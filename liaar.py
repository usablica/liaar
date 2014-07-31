'''
 Liaar v0.1.0
 By Afshin Mehrabani (@afshinmeh) - 2014
'''
from lib import setting, bootstrap, path, parser, app, url, exception, route, twisted_handler


def main():
    # bootstrap
    args = bootstrap.intro()

    bootstrap.init_apps()

 #   print app.get_app_setting(args.app_name)
 #   print url.resource_url(app.get_app_setting(args.app_name))



    twisted_handler.start()


if __name__ == '__main__':
    main()
