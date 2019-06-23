#!/usr/bin/python


from http import cookies
from urllib.parse import parse_qs, urlparse

import os
import mysql.connector
import my

#------------------------------------------------------------------------------------------------------------------------



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

#---Start a temporary Order ------------------

    qs=os.environ['QUERY_STRING']
    guestname=my.parse_query(qs,'guestname')
    orderid=my.parse_query(qs,'orderid')
    query = "INSERT INTO order_temp (guestname, orderid) VALUES (%s,%s)"
#    print(query)
    args = (guestname, orderid)
    cur.execute(query,args)
    cnx.commit()

#---Present Menu -------------------------------------------------------------------------------------------

    query = ("SELECT * from menu WHERE category='Food'")
#    print(query)
    cur.execute(query)

    my.starthtml()
    my.startheader()
    my.closeheader()

    print("<style> table, th, td { border: 1px solid black;</style>")

    my.startbody()

    my.startform('customizeorder.py')

#    print("<form action=\"customizeorder.py\">\r\n")

    print()
    print("<h3>Main Dishes</h3>")
    print("<table style=\"width:100%\">")
    print("<tr><td><h4>Description</h4></td><td><h4>Price</h4></td>") #<td><h4>Quantity</h4></td></tr>")
    for r in cur:
        print("<tr>")
        print("<td><input type=\"radio\" name=\"mainorder\" value=",r[0],">",r[1],"</td>","<td>",r[2],"</td>")  #<td><input type='text' quantity_main='quantmain'></td>")
        print("</tr>")
    print("</table>")
#---------------------------------------------------------------------------------------------------------------
    query = ("SELECT * from menu WHERE category='Side'")
    cur.execute(query)
    print("<table style=\"width:100%\">")
    print()
    print("<h3>Side Dishes</h3>")
    print("<tr><td><h4>Description</h4></td><td><h4>Price</h4></td>") #<td><h4>Quantity</h4></td></tr>")
    for r in cur:
        print("<tr>")
        print("<td><input type=\"radio\" name=\"sideorder\" value=",r[0],">",r[1],"</td>","<td>",r[2],"</td>")  #<td><input type='text' quantity_side='quantside'></td>")
        print("</tr>")
    print("</table>")
#---------------------------------------------------------------------------------------------------------------
    query = ("SELECT * from menu WHERE category='Drink'")
    cur.execute(query)
    print("<table style=\"width:100%\">")
    print()
    print("<h3>Drinks</h3>")
    print("<tr><td><h4>Description</h4></td><td><h4>Price</h4></td>") #<td><h4>Quantity</h4></td></tr>")
    for r in cur:
        print("<tr>")
        print("<td><input type=\"radio\" name=\"drinkorder\" value=",r[0],">",r[1],"</td>","<td>",r[2],"</td>")  #<td><input type='text' quantity_drink='quantdrink'></td>")
        print("</tr>")
    print("</table>")

    print("<input type='hidden' name='guestname' value=", guestname, "><br><br>")
    print("<input type='hidden' name='orderid' value=", orderid,"><br><br>")
    print("<br><br><input type=\"submit\" value=\"Customize your Order\">")

    my.closeform()
    my.closebody()
    my.closehtml()

    cur.close()
    cnx.close()
