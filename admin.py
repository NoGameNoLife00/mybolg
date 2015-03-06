 #encoding=utf-8

from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqlamodel import ModelView
# from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op
from blogapp import app
from data_model import db, Tag, User, Category, Entry

admin = Admin(app, url='/blog/admin')


class MyAdminView(ModelView):
    # @expose('/')
    # def index(self):
    #    return self.render('/admin/index.html')

    def is_accessible(self):
        return True

admin.add_view(MyAdminView(Category, db.session))
admin.add_view(MyAdminView(Tag, db.session))
admin.add_view(MyAdminView(Entry, db.session))
admin.add_view(MyAdminView(User, db.session))

#文件管理
# path = op.join(op.dirname(__file__), 'static')
# admin.add_view(FileAdmin(path, '/static/', name='Static Files'))
