 #encoding=utf-8
"""
用户登录表单
"""
from flask.ext.wtf import Form
from wtforms.fields import TextField, BooleanField, TextAreaField
from wtforms.validators import Required, Length
from data_model import User
class LoginForm(Form):
    openid = TextField('openid', validators = [Required()])
    remember_me = BooleanField('remember', default=False)

class EditForm(Form):
    nickname = TextField('nickname', validators=[Required()])
    about_me = TextAreaField('about_me', validators=[Length(min=0, max=250)])

    def __init__(self, original_nickname, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.original_nickname = original_nickname

    def validate(self):
        if not Form.validate(self):
            return False
        if self.nickname.data == self.original_nickname:
            return True
        user = User.query.filter_by(nickname=self.nickname.data).first()
        if user != None:
            self.nickname.errors.append('This nickname is already in use. Please choose another one.')
            return False
        return True



