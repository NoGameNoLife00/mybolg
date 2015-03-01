 #encoding=utf-8
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
    entry = db.relationship('Entry', backref='author', lazy='dynamic')
    about_me = db.Column(db.String(250))
    last_seen = db.Column(db.DateTime)

    #
    # def is_authenticated(self):
    # #   是否通过认证
    #     return True

    def is_active(self):
    #   是否有效
        return True
    # def is_anonymous(self):
    # #   是否匿名
    #     return False

    # def avatar(self, size):
    # #   用户头像
    #     return 'http://www.gravatar.com/avatar/' + \
    #            md5(self.email).hexdigest() + '?d=mm&s=' + str(size)


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


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __repr__(self):
        return '<Category %r>' % self.name

    def __unicode__(self):
        return self.name


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True)

    def __repr__(self):
        return '<Tag %r>' % self.name

tags = db.Table('tags',
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id')),
                db.Column('entry_id', db.Integer, db.ForeignKey('entry.id'))
                )


class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    status = db.Column(db.Integer, default=1) #完成：1, 失败0, 草稿:-1
    create_time = db.Column(db.DateTime, default=datetime.now())
    modified_time = db.Column(db.DateTime, default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    category = db.relationship('Category', backref=db.backref('entries', lazy='dynamic'), lazy='select')
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    tag = db.relationship('Tag', secondary=tags, backref=db.backref('entries', lazy='dynamic'))
    view_count = db.Column(db.Integer, default=0)

    def __repr__(self):
        return '<Entry %r>' % self.title

    def __unicode__(self):
        return self.title


if __name__ == '__main__':
    db.create_all()