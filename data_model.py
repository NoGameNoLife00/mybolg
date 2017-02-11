 #encoding=utf-8
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import UserMixin
from blogapp import db
from hashlib import md5
from flask import Markup
import markdown
import bleach
import config



ROLE_ADMIN = 1
ROLE_USER = 2

CONTENT_FORMAT = 'html'
if config.ARTICLE_EDITOR == "simplemde":
    CONTENT_FORMAT = 'markdown'


# markdown 转换为 html
def md2html(text, codehilte=False):
    exts = [
        'abbr', 'attr_list', 'def_list', 'sane_lists', 'fenced_code',
        'tables', 'toc', 'wikilinks'
    ]
    if codehilte:
        exts.append('codehilite(guess_lang=True,linenums=False)')

    result_text = Markup(markdown.markdown(
        text,
        extensions=exts,
        safe_mode=False,
    ))
    return result_text


# 用户
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(80), unique=True)
    nickname = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_ADMIN)
    entry = db.relationship('Entry', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(250))
    last_seen = db.Column(db.DateTime)


    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def get_id(self):
        return unicode(self.id)


    # #防止昵称相同
    # @staticmethod
    # def make_unique_nickname(nickname):
    #     if User.query.filter_by(nickname=nickname).first() == None:
    #         return nickname
    #     virsion = 2
    #     while True:
    #         new_nickname = nickname + str(virsion)
    #         if User.query.filter_by(nickname=new_nickname).first() == None:
    #             break
    #         virsion += 1
    #     return new_nickname

    def __repr__(self):
        return '<User %r>' % self.nickname

    def __unicode__(self):
        return self.nickname


# 分类
class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __repr__(self):
        return '<Category %r>' % self.name

    def __unicode__(self):
        return self.name


# 标签
class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __repr__(self):
        return '<Tag %r>' % self.name

tag_entry = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                db.Column('entry_id', db.Integer, db.ForeignKey('entry.id'))
                )


# 文章
class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    content_html = db.Column(db.Text)
    fragment = db.Column(db.Text) #内容片段, 用于主页显示
    status = db.Column(db.Integer, default=1) #完成：1, 失败0, 草稿:-1  （暂时无用）
    create_time = db.Column(db.DateTime, index=True, default=datetime.now())
    modified_time = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category = db.relationship('Category', backref=db.backref('entries', lazy='dynamic'), lazy='select')
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    tag = db.relationship('Tag', secondary=tag_entry, backref=db.backref('entries', lazy='dynamic'))
    view_count = db.Column(db.Integer, default=0)

    @staticmethod
    def on_changed_content(target, value, oldvalue, initator):
        if CONTENT_FORMAT == 'html':
            target.content_html = value
        else:
            target.content_html = md2html(text=value)

    def __repr__(self):
        return '<Entry %r>' % self.title

    def __unicode__(self):
        return self.title

db.event.listen(Entry.content, 'set', Entry.on_changed_content)


# 友链
class Friend_link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    link = db.Column(db.String(120))
    def __repr__(self):
        return '<Friend link %r>' % self.name

    def __unicode__(self):
        return self.name


if __name__ == '__main__':
    db.create_all()