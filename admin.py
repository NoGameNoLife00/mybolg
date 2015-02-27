

from flask.ext.admin import Admin, BaseView, expose
from flask.ext.admin.contrib.sqla import ModelView

from blogapp import app
from data_model import *

admin = Admin(app)


class MyAdminView(ModelView):
#    @expose('/')
 #   def index(self):
  #      return self.render('index.html')

    def is_accessible(self):
        return True

admin.add_View(MyAdminView(Entries, db.session))
