#coding=utf-8
from datetime import datetime
from flask.ext.sqlalchemy import SQLAlchemy
from blogapp import app
from hashlib import md5

db = SQLAlchemy(app)

ROLE_ADMIN = 1
ROLE_USER = 2


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(80), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    role = db.Column(db.SmallInteger, default=ROLE_USER)
    entries = db.relationship('Entries', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(250))
    last_seen = db.Column(db.DateTime)


    def is_authenticated(self):
    #   是否通过认证
        return True

    def is_active(self):
    #   是否有效
        return True
    def is_anonymous(self):
    #   是否匿名
        return False

    def avatar(self, size):
    #   用户头像
        return 'http://www.gravatar.com/avatar/' + \
               md5(self.email).hexdigest() + '?d=mm&s=' + str(size)


    def get_id(self):
        return unicode(self.id)


    #防止昵称相同
    @staticmethod
    def make_unique_nickname(nickname):
        if User.query.filter_by(nickname=nickname).first() == None:
            return nickname
        virsion = 2
        while True:
            new_nickname = nickname + str(virsion)
            if User.query.filter_by(nickname=new_nickname).first() == None:
                break
            virsion += 1
        return new_nickname


    def __repr__(self):
        return '<User %r>' % self.nickname

    def __unicode__(self):
        return self.nickname


class Entries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    status = db.Column(db.Integer) #完成：1, 失败0, 草稿:-1
    create_time = db.Column(db.DateTime)
    modified_time = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Entries %r>' % self.title

    def __unicode__(self):
        return self.title


if __name__ == '__main__':
    db.create_all()