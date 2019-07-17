#!/usr/bin/python3

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from rpos.models import Ingredient, MenuItem, Recipe, User

from rpos.db import db_session
from sqlalchemy.sql import select

bp = Blueprint('manager', __name__, url_prefix='/manager')

@bp.route('/db')
def db():
    print(User.__table__.columns)
    return User.query.all()[0].username


@bp.route('/')
def portal():
    return redirect(url_for('manager.portaltable', table='Menu'))


@bp.route('/<string:table>')
def portaltable(table):

    error = None
    tables = ['Menu', 'Ingredients', 'Recipes', 'Users']

    if table not in tables:
        error = "No table named " + table + " exists in the database."
        table = 'Menu'

    tabobj = {
        "Ingredients" : Ingredient,
        "Menu" : MenuItem,
        "Recipes" : Recipe,
        "Users" : User,
    }.get(table)

    fields = tabobj.__table__.columns.keys()

    types = ""

    contents = db_session.execute(select([tabobj.__table__]))

    if fields[0] == 'id':
        fields = fields[1:]
        contents = [i[1:] for i in contents]

    # if table == 'Ingredients':
    #     fields = ['Name', 'Price', 'Quantity']
    #     types = ['string', 'decimal']
    #     contents = [['Cheese', 3.00, 10],
    #                 ['Hamburger bun', 2.75, 20],
    #                 ['Hamburger patty', 4.25, 15]]
    # else:
    #     fields = ['Just', 'Some', 'Fields']
    #     types = ['string', 'decimal']
    #     contents = [['queso', 'is', 'good'],
    #                 ['chicken coop', 'swoop', 'di woop'],
    #                 ['bloop', 'no', 2390]]

    return render_template('manager/portal.html',
                            curtab=table,
                            tables=tables,
                            fields=beautify_arr(fields),
                            types=types,
                            contents=contents,
                            error=error)

def beautify(s):
    s = s.replace('_', ' ')
    return s[0].upper() + s[1:]

def beautify_arr(arr):
    for i in range(len(arr)):
        arr[i] = beautify(arr[i])
    return arr