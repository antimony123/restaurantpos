from flask import Flask, render_template, request

import db

app = Flask(__name__)
resdb = db.RestaurantDB("localhost")

# _manager_logged_in = False

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/login")
def login():
	return render_template('login.html', error=False)

@app.route("/verifylogin", methods=['POST', 'GET'])
def verifylogin():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		# check with database user/pass that it is correct

		sql = "select * from users where username='manager'"
		resdb.cur.execute(sql)
		
		data = resdb.cur.fetchone()
		
		if data[0] == username and data[1] == password:
			return render_template('managerportal.html')
		return render_template('login.html', error=True)


@app.route("/menu_mgt", methods=["POST", "GET"])
def main_menu():
	keys = "Menu"
	if request.method == "POST":
		keys = [k for k in request.form.keys()]
	return render_template("menu_mgt.html", table=keys[0])

@app.route("/menu_add/<table>")
def add_item(table):
        return render_template("menu_add.html", table=table)

@app.route("/add_review", methods=["POST", "GET"])
def add_review():
        if request.method == "POST" :
	#TODO: implement error handling
                if not request.form["item_name"] or not request.form["item_price"] or not request.form["item_category"] :
                        return render_template("menu_add.html")
                return render_template("add_review.html", item_name=request.form["item_name"], \
                        item_price=request.form["item_price"], item_category=request.form["item_category"] )

@app.route("/add_final", methods=["POST", "GET"])
def insert_new_menu_item():
	if request.method == "POST" :

		entry = (request.form["item_name"], \
			request.form["item_price"], \
			request.form["item_category"])

		resdb.create_entry("menu", entry)

		return render_template("add_final.html", \
					fields=resdb.get_field_names("menu"), \
					data=resdb.get_table_contents("menu"))

@app.route("/menu_del")
def select_to_delete():
	return render_template("menu_del.html", \
				fields=resdb.get_field_names("menu"), \
				data=resdb.get_table_contents("menu"))

@app.route("/del_review", methods=["POST", "GET"])
def delete_review():
	if request.method == "POST" :
		keys = [key for key in request.form.keys()]

		if keys:
			data_string = "select * from menu where id ="
			data_string += " || id=".join(keys)
			data_string += ";"
		else:
			data_string = ""

		resdb.cur.execute(data_string)
		data = [row for row in cur]

		return render_template("del_review.html", keys=keys, fields=resdb.get_field_names("menu"), data=data)

@app.route("/del_final", methods=["POST", "GET"])
def delete_menu_item() :
	if request.method == "POST" :

		char_list = []
		for char in request.form["keys"] :
			char_list.append(str(char))

		int_list = []
		write_flag = False
		new_int = ""
		for char in char_list :
			if char == "'" and not write_flag :
				write_flag = True
			elif char != "'" and write_flag :
				new_int += str(char)
			elif char == "'" and write_flag :
				int_list.append(new_int)
				new_int = ""
				write_flag = False

		sql = "delete from menu where id="
		sql += " || id=".join(int_list)
		sql += ";"
		resdb.cur.execute(sql)
		resdb.db.commit()

		return render_template("del_final.html", \
					fields=resdb.get_field_names("menu"), \
					data=resdb.get_table_contents("menu"))

if __name__ == "__main__":
    app.run()

