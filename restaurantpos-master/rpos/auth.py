#!/usr/bin/python3

import functools
import bcrypt

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)

#!/usr/bin/python3

from rpos.models import User
from rpos.db import db_session

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/login', methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        print(username, " ", password)
        error = None
        users = [i for i in db_session.query(User).filter_by(username=username)]

        user = None
        if len(users) > 0:
            user = users[0]

        if user is None:
            error = 'Incorrect username.'
        elif not bcrypt.checkpw(password.encode(), user.password.encode()):
            error = 'Incorrect password.'

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('manager.portaltable', table='Menu'))

        flash(error)

    return render_template('auth/login.html')

@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        users = [i for i in db_session.query(User).filter_by(id=user_id)]
        if len(users) > 0:
            g.user = users[0]


@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@bp.route('/accessdenied')
def accessdenied():
    return render_template('auth/denied.html')

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view

def manager_login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if not g.user.isadmin:
            return redirect(url_for('auth.accessdenied'))

        return view(**kwargs)

    return wrapped_view