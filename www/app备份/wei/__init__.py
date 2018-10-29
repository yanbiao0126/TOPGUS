from flask import Blueprint

wei = Blueprint('wei',__name__)

from app.wei import views
