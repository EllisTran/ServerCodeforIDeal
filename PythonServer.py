import json
names = []
data = {}
data['student'] = []
data['people'] = []

import sys
import socket           # Import socket module
soc = socket.socket()         # Create a socket object
host = "localhost" # Get local machine name
port = 2004                # Reserve a port for your service.
#serverSocket = socket(AF_INET, SOCK_STREAM)
soc.bind((host, port))       # Bind to the port
soc.listen(5)                 # Now wait for client connection.


while True:
    conn, addr = soc.accept()     # Establish connection with client.
    print ("Got connection from",addr)
    msg = conn.recv(1024)
    #print (msg)
    msg = msg.decode('UTF-8')
    print(msg)
    msg = msg[2:]
    #print("Your id number is: " + msg)
    with open('MOCK_DATA.json') as json_file: #Opens file as json
        data = json.load(json_file) #loads the information and puts it into the data list
        print(json.dumps(data, indent = 4)+ "\n")
        for p in data['people']: 
            if msg == (p['id']):
                    firstName = p['first_name']
                    lastName = p['last_name']
                    email = p['email']
                    print('Name: ' + firstName + ' ' + lastName)
                    print('University ID: ' + msg)
                    print('Email: ' + email)
                    msg = msg.encode('UTF-8')
                    conn.send(len(msg).to_bytes(2, byteorder='big'))
                    conn.send(msg)
                    fullName = firstName + ' ' + lastName
                    fullName = fullName.encode('UTF-8')
                    conn.send(len(fullName).to_bytes(2, byteorder= 'big'))
                    conn.send(fullName)
                    email = email.encode('UTF-8')
                    conn.send(len(email).to_bytes(2, byteorder= 'big'))
                    conn.send(email)
    break

soc.close()

    
 
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	