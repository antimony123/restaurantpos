import unittest

import sys
sys.path.insert(1, '/home/Benten/devshit/sjsu/cs160/restaurantpos')

from rpos.utils import *

row_arr = ['Ingredient description_7', 'Menu description_30', 'Ingredient description_1', 
            'Ingredient quantity_17', 'Menu description_9', 'Ingredient quantity_4', 'Ingredient description_20', 
            'Ingredient quantity_1', 'Ingredient description_4', 'Menu description_11', 'Ingredient quantity_12', 
            'Ingredient quantity_6', 'Menu description_4', 'Show in menu?_25', 'Ingredient description_18', 
            'Ingredient quantity_2', 'Ingredient description_16', 'Ingredient description_24', 'Ingredient description_15', 
            'Menu description_29', 'Ingredient description_31', 'Menu description_2', 'Menu description_12', 
            'Menu description_5', 'Show in menu?_4', 'Ingredient description_21', 'Ingredient quantity_8', 
            'Show in menu?_12', 'Ingredient description_11', 'Ingredient description_26', 
            'Ingredient description_19', 'Menu description_27', 'Menu description_20', 'Ingredient quantity_16', 
            'Menu description_22', 'Show in menu?_14', 'Ingredient quantity_5', 'Menu description_28', 'Menu description_6', 
            'Ingredient description_13', 'Ingredient description_12', 'Ingredient description_2', 'Ingredient quantity_10', 
            'Ingredient description_25', 'Ingredient quantity_20', 'Ingredient description_17', 'Show in menu?_9', 
            'Menu description_13', 'Ingredient description_28', 'Menu description_18', 'Ingredient description_30', 
            'Show in menu?_26', 'Ingredient description_14', 'Ingredient quantity_28', 'Ingredient quantity_26', 
            'Menu description_15', 'Ingredient description_27', 'Menu description_14', 'Ingredient description_6', 
            'Show in menu?_30', 'Menu description_1', 'Ingredient quantity_11', 'Menu description_17', 'Show in menu?_6', 
            'Show in menu?_8', 'Show in menu?_22', 'Ingredient quantity_27', 'Ingredient quantity_21', 'Ingredient quantity_13', 
            'Show in menu?_31', 'Ingredient quantity_29', 'Show in menu?_23', 'Ingredient quantity_19', 'Show in menu?_7', 
            'Show in menu?_5', 'Menu description_19', 'Ingredient quantity_24', 'Ingredient description_23', 
            'Ingredient description_22', 'Ingredient quantity_14', 'Show in menu?_27', 'Menu description_23', 
            'Ingredient quantity_23', 'Show in menu?_18', 'Show in menu?_21', 'Menu description_7', 'Ingredient description_5', 
            'Ingredient quantity_30', 'Menu description_8', 'Ingredient quantity_31', 'Ingredient description_29', 
            'Ingredient quantity_25', 'Menu description_31', 'Menu description_10', 'Menu description_21', 
            'Ingredient quantity_18', 'Ingredient quantity_9', 'Menu description_25', 'Show in menu?_17', 
            'Ingredient quantity_22', 'Show in menu?_24', 'Menu description_16', 'Ingredient quantity_7', 
            'Ingredient description_9', 'Ingredient description_10', 'Show in menu?_10', 'Menu description_26', 
            'Show in menu?_11', 'Show in menu?_20', 'Show in menu?_29', 'Show in menu?_13', 'Show in menu?_28', 
            'Ingredient quantity_15', 'Ingredient description_8', 'Menu description_24', 'Show in menu?_19']
        
