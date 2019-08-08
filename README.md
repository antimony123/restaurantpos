# restaurantpos
POS system for restaurants and small businesses, with inventory tracking and profit reporting.

### Requirements

In order to install restaurantpos, you must already have or install the following:

mysql server
python 3.5 or greater
pip for python 3

pip installations:
pip install flask
pip install mysql
pip install mysql-client
pip install pymysql
pip install sqlalchemy
pip install bcrypt

### Creating the database

Log in to your mysql server.
Create a new database called RESMGTDB:
```
create database RESMGTDB;
```
Create a new user, webaccess, with permissions to modify RESMGTDB:
```
use mysql;
CREATE USER 'webaccess'@'localhost' IDENTIFIED BY 'cs160mysql';
GRANT ALL PRIVILEGES ON RESMGTDB.* TO 'webaccess'@'localhost';
```

Now you have the necessary setup to run the application.

### Running the app locally

In a terminal, run the following:

cd /path/to/restaurantpos
export FLASK_APP=rpos
flask run                   # this will run it on localhost:5000

------------------------------

In case you need to import or export your database from the cloud server, the following sections describe how to do so.

### How to import the database
Assumptions made before running the commands:
- mysql server is installed and running on your computer locally
- a user called webaccess has been created on said mysql server
- a database called RESMGTDB has been created yet on said mysql server
- res.sql is a file in your current directory containing all the RESMGTDB content

Run the following command:
```
mysql -u webaccess -p RESMGTDB < res.sql
```
This will import res.sql into your mysql server. To verify success, from within the mysql prompt, run
```
SHOW TABLES;
```
If your output matches the following output, you have successfully imported the db.
```
+--------------------+
| Tables_in_RESMGTDB |
+--------------------+
| ingredients        |
| menu               |
| order_details      |
| order_temp         |
| orders             |
| recipes            |
| users              |
+--------------------+
```


### How to export the database
Run the following commands in the server terminal:
```
mysqldump -u webaccess -p RESMGTDB > res.sql
```
This will dump the contents of the RESMGTDB database into a file called res.sql in your home directory on the server.
```
cd [directory of choice]
scp [username]@alphacs160.eastus2.cloudapp.azure.com:res.sql .
```
This will copy res.sql from the server to your local directory of choice.
Now you may import the database; see above: How to export the database.
