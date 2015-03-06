 #encoding=utf-8
import os
DEBUG = True
CSRF_ENABLED = True
SECRET_KEY = 'develpment key'
OPENID_PROVIDERS = [
    {'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'},
    {'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
    {'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
    {'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
    {'name': 'MyOpenID', 'url': 'https://www.myopenid.com' }
]
POST_PRE_PAGE = 8
# MYSQL Setting
basedir = os.path.abspath(os.path.dirname(__file__))

MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '110244'
MYSQL_DB = 'app_bugcoding'

SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' \
                          % (MYSQL_USER, MYSQL_PASSWORD,
                             MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_POOL_RECYCLE = 5

#email server settings
MAIL_SERVER = 'localhost'
MAIL_PORT = 25
MAIL_USERNAME = None
MAIL_PASSWORD = None

#administrator list
ADMINS = ['NoGameNo_Life@163.com']