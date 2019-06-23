#!/usr/bin/python

import datetime
import random
import string
import my

my.setcontent()
my.starthtml()
my.startheader()
print("<h1>Please Enter your Name </h1>")
my.closeheader()
my.startbody()
my.startform('displaymenu.py')
print("Firstname - <input type='text' name='guestname', required><br>")
print("<input type='hidden' name='orderid' value=",my.randomString(20),"><br><br>")
print()
print()
print("<input type=\"submit\" value=\"Press Here to View and Select from our Tasty Menu\">")
my.closeform()
print()
my.closebody()
my.closehtml()
