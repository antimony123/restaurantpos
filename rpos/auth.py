from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from rpos.models import User

from rpos.db import db_session

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/test')
def test():
    return 'Auth test successful!'

@bp.route('/login')
def login():
    return render_template('manager/login.html')