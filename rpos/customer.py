from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from rpos.models import Ingredient, MenuItem, Recipe, Order

from rpos.db import db_session

bp = Blueprint('customer', __name__, url_prefix='/customer')

@bp.route('/test')
def test():
    return 'Customer test successful!'