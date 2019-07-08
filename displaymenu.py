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
    cnx = mysql.connector.connect(user='username', password='pwHere', host='localhostIP', database='databaseName')

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

#---Present Menu -------------------------------------------------------------------------------------------

    my.starthtml()
    my.startheader()
    my.closeheader()

    print("<style> table, th, td { border: 1px solid black;</style>")

    my.startbody()
    my.startform('customizeorder.py')

#---------------------------------------------------------------------------------------------------------------

    query = ("SELECT * from menu WHERE category='Food'")
    cur.execute(query)

    print("<table>")
    print("<col width=\"400\"><col width=\"30\">")
    print()
    print("<h3>Main Dishes</h3>")
    print("<tr><td><h4>Description</h4></td><td><h4>Price</h4></td>")
    for r in cur:
        print("<tr>")
        print("<td><input type=\"radio\" name=\"mainorder\" value=",r[0],">",r[1],"</td>","<td>",r[2],"</td>")
        print("</tr>")
    print("</table>")

#---------------------------------------------------------------------------------------------------------------

    query = ("SELECT * from menu WHERE category='Side'")
    cur.execute(query)
    print("<table>")
    print("<col width=\"400\"><col width=\"30\">")
    print()
    print("<h3>Side Dishes</h3>")
    print("<tr><td><h4>Description</h4></td><td><h4>Price</h4></td>")
    for r in cur:
        print("<tr>")
        print("<td><input type=\"radio\" name=\"sideorder\" value=",r[0],">",r[1],"</td>","<td>",r[2],"</td>")
        print("</tr>")
    print("</table>")

#---------------------------------------------------------------------------------------------------------------
    query = ("SELECT * from menu WHERE category='Drink'")
    cur.execute(query)
    print("<table>")
    print("<col width=\"400\"><col width=\"30\">")
    print()
    print("<h3>Drinks</h3>")
    print("<tr><td><h4>Description</h4></td><td><h4>Price</h4></td>")
    for r in cur:
        print("<tr>")
        print("<td><input type=\"radio\" name=\"drinkorder\" value=",r[0],">",r[1],"</td>","<td>",r[2],"</td>")
        print("</tr>")
    print("</table>")
#---------------------------------------------------------------------------------------------------------------
    print("<input type='hidden' name='guestname' value=", guestname, "><br><br>")
    print("<input type='hidden' name='orderid' value=", orderid,"><br><br>")

    print("<br><br><input type=\"submit\" value=\"Customize your Order\">")

    my.closeform()
    my.closebody()
    my.closehtml()

    cur.close()
    cnx.close()