expected_dict = {1: ['Ingredient description', 'Ingredient quantity', 'Menu description'], 
                    2: ['Ingredient quantity', 'Menu description', 'Ingredient description'], 
                    4: ['Ingredient quantity', 'Ingredient description', 'Menu description', 'Show in menu?'], 
                    5: ['Menu description', 'Ingredient quantity', 'Show in menu?', 'Ingredient description'], 
                    6: ['Ingredient quantity', 'Menu description', 'Ingredient description', 'Show in menu?'], 
                    7: ['Ingredient description', 'Show in menu?', 'Menu description', 'Ingredient quantity'], 
                    8: ['Ingredient quantity', 'Show in menu?', 'Menu description', 'Ingredient description'], 
                    9: ['Menu description', 'Show in menu?', 'Ingredient quantity', 'Ingredient description'], 
                    10: ['Ingredient quantity', 'Menu description', 'Ingredient description', 'Show in menu?'], 
                    11: ['Menu description', 'Ingredient description', 'Ingredient quantity', 'Show in menu?'], 
                    12: ['Ingredient quantity', 'Menu description', 'Show in menu?', 'Ingredient description'], 
                    13: ['Ingredient description', 'Menu description', 'Ingredient quantity', 'Show in menu?'], 
                    14: ['Show in menu?', 'Ingredient description', 'Menu description', 'Ingredient quantity'], 
                    15: ['Ingredient description', 'Menu description', 'Ingredient quantity'], 
                    16: ['Ingredient description', 'Ingredient quantity', 'Menu description'], 
                    17: ['Ingredient quantity', 'Ingredient description', 'Menu description', 'Show in menu?'], 
                    18: ['Ingredient description', 'Menu description', 'Show in menu?', 'Ingredient quantity'], 
                    19: ['Ingredient description', 'Ingredient quantity', 'Menu description', 'Show in menu?'], 
                    20: ['Ingredient description', 'Menu description', 'Ingredient quantity', 'Show in menu?'], 
                    21: ['Ingredient description', 'Ingredient quantity', 'Show in menu?', 'Menu description'], 
                    22: ['Menu description', 'Show in menu?', 'Ingredient description', 'Ingredient quantity'], 
                    23: ['Show in menu?', 'Ingredient description', 'Menu description', 'Ingredient quantity'], 
                    24: ['Ingredient description', 'Ingredient quantity', 'Show in menu?', 'Menu description'], 
                    25: ['Show in menu?', 'Ingredient description', 'Ingredient quantity', 'Menu description'], 
                    26: ['Ingredient description', 'Show in menu?', 'Ingredient quantity', 'Menu description'], 
                    27: ['Menu description', 'Ingredient description', 'Ingredient quantity', 'Show in menu?'], 
                    28: ['Menu description', 'Ingredient description', 'Ingredient quantity', 'Show in menu?'], 
                    29: ['Menu description', 'Ingredient quantity', 'Ingredient description', 'Show in menu?'], 
                    30: ['Menu description', 'Ingredient description', 'Show in menu?', 'Ingredient quantity'], 
                    31: ['Ingredient description', 'Show in menu?', 'Ingredient quantity', 'Menu description']}

fd = {'Ingredient description': 'ingredient_description', 
      'Show in menu?': 'to_show', 
      'Ingredient quantity': 'ingredient_quantity', 
      'Menu description': 'menu_description'}

