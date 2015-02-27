#coding:utf-8
"""
升级数据库
"""
from migrate.versioning import api
from config import SQLALCHEMY_MIGRATE_REPO, SQLALCHEMY_DATABASE_URI

api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print "Current database version: " + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))

