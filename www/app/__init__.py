from flask import Flask
from flask_cors import CORS
from app import config

app = Flask(__name__)
CORS(app)
app.config.from_object(config)

from app.admin import admin as admin_mode
app.register_blueprint(admin_mode,url_prefix='/TopGus/Data')

from app.views import *



