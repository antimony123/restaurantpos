
giant_arr = ['Ingredient description_7', 'Menu description_30', 'Ingredient description_1', 'Ingredient quantity_17', 'Menu description_9', 'Ingredient quantity_4', 'Ingredient description_20', 'Ingredient quantity_1', 'Ingredient description_4', 'Menu description_11', 'Ingredient quantity_12', 'Ingredient quantity_6', 'Menu description_4', 'Show in menu?_25', 'Ingredient description_18', 'Ingredient quantity_2', 'Ingredient description_16', 'Ingredient description_24', 'Ingredient description_15', 'Menu description_29', 'Ingredient description_31', 'Menu description_2', 'Menu description_12', 'Menu description_5', 'Show in menu?_4', 'Ingredient description_21', 'Ingredient quantity_8', 'Show in menu?_12', 'Ingredient description_11', 'Ingredient description_26', 'Ingredient description_19', 'Menu description_27', 'Menu description_20', 'Ingredient quantity_16', 'Menu description_22', 'Show in menu?_14', 'Ingredient quantity_5', 'Menu description_28', 'Menu description_6', 'Ingredient description_13', 'Ingredient description_12', 'Ingredient description_2', 'Ingredient quantity_10', 'Ingredient description_25', 'Ingredient quantity_20', 'Ingredient description_17', 'Show in menu?_9', 'Menu description_13', 'Ingredient description_28', 'Menu description_18', 'Ingredient description_30', 'Show in menu?_26', 'Ingredient description_14', 'Ingredient quantity_28', 'Ingredient quantity_26', 'Menu description_15', 'Ingredient description_27', 'Menu description_14', 'Ingredient description_6', 'Show in menu?_30', 'Menu description_1', 'Ingredient quantity_11', 'Menu description_17', 'Show in menu?_6', 'Show in menu?_8', 'Show in menu?_22', 'Ingredient quantity_27', 'Ingredient quantity_21', 'Ingredient quantity_13', 'Show in menu?_31', 'Ingredient quantity_29', 'Show in menu?_23', 'Ingredient quantity_19', 'Show in menu?_7', 'Show in menu?_5', 'Menu description_19', 'Ingredient quantity_24', 'Ingredient description_23', 'Ingredient description_22', 'Ingredient quantity_14', 'Show in menu?_27', 'Menu description_23', 'Ingredient quantity_23', 'Show in menu?_18', 'Show in menu?_21', 'Menu description_7', 'Ingredient description_5', 'Ingredient quantity_30', 'Menu description_8', 'Ingredient quantity_31', 'Ingredient description_29', 'Ingredient quantity_25', 'Menu description_31', 'Menu description_10', 'Menu description_21', 'Ingredient quantity_18', 'Ingredient quantity_9', 'Menu description_25', 'Show in menu?_17', 'Ingredient quantity_22', 'Show in menu?_24', 'Menu description_16', 'Ingredient quantity_7', 'Ingredient description_9', 'Ingredient description_10', 'Show in menu?_10', 'Menu description_26', 'Show in menu?_11', 'Show in menu?_20', 'Show in menu?_29', 'Show in menu?_13', 'Show in menu?_28', 'Ingredient quantity_15', 'Ingredient description_8', 'Menu description_24', 'Show in menu?_19']
fd = {'Ingredient description': 'ingredient_description', 'Show in menu?': 'to_show', 'Ingredient quantity': 'ingredient_quantity', 'Menu description': 'menu_description'}
reqdict = {'Menu description_11':'Signature Hamburger', 'Show in menu?_24':'1', 'Menu description_24':'Diet Coke', 'Show in menu?_17':'1', 'Ingredient quantity_15':'1.00', 'Show in menu?_18':'1', 'Ingredient quantity_21':'8.00', 'Menu description_19':'Signature Hot Dog', 'Menu description_17':'Signature Hot Dog', 'Ingredient quantity_8':'0.50', 'Menu description_9':'Signature Hamburger', 'Ingredient description_5':'Cheddar Cheese (slice)', 'Ingredient description_14':'Mayo', 'Ingredient quantity_11':'1.00', 'Ingredient description_10':'Onion', 'Show in menu?_20':'1', 'Show in menu?_31':'1', 'Ingredient description_15':'Hot Dog Bun', 'Ingredient quantity_24':'1.00', 'Ingredient description_2':'Hamburger Bun', 'Show in menu?_10':'1', 'Ingredient quantity_18':'0.50', 'Show in menu?_9':'1', 'Show in menu?_21':'1', 'Ingredient description_29':'Hamburger Bun', 'Ingredient quantity_22':'8.00', 'Ingredient description_23':'Coke', 'Menu description_27':'Coffee', 'Menu description_12':'Signature Hamburger', 'Ingredient description_19':'Mustard', 'Ingredient description_20':'Chicken Strips', 'Menu description_6':'Signature Hamburger', 'Show in menu?_4':'1', 'Show in menu?_5':'1', 'Ingredient quantity_14':'0.50', 'Menu description_14':'Signature Hamburger', 'Menu description_20':'Chicken Strips', 'Ingredient description_16':'Beef Hot Dog', 'Show in menu?_13':'1', 'Ingredient quantity_27':'0.50', 'Menu description_31':'Signature Hamburger', 'Show in menu?_22':'1', 'Show in menu?_14':'1', 'Ingredient quantity_9':'1.00', 'Show in menu?_7':'1', 'Menu description_10':'Signature Hamburger', 'Ingredient quantity_30':'0.00', 'Ingredient description_27':'Ground Coffee Roast', 'Ingredient description_1':'Hamburger Bun', 'Show in menu?_11':'1', 'Ingredient description_17':'Relish', 'Show in menu?_27':'1', 'Ingredient quantity_10':'0.50', 'Menu description_7':'Signature Hamburger', 'Show in menu?_26':'1', 'Ingredient quantity_12':'0.50', 'Menu description_30':'Signature Hamburger', 'Ingredient description_22':'Onion Rings', 'Menu description_26':'Sprite', 'Ingredient description_26':'Sprite', 'Ingredient quantity_7':'2.00', 'Show in menu?_6':'1', 'Menu description_29':'Signature Hamburger', 'Ingredient quantity_23':'1.00', 'Ingredient description_31':'Hamburger Bun', 'Menu description_2':'Signature Hamburger', 'Ingredient quantity_17':'2.00', 'Menu description_8':'Signature Hamburger', 'Ingredient quantity_29':'0.00', 'Ingredient quantity_19':'0.50', 'Ingredient quantity_20':'3.00', 'Ingredient description_18':'Ketchup', 'Menu description_23':'Coke', 'Menu description_13':'Signature Hamburger', 'Ingredient description_12':'Ketchup', 'Ingredient description_24':'Diet Coke', 'Ingredient description_9':'Tomato', 'update':'Update table', 'Menu description_4':'Signature Hamburger', 'Ingredient description_28':'Sugar', 'Menu description_5':'Signature Hamburger', 'Ingredient description_13':'Mustard', 'Show in menu?_23':'1', 'Ingredient quantity_6':'1.00', 'Menu description_1':'Signature Hamburger', 'Show in menu?_19':'1', 'Menu description_18':'Signature Hot Dog', 'Ingredient quantity_28':'0.50', 'Menu description_28':'Coffee', 'Show in menu?_25':'1', 'Ingredient quantity_16':'1.00', 'Menu description_22':'Signature Hamburger', 'Ingredient description_7':'Hamburger Bun', 'Ingredient description_4':'American Cheese (slice)', 'Menu description_21':'Signature Hamburger', 'Menu description_25':'Root Beer', 'Show in menu?_8':'1', 'Ingredient quantity_25':'1.00', 'Ingredient quantity_4':'1.00', 'Show in menu?_29':'1', 'Ingredient description_8':'Lettuce', 'Menu description_16':'Signature Hot Dog', 'Ingredient quantity_31':'0.00', 'Ingredient description_30':'Hamburger Bun', 'Ingredient quantity_13':'0.50', 'Ingredient quantity_5':'1.00', 'Ingredient quantity_2':'1.00', 'Ingredient quantity_26':'1.00', 'Ingredient description_6':'Swiss Cheese (slice)', 'Show in menu?_28':'1', 'Show in menu?_12':'1', 'Ingredient description_25':'Root Beer', 'Show in menu?_30':'1', 'Ingredient description_21':'French Fries', 'Ingredient description_11':'Pickles', 'Menu description_15':'Signature Hot Dog', 'Ingredient quantity_1':'1.00'}


def generate_rows(arr):
    row_dict = {}
    for i in arr:
        field, id = i.split('_')
        if int(id) not in row_dict.keys():
            row_dict[int(id)] = [field]
        else:
            row_dict[int(id)].append(field)
    
    return row_dict

def sql_query_from_dict(table, idd, fieldd, reqd):
    queries = []

    sql = 'UPDATE ' + table + ' SET '

    for id in idd.keys():
        query = sql
        for col in idd[id]:
            fieldname = fieldd[col]
            val = reqd[col + '_' + str(id)]

            if not is_int(val):
                query += fieldname + "='" + val + "', "
            else:
                query += fieldname + '=' + val + ', '

        query = query[:-2] + ' WHERE id = ' + str(id) + ';'
        queries.append(query)

    return queries


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False



idd = generate_rows(giant_arr)
print(sql_query_from_dict('recipes', idd, fd, reqdict))