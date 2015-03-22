import os
import sys
absolute_path = os.path.abspath(__file__)
app_path = os.path.dirname(absolute_path)
path = os.path.join(app_path, 'libs')
sys.path.insert(0, path)
sys.path.insert(0, app_path)

import sae
from blogapp import app, db
db.create_all()
application = sae.create_wsgi_app(app)

