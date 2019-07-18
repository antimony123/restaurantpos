# restaurantpos
POS system for restaurants, with inventory tracking.

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
