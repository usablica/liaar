'''
 Liaar v0.1.0
 By Afshin Mehrabani (@afshinmeh) - 2014
'''
from lib import setting, bootstrap, path, parser, app, url, exception, route, twisted_handler


def main():
    # bootstrap
    args = bootstrap.intro()

 #   print app.get_app_setting(args.app_name)
 #   print url.resource_url(app.get_app_setting(args.app_name))

    route.add('/', 'root')
    route.add(setting.APP_URL_FORMAT, 'app')
    route.add(setting.APP_URL_FORMAT +
              setting.APP_RESOURCE_URL_FORMAT, 'resource')
    route.add(setting.APP_URL_FORMAT +
              setting.APP_RESOURCE_URL_FORMAT +
              setting.APP_METHOD_URL_FORMAT, 'method')

    bootstrap.init_apps()

    twisted_handler.start()


if __name__ == '__main__':
    main()
