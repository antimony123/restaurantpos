from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)

# from rpos.models import Ingredient, MenuItem, Recipe, Order

# from rpos.db import db_session

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

        cnx = mysql.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
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

        cnx = mysql.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
        cur = cnx.cursor()

        cur.execute("select * FROM menu WHERE id = " + session['mainorder'])
        maindish = cur.fetchone()[1]

        cur.execute("select * FROM recipes WHERE menu_id = " + session['mainorder'] + " AND to_show = 1")
        detailorder = [(r[3], r[4]) for r in cur]

        cur.execute("SELECT * from menu WHERE id = " + session['sideorder'])
        sidedish = cur.fetchone()[1]

        cur.execute("SELECT * from menu WHERE id = " + session['drinkorder'])
        drink = cur.fetchone()[1]

    return render_template("/customer/customizeorder.html", orderid=session['orderid'], \
        guestname=session['guestname'], maindish=maindish, detailorder=detailorder, \
        sidedish=sidedish, drink=drink)

@bp.route('/reviewpayorder', methods=["POST", "GET"])
def reviewpayorder():
    if request.method == "POST" :
        # keys = [key for key in request.form.keys()]
        # for key in keys :
        #     print(key)

        cnx1 = mysql.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
        cnx2 = mysql.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
        cur1 = cnx1.cursor()
        cur2 = cnx2.cursor()

        # ---Present Main Order --------------------------------------------------------------
        query = "SELECT * from menu WHERE id = %s "
        args = (session['mainorder'])
        cur1.execute(query, args)
        main_order_tuple = [(r[1], r[2]) for r in cur1]

        #---Present Main Order Details --------------------------------------------------------

#     for detail in details:
#         query = "SELECT * from recipes WHERE ingredient_id = %s AND menu_id = %s"
#         input_tuple = (detail, mainorder)
#         cur1.execute(query,input_tuple)
#         for r in cur1:
#             print("<tr><td>-->",r[4],"</td></tr>")
#             query = "INSERT INTO orders (orderid, guestname, mainorder, detail, quantity ) VALUES (%s,%s,%s,%s,%s)"
#             args = (orderid, guestname,mainorder,detail,r[5])
#             cur2.execute(query,args)
#             cnx2.commit()

# #---Enter into Orders the hidden items  ----------------------------------------------

#     query = "SELECT * from recipes WHERE menu_id = %s AND to_show = 0"
#     args = (mainorder)
#     cur1.execute(query,(args,))
#     for r in cur1:
#         query = "INSERT INTO orders (orderid, guestname, mainorder, detail, quantity ) VALUES (%s,%s,%s,%s,%s)"
#         args = (orderid, guestname,mainorder,r[3],r[5])
#         cur2.execute(query,args)
#         cnx2.commit()

# #---Present Side Order --------------------------------------------------------------

#     query = "SELECT * from menu WHERE id = %s "
#     args = (sideorder)
#     cur1.execute(query,(args,))
#     for r in cur1:
#        print("<tr><td>",r[1],"</td><td>",r[2],"</td></tr>")

#     totalorder = totalorder + float(r[2])

# #---------Enter Side Order into Orders

#     query = "SELECT * from recipes WHERE menu_id = %s "
#     args = (sideorder)
#     cur1.execute(query,(args,))
#     for r in cur1:
#       query = "INSERT INTO orders (orderid, guestname, mainorder, detail, quantity ) VALUES (%s,%s,%s,%s,%s)"
#       args = (orderid, guestname,sideorder,r[3],r[5])
#       cur2.execute(query,args)
#       cnx2.commit()

# #---Present Drink order -------------------------------------------------------------

#     query = "SELECT * from menu WHERE id = %s "
#     args = (drinkorder)
#     cur1.execute(query,(args,))
#     for r in cur1:
#        print("<tr><td>",r[1],"</td><td>",r[2],"</td></tr>")
#     totalorder = totalorder + float(r[2])

# #---------Enter Drink order into Orders --------------------------------------------

#     query = "SELECT * from recipes WHERE menu_id = %s "
#     args = (drinkorder)
#     cur1.execute(query,(args,))
#     for r in cur1:
#        query = "INSERT INTO orders (orderid, guestname, mainorder, detail, quantity ) VALUES (%s,%s,%s,%s,%s)"
#        args = (orderid, guestname,drinkorder,r[3],r[5])
#        cur2.execute(query,args)
#        cnx2.commit()

#     totalorder = totalorder + float(r[2])

    return render_template("/customer/reviewpayorder.html", guestname=session["guestname"], orderid=session["orderid"], \
        mainorder=session["mainorder"], sideorder=session["sideorder"], drinkorder=session["drinkorder"])
