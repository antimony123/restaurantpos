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


@bp.route('/<string:table>', methods=['GET', 'POST'])
def portaltable(table):

    error = None
    tables = ['Menu', 'Ingredients', 'Recipes']

    if table not in tables:
        error = "No table named " + table + " exists in the database."
        table = 'Menu'
        redirect(url_for('manager.portaltable', table='Menu'))

    tabobj = {      # the object representing both the table and the type of object the table stores
        "Ingredients" : Ingredient,
        "Menu" : MenuItem,
        "Recipes" : Recipe,
    }.get(table)

    tab = tabobj.__table__      # the actual table part of the declarative object

    fields = tab.columns.keys()

    if request.method == 'POST':

        # add row
        if ('add' in request.form.keys()
            and 'update' not in request.form.keys()
            and 'delete' not in request.form.keys()):

                new_item = tabobj()
                db_session.add(new_item)
                db_session.commit()
                redirect(url_for('manager.portaltable', table=table))

        # delete selected items
        elif ('delete' in request.form.keys()
            and 'add' not in request.form.keys()
            and 'update' not in request.form.keys()):

                sql = "DELETE FROM " + tabobj.__tablename__ + " WHERE id = "

                for k in request.form.keys():
                    if 'checkbox_' in k:
                        id = k[9:]
                        sql += id + " or id = "

                sql = sql[:-9] + ";"
                db_session.execute(sql)
                db_session.commit()

        # update
        elif ('update' in request.form.keys()
            and 'add' not in request.form.keys()
            and 'delete' not in request.form.keys()):

                print('updated db')
        else:
            pass

    types = [repr(i.type).split('(')[0].lower() for i in tab.c] # god i'm sorry for this ugly shit
    types = types[1:] # ignore the id type
    print(types)

    cont = db_session.execute(select([tab]))

    if fields[0] == 'id':
        fields = fields[1:]
        idarr = []
        contents = []
        for i in cont:
            idarr.append(i[0])
            contents.append(i[1:])

    catdrop = [i for i in db_session.execute("select category from menu union select category from menu;")]
    unitdrop = [i for i in db_session.execute("select unit from ingredients union select unit from ingredients;")]
    menudrop = [i for i in db_session.execute("select description from menu;")]
    ingdrop = [i for i in db_session.execute("select description from ingredients;")]

    return render_template('manager/portal.html',
                            curtab=table,
                            tables=tables,
                            idarr=idarr,
                            fields=beautify_arr(fields),
                            types=types,
                            contents=contents,
                            catdrop=catdrop,
                            unitdrop=unitdrop,
                            menudrop=menudrop,
                            ingdrop=ingdrop,
                            error=error)

@bp.route('/Users')
def users():
    return "Users editing"


def beautify(s):
    s = s.replace('_', ' ')
    return s[0].upper() + s[1:]

def beautify_arr(arr):
    for i in range(len(arr)):
        arr[i] = beautify(arr[i])
    return arr