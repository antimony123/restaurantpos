#/usr/bin/python

from http import cookies
from urllib.parse import parse_qs, urlparse

import os
import mysql.connector

#--------------------------------------------------------------------

def parse_query(query,fieldname):
  qs = query.split('&')
  for qa in qs:
    fields = qa.split('=')
    if fields[0]==fieldname:
       return fields[1]
  return ""


#-----------------------------------------------------------------------

querystring="field1=value1&field2=value2&field3=value3"

print(parse_query(querystring,"field0"))
