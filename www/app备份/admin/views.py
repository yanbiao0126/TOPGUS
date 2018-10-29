from app.admin import admin
from flask import render_template,url_for


@admin.route('/')
def index():
    return render_template('admin/index.html')

@admin.route('/chart')
def chart():
    return render_template('admin/chart.html')

@admin.route('/login')
def login():
    return render_template('admin/login.html')
