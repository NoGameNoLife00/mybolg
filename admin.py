#encoding=utf-8
from flask import url_for, redirect, request
from flask.ext.login import current_user, login_user, logout_user
from flask.ext.admin import Admin, BaseView, expose, helpers
from flask.ext.admin.contrib.sqla import ModelView
from flask.ext.admin.base import AdminIndexView
from wtforms import fields, widgets
from werkzeug.security import generate_password_hash
from blogapp import app, db
from data_model import Tag, User, Category, Entry, Friend_link
from forms import *
from config import REGISTRATION_CODE
from flask.ext.admin.contrib.fileadmin import FileAdmin
import os.path as op


# Define wtforms widget and field
class CKTextAreaWidget(widgets.TextArea):

    def __call__(self, field, **kwargs):
        kwargs.setdefault('class_', 'ckeditor')
        return super(CKTextAreaWidget, self).__call__(field, **kwargs)


class CKTextAreaField(fields.TextField):
    widget = CKTextAreaWidget()


class EntryAdmin(ModelView):

    form_overrides = dict(content=CKTextAreaField)

    create_template = 'admin/create.html'
    edit_template = 'admin/edit.html'
    # Visible columns in the list view
    column_exclude_list = ['content', 'status', 'modified_time', 'author']
    # List of columns that can be sorted. For 'user' column, use User.username as
    column_sortable_list = ('category', 'create_time')
    # Rename 'title' columns to 'Post Title' in list view
    column_labels = dict(title='Entry Title')

    column_searchable_list = ('title', User.nickname)

    column_filters = ('title', 'create_time', 'category')

    def __init__(self, session):
        super(EntryAdmin, self).__init__(Entry, db.session)

    def is_accessible(self):
        return current_user.is_authenticated()

class UserAdmin(ModelView):
    column_exclude_list = ['password', 'Role']

    def __init__(self, session):
        super(UserAdmin, self).__init__(User, db.session)

    def is_accessible(self):
        return current_user.is_authenticated()

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
admin.add_view(EntryAdmin(db.session))
admin.add_view(UserAdmin(db.session))
admin.add_view(MyAdminView(Friend_link, db.session))

# file manage
path = op.join(op.dirname(__file__), 'static')
admin.add_view(FileAdmin(path, '/static/', name='Static Files'))