reqdict = {'Menu description_11':'Signature Hamburger', 
           'Show in menu?_24':'1', 
           'Menu description_24':'Diet Coke', 
           'Show in menu?_17':'1', 
           'Ingredient quantity_15':'1.00', 
           'Show in menu?_18':'1', 
           'Ingredient quantity_21':'8.00', 
           'Menu description_19':'Signature Hot Dog', 
           'Menu description_17':'Signature Hot Dog', 
           'Ingredient quantity_8':'0.50', 
           'Menu description_9':'Signature Hamburger', 
           'Ingredient description_5':'Cheddar Cheese (slice)', 
           'Ingredient description_14':'Mayo', 
           'Ingredient quantity_11':'1.00', 
           'Ingredient description_10':'Onion', 
           'Show in menu?_20':'1', 
           'Show in menu?_31':'1', 
           'Ingredient description_15':'Hot Dog Bun', 
           'Ingredient quantity_24':'1.00', 
           'Ingredient description_2':'Hamburger Bun', 
           'Show in menu?_10':'1', 
           'Ingredient quantity_18':'0.50', 
           'Show in menu?_9':'1', 
           'Show in menu?_21':'1', 
           'Ingredient description_29':'Hamburger Bun', 
           'Ingredient quantity_22':'8.00', 
           'Ingredient description_23':'Coke', 
           'Menu description_27':'Coffee', 
           'Menu description_12':'Signature Hamburger', 
           'Ingredient description_19':'Mustard', 
           'Ingredient description_20':'Chicken Strips', 
           'Menu description_6':'Signature Hamburger', 
           'Show in menu?_4':'1', 
           'Show in menu?_5':'1', 
           'Ingredient quantity_14':'0.50', 
           'Menu description_14':'Signature Hamburger', 
           'Menu description_20':'Chicken Strips', 
           'Ingredient description_16':'Beef Hot Dog', 
           'Show in menu?_13':'1', 'Ingredient quantity_27':'0.50', 
           'Menu description_31':'Signature Hamburger', 'Show in menu?_22':'1', 
           'Show in menu?_14':'1', 'Ingredient quantity_9':'1.00', 'Show in menu?_7':'1', 
           'Menu description_10':'Signature Hamburger', 'Ingredient quantity_30':'0.00', 
           'Ingredient description_27':'Ground Coffee Roast', 
           'Ingredient description_1':'Hamburger Bun', 'Show in menu?_11':'1', 
           'Ingredient description_17':'Relish', 'Show in menu?_27':'1', 
           'Ingredient quantity_10':'0.50', 'Menu description_7':'Signature Hamburger', 
           'Show in menu?_26':'1', 'Ingredient quantity_12':'0.50', 
           'Menu description_30':'Signature Hamburger', 'Ingredient description_22':'Onion Rings', 
           'Menu description_26':'Sprite', 'Ingredient description_26':'Sprite', 
           'Ingredient quantity_7':'2.00', 'Show in menu?_6':'1', 
           'Menu description_29':'Signature Hamburger', 'Ingredient quantity_23':'1.00', 
           'Ingredient description_31':'Hamburger Bun', 'Menu description_2':'Signature Hamburger', 
           'Ingredient quantity_17':'2.00', 'Menu description_8':'Signature Hamburger', 
           'Ingredient quantity_29':'0.00', 'Ingredient quantity_19':'0.50', 'Ingredient quantity_20':'3.00', 
           'Ingredient description_18':'Ketchup', 'Menu description_23':'Coke', 
           'Menu description_13':'Signature Hamburger', 'Ingredient description_12':'Ketchup', 
           'Ingredient description_24':'Diet Coke', 'Ingredient description_9':'Tomato', 
           'update':'Update table', 'Menu description_4':'Signature Hamburger', 
           'Ingredient description_28':'Sugar', 'Menu description_5':'Signature Hamburger', 
           'Ingredient description_13':'Mustard', 'Show in menu?_23':'1', 'Ingredient quantity_6':'1.00', 
           'Menu description_1':'Signature Hamburger', 'Show in menu?_19':'1', 
           'Menu description_18':'Signature Hot Dog', 'Ingredient quantity_28':'0.50', 
           'Menu description_28':'Coffee', 'Show in menu?_25':'1', 'Ingredient quantity_16':'1.00', 
           'Menu description_22':'Signature Hamburger', 'Ingredient description_7':'Hamburger Bun', 
           'Ingredient description_4':'American Cheese (slice)', 'Menu description_21':'Signature Hamburger', 
           'Menu description_25':'Root Beer', 'Show in menu?_8':'1', 'Ingredient quantity_25':'1.00', 
           'Ingredient quantity_4':'1.00', 'Show in menu?_29':'1', 'Ingredient description_8':'Lettuce', 
           'Menu description_16':'Signature Hot Dog', 'Ingredient quantity_31':'0.00', 
           'Ingredient description_30':'Hamburger Bun', 'Ingredient quantity_13':'0.50', 
           'Ingredient quantity_5':'1.00', 'Ingredient quantity_2':'1.00', 'Ingredient quantity_26':'1.00', 
           'Ingredient description_6':'Swiss Cheese (slice)', 'Show in menu?_28':'1', 'Show in menu?_12':'1', 
           'Ingredient description_25':'Root Beer', 'Show in menu?_30':'1', 
           'Ingredient description_21':'French Fries', 'Ingredient description_11':'Pickles', 
           'Menu description_15':'Signature Hot Dog', 'Ingredient quantity_1':'1.00'}

