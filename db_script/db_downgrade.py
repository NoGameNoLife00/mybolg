#coding:utf-8
"""
降低数据库版本
"""
from migrate.versioning import api
from config import SQLALCHEMY_MIGRATE_REPO, SQLALCHEMY_DATABASE_URI


api.downgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO,
              api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)-1)
print "Current database version: " + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))
