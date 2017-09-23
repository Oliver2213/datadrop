# Datadrop - the tiney pastebin for hackers
# Author: Blake Oliver <oliver22213@me.com>

from flask import Flask
from sqlservice import SQLClient

from models import Base
import utils

app = Flask(__name__)

# configure the app
app.config.from_object('app.default_config')
app.config.from_pyfile('app.config', silent=True)

db = SQLClient(config=utils.get_config_items_with_prefix(app.config, 'SQL'), model_class=Model)