queries = ["UPDATE recipes SET ingredient_description='Hamburger Bun', ingredient_quantity='1.00', menu_description='Signature Hamburger' WHERE id = 1;", 
           "UPDATE recipes SET ingredient_quantity='1.00', menu_description='Signature Hamburger', ingredient_description='Hamburger Bun' WHERE id = 2;",
           "UPDATE recipes SET ingredient_quantity='1.00', ingredient_description='American Cheese (slice)', menu_description='Signature Hamburger', to_show=1 WHERE id = 4;",
           "UPDATE recipes SET menu_description='Signature Hamburger', ingredient_quantity='1.00', to_show=1, ingredient_description='Cheddar Cheese (slice)' WHERE id = 5;",
           "UPDATE recipes SET ingredient_quantity='1.00', menu_description='Signature Hamburger', ingredient_description='Swiss Cheese (slice)', to_show=1 WHERE id = 6;",
           "UPDATE recipes SET ingredient_description='Hamburger Bun', to_show=1, menu_description='Signature Hamburger', ingredient_quantity='2.00' WHERE id = 7;",
           "UPDATE recipes SET ingredient_quantity='0.50', to_show=1, menu_description='Signature Hamburger', ingredient_description='Lettuce' WHERE id = 8;",
           "UPDATE recipes SET menu_description='Signature Hamburger', to_show=1, ingredient_quantity='1.00', ingredient_description='Tomato' WHERE id = 9;",
           "UPDATE recipes SET ingredient_quantity='0.50', menu_description='Signature Hamburger', ingredient_description='Onion', to_show=1 WHERE id = 10;",
           "UPDATE recipes SET menu_description='Signature Hamburger', ingredient_description='Pickles', ingredient_quantity='1.00', to_show=1 WHERE id = 11;", 
           "UPDATE recipes SET ingredient_quantity='0.50', menu_description='Signature Hamburger', to_show=1, ingredient_description='Ketchup' WHERE id = 12;", 
           "UPDATE recipes SET ingredient_description='Mustard', menu_description='Signature Hamburger', ingredient_quantity='0.50', to_show=1 WHERE id = 13;", 
           "UPDATE recipes SET to_show=1, ingredient_description='Mayo', menu_description='Signature Hamburger', ingredient_quantity='0.50' WHERE id = 14;", 
           "UPDATE recipes SET ingredient_description='Hot Dog Bun', menu_description='Signature Hot Dog', ingredient_quantity='1.00' WHERE id = 15;", 
           "UPDATE recipes SET ingredient_description='Beef Hot Dog', ingredient_quantity='1.00', menu_description='Signature Hot Dog' WHERE id = 16;", 
           "UPDATE recipes SET ingredient_quantity='2.00', ingredient_description='Relish', menu_description='Signature Hot Dog', to_show=1 WHERE id = 17;", 
           "UPDATE recipes SET ingredient_description='Ketchup', menu_description='Signature Hot Dog', to_show=1, ingredient_quantity='0.50' WHERE id = 18;", 
           "UPDATE recipes SET ingredient_description='Mustard', ingredient_quantity='0.50', menu_description='Signature Hot Dog', to_show=1 WHERE id = 19;", 
           "UPDATE recipes SET ingredient_description='Chicken Strips', menu_description='Chicken Strips', ingredient_quantity='3.00', to_show=1 WHERE id = 20;", 
           "UPDATE recipes SET ingredient_description='French Fries', ingredient_quantity='8.00', to_show=1, menu_description='Signature Hamburger' WHERE id = 21;", 
           "UPDATE recipes SET menu_description='Signature Hamburger', to_show=1, ingredient_description='Onion Rings', ingredient_quantity='8.00' WHERE id = 22;", 
           "UPDATE recipes SET to_show=1, ingredient_description='Coke', menu_description='Coke', ingredient_quantity='1.00' WHERE id = 23;", 
           "UPDATE recipes SET ingredient_description='Diet Coke', ingredient_quantity='1.00', to_show=1, menu_description='Diet Coke' WHERE id = 24;", 
           "UPDATE recipes SET to_show=1, ingredient_description='Root Beer', ingredient_quantity='1.00', menu_description='Root Beer' WHERE id = 25;", 
           "UPDATE recipes SET ingredient_description='Sprite', to_show=1, ingredient_quantity='1.00', menu_description='Sprite' WHERE id = 26;", 
           "UPDATE recipes SET menu_description='Coffee', ingredient_description='Ground Coffee Roast', ingredient_quantity='0.50', to_show=1 WHERE id = 27;", 
           "UPDATE recipes SET menu_description='Coffee', ingredient_description='Sugar', ingredient_quantity='0.50', to_show=1 WHERE id = 28;", 
           "UPDATE recipes SET menu_description='Signature Hamburger', ingredient_quantity='0.00', ingredient_description='Hamburger Bun', to_show=1 WHERE id = 29;", 
           "UPDATE recipes SET menu_description='Signature Hamburger', ingredient_description='Hamburger Bun', to_show=1, ingredient_quantity='0.00' WHERE id = 30;", 
           "UPDATE recipes SET ingredient_description='Hamburger Bun', to_show=1, ingredient_quantity='0.00', menu_description='Signature Hamburger' WHERE id = 31;"]

