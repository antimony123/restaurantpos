from flask import Flask, render_template, request

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

if __name__ == "__main__":
    app.run()

