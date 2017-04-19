import requests
import socket
import sqlite3
import re
#from flask import Flask, request, jsonify

host = ''
port = 8080
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((host, port))
sock.listen(1)

while True:
	csock, caddr = sock.accept()
	print("Connection from:" + 'caddr')
	req = csock.recv(1024)
	#print (req)
	#match = re.match('GET ^\/[/.a-zA-Z0-9-]+$', req)
	userinp = req.split()[1]
    	if userinp:
        	#userinp = match.group(1)
        	print ("url to check: " + userinp + "\n")
		con = sqlite3.connect('mydata.db')
		cur = con.cursor()
		cur.execute("SELECT boolean_rep FROM testtable WHERE url_name =?", (userinp[1:],))
		res = cur.fetchone()
		print(res[0])
		con.close()
		if res[0] =="true" :
			print("Malware found, not safe to access")
			csock.sendall("""HTTP/1.0 200 OK
			Content-Type: text/html

			<html>
			<head>
			<title>MALWARE</title>
			</head>
			<body>
			Not safe!
			</body>
			</html>
				""")
		if res[0] == "false":
			print("Safe to access")
        		csock.sendall("""HTTP/1.0 200 OK
			Content-Type: text/html

			<html>
			<head>
			<title>SAFE</title>
			</head>
			<body>
			Safe!
			</body>
			</html>
				""")
    	else:
      			# If there was no recognised command then return a 404 (page not found)
       		print "Returning 404"
       		csock.sendall("HTTP/1.0 404 Not Found\r\n")
    		csock.close()
