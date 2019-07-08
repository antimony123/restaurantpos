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
    cnx1 = mysql.connector.connect(user='webaccess', password='mysqlcs160', host='127.0.0.1', database='RESMGTDB')
    cnx2 = mysql.connector.connect(user='webaccess', password='mysqlcs160', host='127.0.0.1', database='RESMGTDB')

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("User Name and Password for Database is not Correct")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(err)

finally:
    cur1 = cnx1.cursor()
    cur2 = cnx2.cursor()

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
    print("<br>--------------------------------------------------------------------------------<br>")
    print("<table >")
    print("<col width=\"400\"><col width=\"30\">")

#---Present Main Order --------------------------------------------------------------

    query = "SELECT * from menu WHERE id = %s "
    args = (mainorder)
    cur1.execute(query,(args,))
    for r in cur1:
       print("<tr><td>",r[1],"</td><td>",r[2],"</td></tr>")

    totalorder = totalorder + float(r[2])


#---Present Main Order Details --------------------------------------------------------

    for detail in details:
        query = "SELECT * from recipes WHERE ingredient_id = %s AND menu_id = %s"
        input_tuple = (detail, mainorder)
        cur1.execute(query,input_tuple)
        for r in cur1:
            print("<tr><td>-->",r[4],"</td></tr>")
            query = "INSERT INTO orders (orderid, guestname, mainorder, detail, quantity ) VALUES (%s,%s,%s,%s,%s)"
            args = (orderid, guestname,mainorder,detail,r[5])
            cur2.execute(query,args)
            cnx2.commit()

#---Enter into Orders the hidden items  ----------------------------------------------

    query = "SELECT * from recipes WHERE menu_id = %s AND to_show = 0"
    args = (mainorder)
    cur1.execute(query,(args,))
    for r in cur1:
        query = "INSERT INTO orders (orderid, guestname, mainorder, detail, quantity ) VALUES (%s,%s,%s,%s,%s)"
        args = (orderid, guestname,mainorder,r[3],r[5])
        cur2.execute(query,args)
        cnx2.commit()

#---Present Side Order --------------------------------------------------------------

    query = "SELECT * from menu WHERE id = %s "
    args = (sideorder)
    cur1.execute(query,(args,))
    for r in cur1:
       print("<tr><td>",r[1],"</td><td>",r[2],"</td></tr>")

    totalorder = totalorder + float(r[2])

#---------Enter Side Order into Orders

    query = "SELECT * from recipes WHERE menu_id = %s "
    args = (sideorder)
    cur1.execute(query,(args,))
    for r in cur1:
      query = "INSERT INTO orders (orderid, guestname, mainorder, detail, quantity ) VALUES (%s,%s,%s,%s,%s)"
      args = (orderid, guestname,sideorder,r[3],r[5])
      cur2.execute(query,args)
      cnx2.commit()

#---Present Drink order -------------------------------------------------------------

    query = "SELECT * from menu WHERE id = %s "
    args = (drinkorder)
    cur1.execute(query,(args,))
    for r in cur1:
       print("<tr><td>",r[1],"</td><td>",r[2],"</td></tr>")
    totalorder = totalorder + float(r[2])

#---------Enter Drink order into Orders --------------------------------------------

    query = "SELECT * from recipes WHERE menu_id = %s "
    args = (drinkorder)
    cur1.execute(query,(args,))
    for r in cur1:
       query = "INSERT INTO orders (orderid, guestname, mainorder, detail, quantity ) VALUES (%s,%s,%s,%s,%s)"
       args = (orderid, guestname,drinkorder,r[3],r[5])
       cur2.execute(query,args)
       cnx2.commit()

#---Finish presentation of items selected-------------------------------------------

    print("</table>")
    print("<br>--------------------------------------------------------------------------------<br>")
    print("<h3>Your Total amount today : ", totalorder)

#-----------------------------------------------------------------------------------

    print("<input type='hidden' name='guestname' value=", guestname, ">")
    print("<input type='hidden' name='orderid' value=", orderid,">")
    print("<input type='hidden' name='orderstatus' value=\"active\">")
    print("<br><br><input type=\"submit\" value=\"Pay for the Order\">")

    my.closeform()

#----------------------------------------------------------------------------------------------------------------  
    my.closebody()
    my.closehtml()
    cur1.close()
    cnx1.close()
    cur2.close()
    cnx2.close()
