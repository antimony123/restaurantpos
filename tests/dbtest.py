import unittest, os, sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
import db

class DatabaseTests(unittest.TestCase):

	def test_print_db_info(self):
		_db = db.Database("localhost", "webaccess", "cs160mysql", "RESMGTDB")
		s = "\nUser: webaccess\nHostname: localhost\nDatabase in use: RESMGTDB\n"
		self.assertEqual(_db.__str__(), s)
		_db.close()

if __name__ == '__main__':
	unittest.main()

