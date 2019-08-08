import unittest

import sys
sys.path.insert(1, './restaurantpos')

from rpos.db import *
from rpos.models import *

class TestDatabase(unittest.TestCase):

    def test_init_db(self):
        init_db()
        tables = [i[0] for i in db_session.execute('SHOW TABLES;')]
        expected = ['ingredients', 'menu', 'orders', 'recipes', 'users']
        self.assertEqual(tables, expected)

    def test_ingredients_schema(self):
        col = Ingredient.__table__.columns.keys()
        e = [i[0] for i in db_session.execute('DESCRIBE ingredients;')]
        self.assertEqual(col, e)

    def test_menu_schema(self):
        col = MenuItem.__table__.columns.keys()
        e = [i[0] for i in db_session.execute('DESCRIBE menu;')]
        self.assertEqual(col, e)

    def test_orders_schema(self):
        col = Order.__table__.columns.keys()
        e = [i[0] for i in db_session.execute('DESCRIBE orders;')]
        self.assertEqual(col, e)

    def test_recipes_schema(self):
        col = Recipe.__table__.columns.keys()
        e = [i[0] for i in db_session.execute('DESCRIBE recipes;')]
        self.assertEqual(col, e)

    def test_users_schema(self):
        col = User.__table__.columns.keys()
        e = [i[0] for i in db_session.execute('DESCRIBE users;')]
        self.assertEqual(col, e)

if __name__ == '__main__':
    unittest.main()