#coding=utf-8
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

# MYSQL Setting
basedir = os.path.abspath(os.path.dirname(__file__))

MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_USER = 'root'
MYSQL_PASSWORD = '110244'
MYSQL_DB = 'blogapp'

SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' \
                          % (MYSQL_USER, MYSQL_PASSWORD,
                             MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')