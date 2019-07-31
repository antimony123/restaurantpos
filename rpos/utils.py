
from rpos.db import db_session

def beautify(s):
    s = s.replace('_', ' ')
    return s[0].upper() + s[1:]

def beautify_arr(arr):
    for i in range(len(arr)):
        arr[i] = beautify(arr[i])
    return arr

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
        if table == 'recipes':
            query += 'to_show=0, '
        for col in idd[id]:
            fieldname = fieldd[col]
            val = reqd[col + '_' + str(id)]

            if not is_int(val):
                query += fieldname + "='" + val + "', "
            else:
                query += fieldname + '=' + val + ', '

            # handle menu_id and ingredient_id here. only for recipes table
            if table == 'recipes':
                ingids = {key:value for (key, value) in db_session.execute('SELECT description, id FROM ingredients;')}
                menuids = {key:value for (key, value) in db_session.execute('SELECT description, id FROM menu;')}
                if fieldname == 'ingredient_description':
                    query += 'ingredient_id=' + str(ingids[val]) + ', '
                elif fieldname == 'menu_description':
                    query += 'menu_id=' + str(menuids[val]) + ', '

        query = query[:-2] + ' WHERE id = ' + str(id) + ';'
        queries.append(query)
        db_session.execute(query)
        db_session.commit()

    return queries


def is_int(s):
    try:
        int(s)
        return True
    except ValueError:
        return False