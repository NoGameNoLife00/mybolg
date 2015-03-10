#encoding=utf-8
from flask import url_for, redirect, request
from flask.ext.login import current_user, login_user, logout_user
from flask.ext.admin import Admin, BaseView, expose, helpers
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.base import AdminIndexView
from wtforms import fields, widgets
from werkzeug.security import generate_password_hash

from blogapp import app, db
# from data_model import *
from data_model import Tag, User, Category, Entry, Friend_link
from forms import *
# from forms import LoginForm, RegistrationForm, init_login
from config import REGISTRATION_CODE
# from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op


# Define wtforms widget and field
class CKTextAreaWidget(widgets.TextArea):

    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextField):
    widget = CKTextAreaWidget()


class MyAdminView(ModelView):

    form_overrides = dict(content=CKTextAreaField)

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'

    def is_accessible(self):
        return current_user.is_authenticated()


class MyAdminIndexView(AdminIndexView):

    @expose('/')
    def index(self):
        if not current_user.is_authenticated():
            return redirect(url_for('.login_view'))
        return super(MyAdminIndexView, self).index()

    @expose('/login/', methods=('GET', 'POST'))
    def login_view(self):
        # handle user login
        form = LoginForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = form.get_user()
            login_user(user)

        if current_user.is_authenticated():
            return redirect(url_for('.index'))
        link = '<p>Don\'t have an account? <a href="' + url_for('.register_view') + '">Click here to register.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/register/', methods=('GET', 'POST'))
    def register_view(self):
        form = RegistrationForm(request.form)
        if helpers.validate_form_on_submit(form):
            user = User()

            form.populate_obj(user)
            # we hash the users password to avoid saving it as plaintext in the db,
            # remove to use plain text:
            # user.password = generate_password_hash(form.password.data)

            db.session.add(user)
            db.session.commit()

            login_user(user)
            return redirect(url_for('.index'))
        link = '<p>Already have an account? <a href="' + url_for('.login_view') + '">Click here to log in.</a></p>'
        self._template_args['form'] = form
        self._template_args['link'] = link
        return super(MyAdminIndexView, self).index()

    @expose('/logout/')
    def logout_view(self):
        logout_user()
        return redirect(url_for('.index'))


# Initialize flask-login
init_login()

admin = Admin(app, url='/blog/admin', index_view=MyAdminIndexView(), base_template='/admin/master.html')


admin.add_view(MyAdminView(Category, db.session))
admin.add_view(MyAdminView(Tag, db.session))
admin.add_view(MyAdminView(Entry, db.session))
admin.add_view(MyAdminView(User, db.session))
admin.add_view(MyAdminView(Friend_link, db.session))
# file manage
# path = op.join(op.dirname(__file__), 'static')
# admin.add_view(FileAdmin(path, '/static/', name='Static Files'))
