#coding=utf-8

from flask import render_template, flash, redirect, session, url_for, request, g
# from flask.ext.login import login_user, logout_user, current_user, login_required
from data_wrappers import DataWrappers
from data_model import *
from blogapp import app #lm, oid
# from forms import LoginForm, EditForm
from config import POST_PRE_PAGE
date = DataWrappers()


@app.before_request
def befor_request():
    pass


@app.route('/')
@app.route('/blog')
@app.route('/blog/<int:page>')
def show_blog(page=1):
    if page < 1:
        page = 1
    p = date.get_entries_by_page(page=page, par_page=POST_PRE_PAGE)
    entries = p.items
    #页数标签
    if not p.total:
        pagination = [0]
    elif p.total % POST_PRE_PAGE != 0:
        pagination = range(1, p.total/POST_PRE_PAGE + 2)
    else:
        pagination = range(1, p.total/POST_PRE_PAGE + 1)

    return render_template('/blog/show_blog.html', entries=entries,
                           p=p, page=page, pagination=pagination)


#表单视图
# @app.route('/login', methods = ['GET', 'POST'])
# @oid.loginhandler
# def login():
#     if g.user is not None and g.user.is_authenticated():
#         return redirect(url_for('blog'))
#     form = LoginForm()
#     if form.validate_on_submit():
#         session['remeber_me'] = form.remember_me.data
#         return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
#
#     return render_template('/blog/login.html', title='Sign In',
#                            form=form, providers=app.config['OPENID_PROVIDERS'])
#
# @app.route('/logout')
# def logout():
#     logout_user()
#     return redirect(url_for('show_blog'))
#
#
# @lm.user_loader
# def load_user(id):
#     return User.query.get(int(id))
#
# @oid.after_login
# def after_login(resp):
#     if resp.email is None or resp.email == "":
#         flash('Invalid login. Please try again!')
#         return redirect(url_for('login'))
#     user = User.query.filter_by(email=resp.email).first()
#     if user is None:
#         nickname = resp.nickname
#         if nickname is None or nickname == "":
#             nickname = resp.email.split('@')[0]
#         user = User(nickname=nickname, email=resp.email, role=ROLE_USER)
#         db.session.add(user)
#         db.session.commit()
#     remember_me = False
#     if 'remember_me' in session:
#         remember_me = session['remember_me']
#         session.pop('remember_me', None)
#     login_user(user, remember=remember_me)
#     return redirect(request.args.get('next') or url_for('show_blog'))
#用户信息
# @app.route('/user/<nickname>')
# @login_required
# def user(nickname):
#     user = User.query.filter_by(nickname=nickname).first()
#     if user == None:
#         flash('user'+nickname+'not found')
#         return redirect(url_for('show_blog'))
#     entries = [
#         {'author': user, 'content': 'Test post #1'},
#         {'author': user, 'content': 'Test post #2'}
#     ]
#     return render_template('/blog/user.html', user=user, entries=entries)
#
# @app.route('/edit', methods=['GET', 'POST'])
# @login_required
# def edit():
#     form = EditForm(g.user.nickname)
#     if form.validate_on_submit():
#         g.user.nickname = form.nickname.data
#         g.user.about_me = form.about_me.data
#         db.session.add(g.user)
#         db.session.commit()
#         flash('Your changes have been saved.')
#         return redirect(url_for('edit'))
#     else:
#         form.nickname.data = g.user.nickname
#         form.about_me.data = g.user.about_me
#     return render_template('/blog/edit.html', form=form)

#错误处理
@app.errorhandler(404)
def internal_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    return render_template('500.html'), 500


#管理视图
@app.route('/admin')
def admin_index():
    return '<a href="/admin/"> Click me to get to Admin!</a>'


