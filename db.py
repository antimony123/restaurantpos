import mysql.connector as mc

# running bug list
# creation does not check for duplicates.
# deletion does not fail gracefully if item does not exist in db.
# RestaurantDB class does not have methods to add/delete/modify orders, users, or recipe tables. 


class Database:

	def __init__(self, host, user, passwd, dbname):
		self.user = user	# username
		self.host = host	# host
		self.dbname = dbname	# name of database
		self.db = None		# actual database
		self.cur = None		# cursor of database

		try:
			self.db = mc.connect(host=self.host,
					     user=self.user,
					     passwd=passwd,
					     database=self.dbname)
			self.cur = self.db.cursor()
		except mc.Error as mce:
			print(mce)

	def __str__(self):
		return "\nUser: " + self.user + "\nHostname: " + self.host + "\nDatabase in use: " + self.dbname + "\n"

	def close(self):
		self.db.close()

	'''Create new entry in specified table. entry is an array of strings'''
	def create_entry(self, table, entry):

		fields = self.get_field_names(table)[1:]	# slicing this to not include id since id auto-increments

		sql = "INSERT INTO " + table + " ("

		for i in range(len(entry)):
			if i == len(entry)-1:
				sql = sql + fields[i] + ") VALUES ("
			else:
				sql = sql + fields[i] + ", "

		for i in range(len(entry)):
			if i == len(entry)-1:
				sql = sql + "%s);"
			else:
				sql = sql + "%s, "	
	
		try:
			self.cur.execute(sql, entry)
			self.db.commit()
		except mc.Error as mce:
			print(mce)

	'''Delete specified entry in specified table.
	   deltup is a tuple specifying (field, value),
	   e.g. (description, "some kinda sauce").'''
	def delete_entry(self, table, entry):

		sql = 'DELETE FROM ' + table + ' WHERE ' + entry[0] + ' = " ' + entry[1] + '"'

		try:
			self.cur.execute(sql)
			self.db.commit()
		except mc.Error as mce:
			print(mce)

	'''Update entry in specified table.
	   Both oldentry and newentry are tuples
	   specifying (field, value).
	   E.g. oldentry = ("description", "ketchup")
	   newentry = ("description", "tomato sauce")
	   will change the "ketchup" entry in the db
	   to have a description of "tomato sauce".'''
	def modify_entry(self, table, oldentry, newentry):
		
		sql = 'UPDATE ' + table + ' SET ' + newentry[0] + ' = "' + newentry[1] + \
		      '" WHERE ' + oldentry[0] + ' = "' + oldentry[1] + '";'

		print(sql)

		try:
			self.cur.execute(sql)
			self.db.commit()
		except mc.Error as mce:
			print(mce)



	'''Get description of a table by column, e.g. Field'''
	def get_field_names(self, table):
		try:
			self.cur.execute("DESCRIBE " + table + ";")
			return [x[0] for x in self.cur]
		except mc.Error as mce:
			print(mce)

	'''Get contents of specified table'''
	def get_table_contents(self, table):
		try:
			self.cur.execute("SELECT * FROM " + table + ";")
			return [x for x in self.cur]
		except mc.Error as mce:
			print(mce)


class RestaurantDB(Database):

	def __init__(self, host):
		super().__init__(host, "webaccess", "cs160mysql", "RESMGTDB")

	def add_ingredient(self, ingredient):
		pass

	def delete_ingredient(self, ingredient):
		pass

	def add_menu_item(self, item):
		pass

	def delete_menu_item(self, item):
		pass









