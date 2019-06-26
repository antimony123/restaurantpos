from flask import Flask, render_template, request

import mysql.connector as mc

app = Flask(__name__)

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

@app.route("/inventory")
def show_inventory():
	mydb = mc.connect(host='localhost', user='webaccess', passwd='cs160mysql', database="RESMGTDB")
	cur = mydb.cursor()
	cur.execute("DESCRIBE ingredients;")
	fields = [row[0] for row in cur]
	cur.execute("SELECT * FROM ingredients;")
	data = [row for row in cur]
	return render_template('inventory.html', fields=fields, data=data)

if __name__ == "__main__":
    app.run()

