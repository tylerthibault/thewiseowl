from flask_app import app
from flask_app.config.helper import login_required, admin_required, page_logger, parent_required, get_last_page
from flask import render_template, redirect, session, request


@app.route('/')
@page_logger
def index():
    return render_template('/pages/index.html')

@app.route('/dashboard')
@page_logger
@parent_required
def dashboard():
    return render_template('/pages/dashboard.html')
