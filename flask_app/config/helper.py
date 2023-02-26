from functools import wraps
from flask import request, redirect, url_for, session

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('landing'))
        return f(*args, **kwargs)
    return decorated_function

def parent_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('landing'))
        elif session['user']['level'] < 2:
            return redirect(url_for('kiddos_dashboard'))
        return f(*args, **kwargs)
    return decorated_function

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            return redirect(url_for('landing'))
        elif session['user']['level'] < 2:
            return redirect(url_for('kiddos_dashboard'))
        elif session['user']['level'] < 3:
            return redirect(url_for('parents_dashboard'))
        return f(*args, **kwargs)
    return decorated_function

def page_logger(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        current_page = request.path
        if 'page_logger' not in session:
            session['page_logger'] = [current_page]
        else:
            pages = session['page_logger']
            if (pages[-1] != current_page):
                pages.append(current_page)
                session['page_logger'] = pages
        return f(*args, **kwargs)
    return decorated_function

def get_last_page():
    if 'page_logger' in session:
        return session['page_looger'].pop()
    return False