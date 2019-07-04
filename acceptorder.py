#!/usr/bin/python


from http import cookies
from urllib.parse import parse_qs, urlparse

import os
import mysql.connector
import my

#------------------------------------------------------------------------------------------------------------------------
my.setcontent()
my.starthtml()
my.startbody()


#from mysql.connector import (errorcode)
try:
    cnx1 = mysql.connector.connect(user='usernameHere', password='pwHere', host='localHostIP', database='databaseName')
    cnx2 = mysql.connector.connect(user='usernameHere', password='pwHere', host='localhostIP', database='databaseName')
    cnx3 = mysql.connector.connect(user='usernameHere', password='pwHere', host='localhostIP', database='databaseName')

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
    cur3 = cnx3.cursor()
#---Read the environmental variables ------------------

    qs=os.environ['QUERY_STRING']
    guestname=my.parse_query(qs,'guestname')
    orderid=my.parse_query(qs,'orderid')
    orderstatus=my.parse_query(qs,'orderstatus')

#---Activate Order --------------------------------------------------

    query = "SELECT * from orders WHERE orderid = %s AND guestname = %s AND active = 0 "
    args = (orderid,guestname)
    cur1.execute(query,args)
    for r in cur1:
      query = "UPDATE orders SET active = %s where item_id = %s"
      args = (1,r[0])
      cur2.execute(query,args)
      cur2.execute("COMMIT")

#---Subtract order from Inventory -----------------------------------

    query = "SELECT * from orders WHERE orderid = %s AND guestname = %s"
    args = (orderid,guestname)
    cur1.execute(query,args)
    for r in cur1:
      queryin = "SELECT * from ingredients WHERE id = %s"
      args = r[4]
      cur2.execute(queryin,(args,))
      for qua in cur2:
        newstock = qua[2] - r[5]
        print(newstock)
        query = "UPDATE ingredients SET stock = %s where id = %s"
        args = (newstock,qua[0])
        cur3.execute(query,args)
        cur3.execute("COMMIT")

#------------------------------------------------------------------


    cur1.close()
    cnx1.close()
    cur2.close()
    cnx2.close()
    cur3.close()
    cnx3.close()




print("FD")

my.closebody()
my.closehtml()

