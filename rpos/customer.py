from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)

from rpos.models import Ingredient, MenuItem, Recipe, Order

from rpos.db import db_session

import mysql.connector as mysql

import string, random, os
bp = Blueprint('customer', __name__, url_prefix='/customer')
bp.secret_key = os.urandom(24)

def randomString(stringLength=20):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))

@bp.route('/firststep')
def firststep():
    orderid = randomString()
    return render_template('/customer/cusportal.html', orderid=orderid)

@bp.route('/displaymenu', methods=["POST", "GET"])
def displaymenu():
    if request.method == "POST" :
        session['guestname'] = request.form['guestname']
        session['orderid'] = request.form['orderid']

        cnx = mysql.connect(user='root', password='putpwhere', host='127.0.0.1', database='RESMGTDB')
        cur = cnx.cursor()

        cur.execute("SELECT * from menu WHERE category='Food'")
        food_table = [row for row in cur]

        cur.execute("SELECT * from menu WHERE category='Side'")
        side_table = [row for row in cur]

        cur.execute("SELECT * from menu WHERE category='Drink'")
        drink_table = [row for row in cur]

    return render_template('/customer/displaymenu.html', food_table=food_table, side_table=side_table, drink_table=drink_table)

@bp.route('/customizeorder', methods=["POST", "GET"])
def customizeorder():
    if request.method == "POST" :
        session['mainorder'] = request.form['mainorder']
        session['sideorder'] = request.form['sideorder']
        session['drinkorder'] = request.form['drinkorder']

        cnx = mysql.connect(user='root', password='putpwhere', host='127.0.0.1', database='RESMGTDB')
        cur = cnx.cursor()

        #query = "select * FROM menu WHERE id = %s "
        #args = session['mainorder']
        #cur.execute(query, args)
        cur.execute("select * FROM menu WHERE id = " + session['mainorder'])
        maindish = cur.fetchone()[1]

        #query = "select * FROM recipes WHERE menu_id = '%s' AND to_show = 1"
        #args = session['mainorder']
        #cur.execute(query, args)
        #detailorder = [(r[3], r[4]) for r in cur]
        cur.execute("select * FROM recipes WHERE menu_id = " + session['mainorder'] + " AND to_show = 1")
        detailorder = [(r[3], r[4]) for r in cur]

        #query = "SELECT * from menu WHERE id = '%s'"
        #args = session['sideorder']
        #cur.execute(query, args)
        cur.execute("SELECT * from menu WHERE id = " + session['sideorder'])
        sidedish = cur.fetchone()[1]

        #query = "SELECT * from menu WHERE id = '%s'"
        #args = session['drinkorder']
        #cur.execute(query, args)
        #drink = [r[1] for r in cur]
        cur.execute("SELECT * from menu WHERE id = " + session['drinkorder'])
        drink = cur.fetchone()[1]

    return render_template("/customer/customizeorder.html", orderid=session['orderid'], \
        guestname=session['guestname'], maindish=maindish, detailorder=detailorder, \
        sidedish=sidedish, drink=drink)
