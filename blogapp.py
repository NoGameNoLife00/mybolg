 #encoding=utf-8

import os
import sys
absolute_path = os.path.abspath(__file__)
app_path = os.path.dirname(absolute_path)
path = os.path.join(app_path, 'libs')
sys.path.insert(0, path)
sys.path.insert(0, app_path)


from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
# from flask.ext.login import LoginManager
# from flask.ext.openid import OpenID
# from config import basedir



app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
from admin import *

#Login
# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'login'
# oid = OpenID(app, os.path.join(basedir, 'tmp'))

#邮件系统
from config import ADMINS, MAIL_PASSWORD, MAIL_PORT, MAIL_SERVER, MAIL_USERNAME

# if not app.debug:
#     import logging
#     from logging.handlers import SMTPHandler
#     credentials = None
#     if MAIL_USERNAME or MAIL_PASSWORD:
#         credentials = (MAIL_USERNAME, MAIL_PASSWORD)
#     mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT),
#                                'no-reply@' + MAIL_SERVER, ADMINS, 'blog failure', credentials)
#     mail_handler.setLevel(logging.ERROR)
#     app.logger.addHandler(mail_handler)

# from flask.ext.mail import Mail
# mail = Mail(app)

#日志
# if not app.debug:
#     import logging
#     from logging.handlers import  RotatingFileHandler
#     file_handler = RotatingFileHandler('tmp/blog.log', 'a', 1*1024*1024, 10)
#     file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
#     app.logger.setLevel(logging.INFO)
#     app.logger.addHandler(file_handler)
#     app.logger.info('blog startup')


from view import *


if  __name__ == '__main__':
    app.run(host='0.0.0.0', port=5005)