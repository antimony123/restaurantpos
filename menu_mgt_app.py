from flask import Flask, render_template, request
import mysql.connector as mc

app = Flask(__name__)

@app.route("/")
def main():
	return render_template("menu_mgt.html")

@app.route("/menu_mgt")
def main_menu():
	return render_template("menu_mgt.html")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Addition Handling~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/menu_add")
def add_item():
	return render_template("menu_add.html")

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
		mydb = mc.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
		cur = mydb.cursor()
	
		sql = "insert into menu (description, price, category) values (%s, %s, %s)"
		val = (request.form["item_name"], request.form["item_price"], request.form["item_category"])
		cur.execute(sql, val)

		mydb.commit()

		cur.execute("describe menu;")
		fields = [row[0] for row in cur]
		cur.execute("select * from menu;")
		data = [row for row in cur]

		return render_template("add_final.html", fields=fields, data=data)


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Price Change Handling~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/menu_prices")
def select_to_change():
	mydb = mc.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
	cur = mydb.cursor()
	
	cur.execute("describe menu;")
	fields = [row[0] for row in cur]
	cur.execute("select * from menu;")
	data = [row for row in cur]

	return render_template("menu_prices.html", fields=fields, data=data)

@app.route("/price_entry", methods=["POST", "GET"])
def price_entry():
	keys = [key for key in request.form.keys()]

	mydb = mc.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
	cur = mydb.cursor()

	cur.execute("describe menu;")
	fields = [row[0] for row in cur]

	if keys:
		data_string = "select * from menu where id ="
		data_string += " || id=".join(keys)
		data_string += ";"
	else:
		data_string = ""

	cur.execute(data_string)

	data = [row for row in cur]
	return render_template("price_entry.html", keys=keys, fields=fields, data=data)

@app.route("/price_review", methods=["POST", "GET"])
def price_review():
	if request.method == "POST" :

# TODO: price_entry acquires data by using input type="number". Where does it go, and how do I use it?		

	return render_template("price_review.html")


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Deletion Handling~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
@app.route("/menu_del")
def select_to_delete():
	mydb = mc.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
	cur = mydb.cursor()
	
	cur.execute("describe menu;")
	fields = [row[0] for row in cur]
	cur.execute("select * from menu;")
	data = [row for row in cur]

	return render_template("menu_del.html", fields=fields, data=data)

@app.route("/del_review", methods=["POST", "GET"])
def delete_review():
	if request.method == "POST" :
		keys = [key for key in request.form.keys()]

		mydb = mc.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
		cur = mydb.cursor()

		cur.execute("describe menu;")
		fields = [row[0] for row in cur]

		if keys:
			data_string = "select * from menu where id ="
			data_string += " || id=".join(keys)
			data_string += ";"
		else:
			data_string = ""

		cur.execute(data_string)
		data = [row for row in cur]

		return render_template("del_review.html", keys=keys, fields=fields, data=data)

@app.route("/del_final", methods=["POST", "GET"])
def delete_menu_item() :
	if request.method == "POST" :
		mydb = mc.connect(host="localhost", username="webaccess", passwd="cs160mysql", database="RESMGTDB")
		cur = mydb.cursor()

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
		cur.execute(sql)

		mydb.commit()

		cur.execute("describe menu;")
		fields = [row[0] for row in cur]
		cur.execute("select * from menu;")
		data = [row for row in cur]

		return render_template("del_final.html", fields=fields, data=data)

if __name__ == "__main__":
    app.run()