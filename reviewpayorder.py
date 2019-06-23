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
    print("<h2>Review and Pay for Your Order</h2>")
    qs=os.environ['QUERY_STRING']
#    print(os.environ)
#    print()
    guestname=my.parse_query(qs,'guestname')
    orderid=my.parse_query(qs,'orderid')
    mainorder=my.parse_query(qs,'mainorder')
    sideorder=my.parse_query(qs,'sideorder')
    drinkorder=my.parse_query(qs,'drinkorder')
    details=my.findinquery(qs,'detailorder')
    totalorder = 0.00

    my.starthtml()
    my.startbody()

#    for detail in details:
#        print(detail)
#    print(mainorder)


    my.startform('acceptorder.py')

    print("<h4>OrderID :",orderid,"</h4>")

    print("<h3>>>>>",guestname," Your Order Today is the Following </h3>")
    print("<br>-----------------------------------------------------------------<br>")
    print("<table style=\"width:100%\">")
    query = "SELECT * from menu WHERE id = %s "
    args = (mainorder)
    cur.execute(query,(args,))
    for r in cur:
       print("<tr><td>",r[1],".....",r[2],"</td></tr>")
    totalorder = totalorder + float(r[2])
#---Present Main Order Details --------------------------------------------------------
    for detail in details:
        query = "SELECT * from recipes WHERE ingredient_id = %s AND to_show = 1"
        args = (detail)
        cur.execute(query,(args,))
        for r in cur:
            print("<tr><td>-->",r[4],"</td></tr>")
#---Present Side Order --------------------------------------------------------------
    query = "SELECT * from menu WHERE id = %s "
    args = (sideorder)
    cur.execute(query,(args,))
    for r in cur:
       print("<tr><td>",r[1],".....",r[2],"</td></tr>")
    totalorder = totalorder + float(r[2])
#---Present Drink order -------------------------------------------------------------
    query = "SELECT * from menu WHERE id = %s "
    args = (drinkorder)
    cur.execute(query,(args,))
    for r in cur:
       print("<tr><td>",r[1],".....",r[2],"</td></tr>")
    totalorder = totalorder + float(r[2])
#---Finish presentation of items selected-------------------------------------------
    print("</table>")
    print("<br>-----------------------------------------------------------------<br>")
    print("<h3>Your Total amount today : ", totalorder)

    print("<br><br><input type=\"submit\" value=\"Finish\">")

    my.closeform()
#----------------------------------------------------------------------------------------------------------------  
    my.closebody()
    my.closehtml()
    cur.close()
    cnx.close()
