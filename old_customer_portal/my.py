import datetime
import random
import string

#--------------------------------------------------------------------------------------------------------
def parse_query(query,fieldname):
  qs = query.split('&')
  for qa in qs:
    fields = qa.split('=')
    if fields[0]==fieldname:
       return fields[1]
  return ""
#--------------------------------------------------------------------------------------------------------
def findinquery(query,fieldname):
  fieldlist =[]
  qs = query.split('&')
  for qa in qs:
    fields = qa.split('=')
    if fields[0]==fieldname:
       fieldlist.append(fields[1])
  return fieldlist
#-------------------------------------------------------------------------------------------------------
def randomString(stringLength=20):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))
#------------------------------------------------------------------------------------------------------
def setcontent():
	print("Content-type: text/html\r\n")
#--------------------
def starthtml():
	print("<html>\r\n")
#--------------------
def startbody():
	print("<body>\r\n")
#-------------------
def startheader():
	print("<head>\r\n")
#------------------
def closeheader():
	print("</head>\r\n")
#--------------------
def closebody():
	print("</body>\r\n")
#--------------------
def closehtml():
	print("</html>\r\n")
#--------------------
def startform(action):
	print("<form action = ",action,">")
#--------------------
def closeform():
	print("</form>")