morequeries = ["UPDATE recipes SET to_show=0, ingredient_description='Hamburger Bun', ingredient_id=1, ingredient_quantity='1.00', menu_description='Signature Hamburger', menu_id=1 WHERE id = 1;", "UPDATE recipes SET to_show=0, ingredient_quantity='1.00', menu_description='Signature Hamburger', menu_id=1, ingredient_description='Hamburger Bun', ingredient_id=1 WHERE id = 2;", "UPDATE recipes SET to_show=0, ingredient_quantity='1.00', ingredient_description='American Cheese (slice)', ingredient_id=4, menu_description='Signature Hamburger', menu_id=1, to_show=1 WHERE id = 4;", "UPDATE recipes SET to_show=0, menu_description='Signature Hamburger', menu_id=1, ingredient_quantity='1.00', to_show=1, ingredient_description='Cheddar Cheese (slice)', ingredient_id=5 WHERE id = 5;", "UPDATE recipes SET to_show=0, ingredient_quantity='1.00', menu_description='Signature Hamburger', menu_id=1, ingredient_description='Swiss Cheese (slice)', ingredient_id=6, to_show=1 WHERE id = 6;", "UPDATE recipes SET to_show=0, ingredient_description='Hamburger Bun', ingredient_id=1, to_show=1, menu_description='Signature Hamburger', menu_id=1, ingredient_quantity='2.00' WHERE id = 7;", "UPDATE recipes SET to_show=0, ingredient_quantity='0.50', to_show=1, menu_description='Signature Hamburger', menu_id=1, ingredient_description='Lettuce', ingredient_id=8 WHERE id = 8;", "UPDATE recipes SET to_show=0, menu_description='Signature Hamburger', menu_id=1, to_show=1, ingredient_quantity='1.00', ingredient_description='Tomato', ingredient_id=9 WHERE id = 9;", "UPDATE recipes SET to_show=0, ingredient_quantity='0.50', menu_description='Signature Hamburger', menu_id=1, ingredient_description='Onion', ingredient_id=10, to_show=1 WHERE id = 10;", "UPDATE recipes SET to_show=0, menu_description='Signature Hamburger', menu_id=1, ingredient_description='Pickles', ingredient_id=11, ingredient_quantity='1.00', to_show=1 WHERE id = 11;", "UPDATE recipes SET to_show=0, ingredient_quantity='0.50', menu_description='Signature Hamburger', menu_id=1, to_show=1, ingredient_description='Ketchup', ingredient_id=12 WHERE id = 12;", "UPDATE recipes SET to_show=0, ingredient_description='Mustard', ingredient_id=13, menu_description='Signature Hamburger', menu_id=1, ingredient_quantity='0.50', to_show=1 WHERE id = 13;", "UPDATE recipes SET to_show=0, to_show=1, ingredient_description='Mayo', ingredient_id=14, menu_description='Signature Hamburger', menu_id=1, ingredient_quantity='0.50' WHERE id = 14;", "UPDATE recipes SET to_show=0, ingredient_description='Hot Dog Bun', ingredient_id=15, menu_description='Signature Hot Dog', menu_id=2, ingredient_quantity='1.00' WHERE id = 15;", "UPDATE recipes SET to_show=0, ingredient_description='Beef Hot Dog', ingredient_id=16, ingredient_quantity='1.00', menu_description='Signature Hot Dog', menu_id=2 WHERE id = 16;", "UPDATE recipes SET to_show=0, ingredient_quantity='2.00', ingredient_description='Relish', ingredient_id=17, menu_description='Signature Hot Dog', menu_id=2, to_show=1 WHERE id = 17;", "UPDATE recipes SET to_show=0, ingredient_description='Ketchup', ingredient_id=12, menu_description='Signature Hot Dog', menu_id=2, to_show=1, ingredient_quantity='0.50' WHERE id = 18;", "UPDATE recipes SET to_show=0, ingredient_description='Mustard', ingredient_id=13, ingredient_quantity='0.50', menu_description='Signature Hot Dog', menu_id=2, to_show=1 WHERE id = 19;", "UPDATE recipes SET to_show=0, ingredient_description='Chicken Strips', ingredient_id=18, menu_description='Chicken Strips', menu_id=3, ingredient_quantity='3.00', to_show=1 WHERE id = 20;", "UPDATE recipes SET to_show=0, ingredient_description='French Fries', ingredient_id=19, ingredient_quantity='8.00', to_show=1, menu_description='Signature Hamburger', menu_id=1 WHERE id = 21;", "UPDATE recipes SET to_show=0, menu_description='Signature Hamburger', menu_id=1, to_show=1, ingredient_description='Onion Rings', ingredient_id=20, ingredient_quantity='8.00' WHERE id = 22;", "UPDATE recipes SET to_show=0, to_show=1, ingredient_description='Coke', ingredient_id=21, menu_description='Coke', menu_id=6, ingredient_quantity='1.00' WHERE id = 23;", "UPDATE recipes SET to_show=0, ingredient_description='Diet Coke', ingredient_id=22, ingredient_quantity='1.00', to_show=1, menu_description='Diet Coke', menu_id=7 WHERE id = 24;", "UPDATE recipes SET to_show=0, to_show=1, ingredient_description='Root Beer', ingredient_id=23, ingredient_quantity='1.00', menu_description='Root Beer', menu_id=8 WHERE id = 25;", "UPDATE recipes SET to_show=0, ingredient_description='Sprite', ingredient_id=24, to_show=1, ingredient_quantity='1.00', menu_description='Sprite', menu_id=9 WHERE id = 26;", "UPDATE recipes SET to_show=0, menu_description='Coffee', menu_id=10, ingredient_description='Ground Coffee Roast', ingredient_id=25, ingredient_quantity='0.50', to_show=1 WHERE id = 27;", "UPDATE recipes SET to_show=0, menu_description='Coffee', menu_id=10, ingredient_description='Sugar', ingredient_id=26, ingredient_quantity='0.50', to_show=1 WHERE id = 28;", "UPDATE recipes SET to_show=0, menu_description='Signature Hamburger', menu_id=1, ingredient_quantity='0.00', ingredient_description='Hamburger Bun', ingredient_id=1, to_show=1 WHERE id = 29;", "UPDATE recipes SET to_show=0, menu_description='Signature Hamburger', menu_id=1, ingredient_description='Hamburger Bun', ingredient_id=1, to_show=1, ingredient_quantity='0.00' WHERE id = 30;", "UPDATE recipes SET to_show=0, ingredient_description='Hamburger Bun', ingredient_id=1, to_show=1, ingredient_quantity='0.00', menu_description='Signature Hamburger', menu_id=1 WHERE id = 31;"]

class TestUtils(unittest.TestCase):

    def test_beautify(self):
        self.assertEqual(beautify('menu_items'), 'Menu items')
        self.assertEqual(beautify('make_this_pretty'), 'Make this pretty')

    def test_beautify_arr(self):
        arr = ['menu_items', 'make_this_pretty', 'low_threshold', 'et_cetera']
        beautified_arr = ['Menu items', 'Make this pretty', 'Low threshold', 'Et cetera']
        self.assertEqual(beautify_arr(arr), beautified_arr)

    def test_generate_rows(self):
        self.assertEqual(generate_rows(row_arr), expected_dict)

    def test_sql_query_from(self):
        self.assertEqual(sql_query_from_dict('recipes', expected_dict, fd, reqdict), morequeries)

    def test_is_int(self):
        self.assertTrue(is_int('1'))
        self.assertFalse(is_int('yes'))

if __name__ == '__main__':
    unittest.main()