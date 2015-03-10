 #encoding=utf-8
"""
用户登录表单
"""
from flask.ext.wtf import Form
from wtforms.fields import TextField, BooleanField, TextAreaField, PasswordField
from wtforms.validators import required, Required, Length, DataRequired, ValidationError
from werkzeug.security import generate_password_hash, check_password_hash
from blogapp import app, db
from data_model import User
from flask.ext.login import LoginManager
from config import REGISTRATION_CODE

# Define login and registration forms (for flask-login)
class LoginForm(Form):
    login = TextField(validators=[required()])
    password = PasswordField(validators=[required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise ValidationError('Invalid user')

        # we're comparing the plaintext pw with the the hash from the db
        # if not check_password_hash(user.password, self.password.data):
        # to compare plain text passwords use
        if user.password != self.password.data:
            raise ValidationError('Invalid password')

    def get_user(self):
        return db.session.query(User).filter_by(login=self.login.data).first()


class RegistrationForm(Form):
    login = TextField(validators=[required()])
    nickname = TextField()
    email = TextField()
    password = PasswordField(validators=[required()])
    registration_code = PasswordField(validators=[required()])

    def validate_login(self, field):

        if self.registration_code.data != REGISTRATION_CODE:
            raise ValidationError('Invalid Registration')

        if db.session.query(User).filter_by(login=self.login.data).count() > 0:
            raise ValidationError('Duplicate username')


def init_login():
    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.query(User).get(user_id)



# class EditForm(Form):
#     nickname = TextField('nickname', validators=[Required()])
#     about_me = TextAreaField('about_me', validators=[Length(min=0, max=250)])
#
#     def __init__(self, original_nickname, *args, **kwargs):
#         Form.__init__(self, *args, **kwargs)
#         self.original_nickname = original_nickname
#
#     def validate(self):
#         if not Form.validate(self):
#             return False
#         if self.nickname.data == self.original_nickname:
#             return True
#         user = User.query.filter_by(nickname=self.nickname.data).first()
#         if user != None:
#             self.nickname.errors.append('This nickname is already in use. Please choose another one.')
#             return False
#         return True
#


