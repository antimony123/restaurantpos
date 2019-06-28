import mysql.connector as mc

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
	def create_entry(self, entry, table):
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
		print(sql)
		
		try:
			self.cur.execute(sql, entry)
			for x in self.cur:
				print(x)
		except mc.Error as mce:
			print(mce)

	'''Delete specified entry in specified table'''
	def delete_entry(self, entry, table):
		pass

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


class RestaurantDB:

	def __init__():
		pass

