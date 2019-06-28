from flask import Flask, render_template, request

import db

app = Flask(__name__)
resdb = db.RestaurantDB("localhost")

@app.route("/")
def main():
	return render_template('index.html')

@app.route("/login")
def login():
	return render_template('login.html')

@app.route("/verifylogin", methods=['POST', 'GET'])
def verifylogin():
	if request.method == 'POST':
		username = request.form['username']
		password = request.form['password']
		print(username, password)
	else:
		print("ERROR!!")
	return render_template('index.html')

@app.route("/menu_mgt")
def main_menu():
        return render_template("menu_mgt.html")

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
	if request.method == "POST":
		print([i for i in request.form.keys()])
	return render_template("del_review.html")


if __name__ == "__main__":
    app.run()

