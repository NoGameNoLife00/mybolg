 #encoding=utf-8

from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView

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