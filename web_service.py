import pymysql
from flask import Flask, request, jsonify 

 
app = Flask(__name__)

def db_connection():
	conn = None
	try:
		conn = pymysql.connect(host='localhost',
			                   user='root',
			                   password = "manianni0512",
			                   db='mysqldatabase',
                               )
	except pymysql.Error as e:
		print(e)
	return conn

    	
@app.route("/customer", methods=["GET"])
def customer_name():
	conn = db_connection()
	cursor = conn.cursor() 
	cursor.execute("select * from customers")
	outputs = cursor.fetchall()
	return jsonify(outputs)
	
	#conn.close()

if __name__ == "__main__" :
	app.run(debug = True)