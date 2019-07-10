from flask import Flask, render_template, request, session
import os
import mysql.connector as mc

app = Flask(__name__)
app.secret_key = os.urandom(24)

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

	session['price_keys'] = keys
	session['fields'] = fields
	session['init_data'] = data

	return render_template("price_entry.html", keys=session['price_keys'], fields=session['fields'], data=session['init_data'])

@app.route("/price_review", methods=["POST", "GET"])
def price_review():
	if request.method == "POST" :		
		prices = [request.form.get(key) for key in session['price_keys']]
		data_and_prices = [(session['init_data'][i], prices[i]) for i in range(0, len(prices))]
		session['data_and_prices'] = data_and_prices
	return render_template("price_review.html", fields=session['fields'], data_and_prices=session['data_and_prices'])

@app.route("/price_retry")
def price_retry():
	return render_template("price_entry.html", keys=session['price_keys'], fields=session['fields'], data=session['init_data'])

@app.route("/price_final", methods=["POST", "GET"])
def change_price():
	if request.method == "POST" :
		mydb = mc.connect(host="localhost", user="webaccess", passwd="cs160mysql", database="RESMGTDB")
		cur = mydb.cursor()

#		TODO: This loop is hardcoded to work for editing the menu table. Edit it to work for ingredients, as well.
		for entry in session['data_and_prices'] :
			sql = "update menu set price = %s where id = %s;"
			val = (entry[1], entry[0][0])
			cur.execute(sql, val)
			mydb.commit()

		cur.execute("select * from menu;")
		data = [row for row in cur]

	return render_template("price_final.html", fields=session['fields'], data=data)


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

		session['del_keys'] = keys
		session['fields'] = fields

		return render_template("del_review.html", keys=keys, fields=fields, data=data)

@app.route("/del_final", methods=["POST", "GET"])
def delete_menu_item() :
	if request.method == "POST" :
		mydb = mc.connect(host="localhost", username="webaccess", passwd="cs160mysql", database="RESMGTDB")
		cur = mydb.cursor()
		
		keys = session['del_keys']
		print(keys)

		sql = "delete from menu where id="
		sql += " || id=".join(keys)
		sql += ";"
		cur.execute(sql)

		mydb.commit()

		cur.execute("select * from menu;")
		data = [row for row in cur]

		return render_template("del_final.html", fields=session['fields'], data=data)

if __name__ == "__main__":
    app.run()