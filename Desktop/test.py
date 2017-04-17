import requests
import socket
import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/<content>', methods = ['GET'])
def checkfunction(content):
	con = sqlite3.connect('mydata.db')
	cur = con.cursor()
	cur.execute("select boolean_rep from testtable where url_name =?", (content,))
	if cur.fetchone()[0] == "true":
		return("Malware found, not safe to access")
	else:
		return("Safe to access")

@app.errorhandler(404)
def not_found(error=None):
    message = {
            'status': 404,
            'message': 'Not Found: ' + request.url,
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp

if __name__ == '__main__':
	port =8080
	app.debug = "true"
	app.run(host = '0.0.0.0', port=port)
																																																																																																																																																													
