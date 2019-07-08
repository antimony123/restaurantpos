#!/usr/bin/python
from http import cookies
from urllib.parse import parse_qs, urlparse

import os
import mysql.connector
import my

#-----------------------------------------------------------------------------------------------------------------

my.setcontent()

#from mysql.connector import (errorcode)
try:
    cnx = mysql.connector.connect(user='webaccess', password='mysqlcs160', host='127.0.0.1', database='RESMGTDB')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User Name and Password for Database is not Correct")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

finally:
    cur = cnx.cursor()
    print("<h2>Customize Your Order</h2>")
    qs=os.environ['QUERY_STRING']
#    print(os.environ)
#    print()
    guestname=my.parse_query(qs,'guestname')
    orderid=my.parse_query(qs,'orderid')
    mainorder=my.parse_query(qs,'mainorder')
    sideorder=my.parse_query(qs,'sideorder')
    drinkorder=my.parse_query(qs,'drinkorder')
    my.starthtml()
    my.startbody()

#    print("<br><br><br>",mainorder,sideorder,drinkorder,guestname,orderid)
    my.startform('reviewpayorder.py')

    print("<h4>OrderID :",orderid,"</h4>")

#---Present Maindish-----------------------------------------------------------------
    query = "SELECT * from menu WHERE id = %s "
    args = (mainorder)
    cur.execute(query,(args,))
    for r in cur:
       maindish = r[1]
#-------------------------------------------------------------------------------------

    print("<h3>..",guestname," how would you like your ",maindish," today.!</h3>")

#---Present Maindish Option with---------------------------------------------------------------
    print("<table style=\"width:100%\">")
    query = "SELECT * from recipes WHERE menu_id = %s AND to_show = 1"
    args = (mainorder)
    cur.execute(query,(args,))
    for r in cur:
        print("<tr><td><input type=\"checkbox\" name=\"detailorder\" value=",r[3],">",r[4],"</td></tr>")
    print("</table>")
    print("<br>--------------------------------------------------<br><br>")
    print("<h4>")
#---Present Side Order --------------------------------------------------------------
    query = "SELECT * from menu WHERE id = %s "
    args = (sideorder)
    cur.execute(query,(args,))
    for r in cur:
       sidedish = r[1]
    print("Your Side Order today : ",sidedish)
    print("<br>--------------------------------------------------<br><br>")

#---Present Drink order -------------------------------------------------------------
    query = "SELECT * from menu WHERE id = %s "
    args = (drinkorder)
    cur.execute(query,(args,))
    for r in cur:
       drink = r[1]
    print("Your Drinks Order today: ",drink)
    print("<br>--------------------------------------------------<br><br>")
#-----------------------------------------------------------------------------------
    print("<input type='hidden' name='guestname' value=", guestname, ">")
    print("<input type='hidden' name='orderid' value=", orderid,">")
    print("<input type='hidden' name='mainorder' value=", mainorder, ">")
    print("<input type='hidden' name='sideorder' value=", sideorder,">")
    print("<input type='hidden' name='drinkorder' value=", drinkorder,">")
    print("<br><br><input type=\"submit\" value=\"Review your Order & Pay\">")

    my.closeform()

#----------------------------------------------------------------------------------------------------------------  
    my.closebody()
    my.closehtml()
    cur.close()
    cnx.close()
