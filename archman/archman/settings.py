# -*- coding=UTF-8 -*-


class Config(object):
    DEBUG = False
    SECRET_KEY = '8124uckmbUYIj3wr7*)(935okk)'

    PORT = 8000

    NGINX_URL = '//localhost:8080/'
    NGINX_PATH = 'd:\\srcode\\web_public'

    PROJECT_ABBR = u'档案管理'
    PROJECT_NAME = u'哈尔滨市人力资源市场档案管理系统'
    PROJECT_USER = u'哈尔滨市人力资源市场'

    FILE_DIR = 'archman'
    FILE_EXT = '.jpg'

    DB_USER = 'cmtech'
    DB_PASSWORD = 'cmtech.1123'
    DB_HOST = '125.211.221.215'
    DB_NAME = 'archman'


class DevelConfig(Config):
    DEBUG = True
