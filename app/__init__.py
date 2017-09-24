# Datadrop - the tiney pastebin for hackers
# Author: Blake Oliver <oliver22213@me.com>

from flask import Flask
#from sqlservice import SQLClient
from utils import FlaskSQLService
from flask_moment import Moment

import utils

app = Flask(__name__)

# configure the app
app.config.from_object('app.default_config')
app.config.from_pyfile('config.py', silent=True)

from models import Model
db = FlaskSQLService(app=app, model_class=Model)
#db = SQLClient(config=utils.get_config_items_with_prefix(app.config, 'SQL'), model_class=Model)
moment = Moment(app)

import views