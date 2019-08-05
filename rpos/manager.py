#!/usr/bin/python3

import bcrypt, datetime

from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)

from rpos.models import Ingredient, MenuItem, Recipe, User
from rpos.db import db_session
from rpos.auth import login_required, manager_login_required
from rpos.utils import *

from sqlalchemy.sql import select

bp = Blueprint('manager', __name__, url_prefix='/manager')
tables = ['Menu', 'Ingredients', 'Recipes']

# prefilling fieldmap with table values
fieldmap = {'Menu description' : 'menu_description',
            'Ingredient description' : 'ingredient_description',
            'Ingredient quantity' : 'ingredient_quantity',
            'Show in menu?' : 'to_show',
            'Description': 'description',
            'Stock': 'stock',
            'Unit': 'unit',
            'Cost':'cost',
            'Price': 'price',
            'Category': 'category',
            'Low threshold': 'low_threshold'}

@bp.route('/')
def portal():
    return redirect(url_for('manager.portaltable', table='Menu'))

@bp.route('/<string:table>', methods=['GET', 'POST'])
@login_required
def portaltable(table):

    error = None
    ingunitmap = {}

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

                # strip request keys from singular words
                reqkeys = [i for i in request.form.keys()]
                reqkeys.remove('update')
                # generate rows, dict of id:['request key_1', 'request key_2', ...]
                idd = generate_rows(reqkeys)
                queries = sql_query_from_dict(table.lower(), idd, fieldmap, request.form)
                print(queries)
        else:
            pass

    types = [repr(i.type).split('(')[0].lower() for i in tab.c] # god i'm sorry for this ugly shit
    types = types[1:] # ignore the id type

    cont = db_session.execute(select([tab]))

    if fields[0] == 'id':
        fields = fields[1:]
        idarr = []
        contents = []
        for i in cont:
            idarr.append(i[0])
            contents.append(i[1:])

    # exclude the menu and ingredient ids
    if table == 'Recipes':
        sql = "select menu_description, ingredient_description, ingredient_quantity, to_show from recipes;"
        contents = [i for i in db_session.execute(sql)]
        fields = ['Menu description', 'Ingredient description', 'Ingredient quantity', 'Show in menu?']
        types = ['varchar', 'varchar', 'decimal', 'tinyint']
        # get ingredient:unit map
        ingunitmap = {i[0]:i[1] for i in db_session.execute("select description, unit from ingredients;")}
    

    catdrop = [i[0] for i in db_session.execute("select category from menu union select category from menu;")]
    unitdrop = [i[0] for i in db_session.execute("select unit from ingredients union select unit from ingredients;")]
    menudrop = [i[0] for i in db_session.execute("select description from menu;")]
    ingdrop = [i[0] for i in db_session.execute("select description from ingredients;")]

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
                            ingunitmap=ingunitmap,
                            error=error)

@bp.route('/Users')
@manager_login_required
def users():
    return redirect(url_for('manager.adduser'))

@bp.route('/AddUser', methods=['POST', 'GET'])
@manager_login_required
def adduser():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confpass = request.form['confpass']
        print(username, " ", password, " ", confpass)
        error = None
        users = [i[0] for i in db_session.execute("SELECT username FROM users;")]
        print(users)

        if username in users:
            error = "Username exists."
        elif password != confpass:
            error = "Passwords don't match."
        else:

            salt = bcrypt.gensalt()
            hashpass = bcrypt.hashpw(password.encode(), salt)
            print(hashpass)

            sql = "INSERT INTO users (username, password, isadmin) VALUES ('" + username + "', '" + hashpass.decode() + "', 0);"
            db_session.execute(sql)
            db_session.commit()

            error = "User successfully added."

        flash(error)
    
    return render_template('manager/adduser.html', tables=tables)

@bp.route('/DelUser', methods=['POST', 'GET'])
@manager_login_required
def deluser():

    if request.method == 'POST':
        if ('delete' in request.form.keys()):

                sql = "DELETE FROM " + User.__tablename__ + " WHERE id = "

                for k in request.form.keys():
                    if 'checkbox_' in k:
                        id = k[9:]
                        sql += id + " or id = "

                sql = sql[:-9] + ";"
                db_session.execute(sql)
                db_session.commit()

    sql = "SELECT * FROM users;"
    contents = [i[:2] for i in db_session.execute(sql)][1:] # the manager can never be deleted

    return render_template('manager/deluser.html', tables=tables,
                                                   contents=contents)

@bp.route('/lowthreshold')
@login_required
def lowthreshold():

    sql = "SELECT description, stock, unit, low_threshold FROM ingredients WHERE stock < low_threshold;"
    contents = [i for i in db_session.execute(sql)]

    return render_template('manager/lowthreshold.html', tables=tables, contents=contents)


@bp.route('/reports', methods=['POST', 'GET'])
@login_required
def reports():
    odict = {}
    total_ing_cost = 0
    total_income = 0
    mindt = [datetime.datetime.now(), datetime.datetime.now()]
    maxdt = [datetime.datetime.now(), datetime.datetime.now()]

    dt = [i[0] for i in db_session.execute("SELECT ordertime FROM orders;")]
    
    if len(dt) > 0:
        d, t = str(sorted(dt)[0]).split(' ')
        mindt = (d, t)
        d, t = str(sorted(dt)[-1]).split(' ')
        maxdt = (d, t)

    startdate = mindt[0]
    starttime = mindt[1]
    enddate = maxdt[0]
    endtime = maxdt[1]

    sql = "SELECT * FROM orders;"

    if request.method == 'POST':
        startdate = request.form['startdate']
        starttime = request.form['starttime']
        enddate = request.form['enddate']
        endtime = request.form['endtime']

        sql = "SELECT * FROM orders WHERE ordertime >= '" + startdate + ' ' + starttime + \
                                    "' and ordertime <= '" + enddate + ' ' + endtime + "';"

    orders = [i for i in db_session.execute(sql)]

    for i in orders:
        _, otime, oid, gname, menuid, ingid, quantity, _ = i
        if oid not in odict.keys():
            odict[oid] = {'otime': otime,
                            'gname': gname,
                            'menuitems': {},
                            'ingredients': [],
                            'ototal': 0,
                            'ingcost': 0}
        
        if menuid not in odict[oid]['menuitems'].keys():
            mdesc, mcost = [i for i in db_session.execute("select description, price from menu where id=" + str(menuid) + ";")][0]
            odict[oid]['menuitems'][menuid] = mdesc
            odict[oid]['ototal'] += mcost
            total_income += mcost

        idesc, icost = [i for i in db_session.execute("select description, cost from ingredients where id=" + str(ingid) + ";")][0]
        odict[oid]['ingredients'].append(idesc + " (" + str(quantity) + ")")
        item_ing_cost = (icost * quantity)
        odict[oid]['ingcost'] += item_ing_cost
        total_ing_cost += item_ing_cost

    return render_template('manager/reports.html', 
                                    tables=tables, 
                                    mindt=mindt, 
                                    maxdt=maxdt,
                                    startdate=startdate,
                                    starttime=starttime,
                                    enddate=enddate,
                                    endtime=endtime,
                                    orders=odict,
                                    total_ing_cost=total_ing_cost,
                                    total_income=total_income)
