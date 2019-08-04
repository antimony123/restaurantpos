from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for, session
)

# from rpos.models import Ingredient, MenuItem, Recipe, Order

# from rpos.db import db_session

import mysql.connector as mysql

import string, random, os, time

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

        query = "SELECT description FROM menu WHERE id = %s"
        cur.execute(query, (session['mainorder'],))
        maindish = cur.fetchone()[0]

        query = "SELECT ingredient_id, ingredient_description FROM recipes WHERE menu_id = %s AND to_show = 1"
        cur.execute(query, (session['mainorder'],))
        detailorder = [(r[0], r[1]) for r in cur]
        session['detailorder'] = detailorder

        query = "SELECT description FROM menu WHERE id = %s"
        cur.execute(query, (session['sideorder'],))
        sidedish = cur.fetchone()[0]

        query = "SELECT description FROM menu WHERE id = %s"
        cur.execute(query, (session['drinkorder'],))
        drink = cur.fetchone()[0]

    return render_template("/customer/customizeorder.html", orderid=session['orderid'], \
        guestname=session['guestname'], maindish=maindish, detailorder=detailorder, \
        sidedish=sidedish, drink=drink)

@bp.route('/reviewpayorder', methods=["POST", "GET"])
def reviewpayorder():
    if request.method == "POST" :
        detail_ids = [key for key in request.form.keys()]

        cnx1 = mysql.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
        cnx2 = mysql.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
        cur1 = cnx1.cursor()
        cur2 = cnx2.cursor()

        totalorder = 0.00

        # ---Present Main Order --------------------------------------------------------------
        query = "SELECT description, price from menu WHERE id = %s "
        cur1.execute(query, (session['mainorder'],))
        row = cur1.fetchone()
        main_order_tuple = (row[0], row[1])                     # send to template

        totalorder += float(main_order_tuple[1])

        #---Present Main Order Details --------------------------------------------------------

        detail_list = []                                        # send to template

        for detail in detail_ids :
            query = "SELECT ingredient_description, ingredient_quantity FROM recipes WHERE ingredient_id = %s AND menu_id = %s"
            input_tuple = (detail, session['mainorder'])
            cur1.execute(query, input_tuple)

            for r in cur1 :
                detail_list.append(r[0])

                query = "INSERT INTO orders (ordertime, orderid, guestname, mainorder, detail, quantity) VALUES (%s, %s, %s, %s, %s, %s)"
                args = (time.strftime('%Y-%m-%d %H:%M:%S'), session['orderid'], session['guestname'], session['mainorder'], detail, r[1],)
                cur2.execute(query, args)
                cnx2.commit()

        #---Enter into Orders the hidden items  ----------------------------------------------

        query = "SELECT ingredient_id, ingredient_quantity from recipes WHERE menu_id = %s AND to_show = 0"
        args = (session['mainorder'])
        cur1.execute(query, (args,))
        for r in cur1:
            query = "INSERT INTO orders (ordertime, orderid, guestname, mainorder, detail, quantity) VALUES (%s, %s, %s, %s, %s, %s)"
            args = (time.strftime('%Y-%m-%d %H:%M:%S'), session['orderid'], session['guestname'], session['mainorder'], r[0], r[1],)
            cur2.execute(query,args)
            cnx2.commit()

        #---Present Side Order --------------------------------------------------------------
        
        query = "SELECT description, price from menu WHERE id = %s "
        args = (session['sideorder'])
        cur1.execute(query,(args,))
        side_tuples = []                                # send to templates

        for r in cur1:
            side_tuples.append((r[0], r[1]))
            totalorder = totalorder + float(r[1])

        #---------Enter Side Order into Orders

        query = "SELECT ingredient_id, ingredient_quantity from recipes WHERE menu_id = %s "
        args = (session['sideorder'])
        cur1.execute(query,(args,))
        for r in cur1:
            query = "INSERT INTO orders (ordertime, orderid, guestname, mainorder, detail, quantity ) VALUES (%s, %s, %s, %s, %s, %s)"
            args = (time.strftime('%Y-%m-%d %H:%M:%S'), session['orderid'], session['guestname'], session['sideorder'], r[0], r[1],)
            cur2.execute(query, args)
            cnx2.commit()

        #---Present Drink order -------------------------------------------------------------

        query = "SELECT description, price from menu WHERE id = %s "
        args = (session['drinkorder'])
        cur1.execute(query,(args,))
        drink_tuples = []                               # send to template

        for r in cur1:
            drink_tuples.append((r[0], r[1]))
            totalorder = totalorder + float(r[1])

        #---------Enter Drink order into Orders --------------------------------------------

        query = "SELECT ingredient_id, ingredient_quantity from recipes WHERE menu_id = %s "
        args = (session['drinkorder'])
        cur1.execute(query,(args,))
        for r in cur1:
            query = "INSERT INTO orders (ordertime, orderid, guestname, mainorder, detail, quantity ) VALUES (%s, %s, %s, %s, %s, %s)"
            args = (time.strftime('%Y-%m-%d %H:%M:%S'), session['orderid'], session['guestname'], session['drinkorder'], r[0], r[1],)
            cur2.execute(query,args)
            cnx2.commit()

        session['main_order_tuple'] = main_order_tuple
        session['detail_list'] = detail_list
        session['side_tuples'] = side_tuples
        session['drink_tuples'] = drink_tuples
        session['totalorder'] = totalorder

    return render_template("/customer/reviewpayorder.html", guestname=session["guestname"], orderid=session["orderid"], \
        main_order_tuple=main_order_tuple, detail_list=detail_list, side_tuples=side_tuples, drink_tuples=drink_tuples, \
        totalorder=totalorder)

@bp.route('/acceptorder', methods=["POST", "GET"])
def acceptorder() :
    if request.method == "POST" :
        cnx1 = mysql.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
        cnx2 = mysql.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
        cnx3 = mysql.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
        cur1 = cnx1.cursor()
        cur2 = cnx2.cursor()
        cur3 = cnx3.cursor()

        #---Activate Order --------------------------------------------------

        query = "SELECT id from orders WHERE orderid = %s AND guestname = %s AND active = 0"
        args = (session['orderid'], session['guestname'])
        cur1.execute(query, args)
        for r in cur1:
            query = "UPDATE orders SET active = %s where id = %s"
            args = (1, r[0],)
            cur2.execute(query, args)
            cnx2.commit()

        #---Subtract order from Inventory -----------------------------------

        query = "SELECT detail, quantity from orders WHERE orderid = %s AND guestname = %s"
        args = (session['orderid'], session['guestname'])
        cur1.execute(query, args)
        for r in cur1:
            queryin = "SELECT id, stock from ingredients WHERE id = %s"
            args = r[0]
            cur2.execute(queryin, (args,))
            for qua in cur2:
                newstock = qua[1] - r[1]
#                print(newstock)
                query = "UPDATE ingredients SET stock = %s where id = %s"
                args = (newstock,qua[0])
                cur3.execute(query,args)
                cnx3.commit()

        #---Retrieve timestamp-----------------------------------------------

        query = "SELECT ordertime FROM orders WHERE orderid = %s AND guestname = %s"
        args = (session['orderid'], session['guestname'])
        cur1.execute(query, args)
        ordertime = cur1.fetchone()[0]

    return render_template("/customer/receipt.html", guestname=session['guestname'], ordertime=ordertime, orderid=session['orderid'], \
        main_order_tuple=session['main_order_tuple'], detail_list=session['detail_list'], side_tuples=session['side_tuples'], \
        drink_tuples=session['drink_tuples'], totalorder=session['totalorder'])