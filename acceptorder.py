#!/usr/bin/python

import datetime
import random
import string
import my

my.setcontent()
my.starthtml()
my.startheader()
print("<h1>Thank you for your order </h1>")
my.closeheader()
my.startbody()
print("Submit ticket to Kitchen")
print("Subtract inventory")
print("Add payment to revenue books")
my.closebody()
my.closehtml()
