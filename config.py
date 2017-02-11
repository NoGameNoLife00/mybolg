 #encoding=utf-8
import os

# sql seting from SAE
# from sae.const import (MYSQL_HOST, MYSQL_HOST_S,
#     MYSQL_PORT, MYSQL_USER, MYSQL_PASS, MYSQL_DB
# )

DEBUG = False
CSRF_ENABLED = True
SECRET_KEY = 'you-guess'
REGISTRATION_CODE = 'zhuchema'
POST_PRE_PAGE = 8
# MYSQL Setting
basedir = os.path.abspath(os.path.dirname(__file__))

MYSQL_HOST = 'localhost'
MYSQL_PORT = '3306'
MYSQL_USER = ''
MYSQL_PASS = ''
MYSQL_DB = ''

SQLALCHEMY_DATABASE_URI = 'mysql://%s:%s@%s:%s/%s' \
                          % (MYSQL_USER, MYSQL_PASS,
                             MYSQL_HOST, MYSQL_PORT, MYSQL_DB)
SQLALCHEMY_POOL_RECYCLE = 5

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')

# simpleMDE
ARTICLE_EDITOR = 'simplemde'

#email server settings
MAIL_SERVER = 'smtp.vip.163.com'
MAIL_PORT = 25
MAIL_USER_TLS = False
MAIL_USER_SSL = False
MAIL_USERNAME = ''
MAIL_PASSWORD = ''

#administrator list
ADMINS = []
