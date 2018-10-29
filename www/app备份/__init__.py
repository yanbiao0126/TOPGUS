from flask import Flask
from app import config

app = Flask(__name__)

app.config.from_object(config)

from app.home import home as home_mode
app.register_blueprint(home_mode)
from app.wei import wei as wei_mode
app.register_blueprint(wei_mode,url_prefix='/wei')
