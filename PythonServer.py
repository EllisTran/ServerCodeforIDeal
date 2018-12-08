import json
import time, sys
import threading
from Threading import Threading
import socket                 # Import socket module
data = {}
soc = socket.socket()         # Create a socket object
host = "localhost"            # Get local machine name
port = 2004                   # Reserve a port for your service.
waitingforClient = True
soc.bind((host, port))        # Bind to the port
soc.listen(5)                 # Now wait for client connection.
notFound = "Sorry, ID number not found"
found = False

print("<------------------------------------------------------------------------->")
print("                     WELCOME TO ELLIS'S PYTHON SERVER                      ")
print("<------------------------------------------------------------------------->\n")

t = Threading("Waiting for connection from client", True)       #Create a new thread in the Threading class to do the ... animation

while True:
    conn, addr = soc.accept()     # Establish connection with client.
    t.stillThreading = False
    
    print ("\nGot connection from",addr,"\n")
    t = Threading("Waiting for client to send student's ID number", True)
    
    msg = conn.recv(1024)                   #Receive message from Client
    msg = msg.decode('UTF-8')               #Decode that and put it in Unicode
    msg = msg[2:]                           #Cut off the beginning of the UTF-8 message

    t.stillThreading = False

    print("\nID number received:",msg)
    with open('MOCK_DATA.json') as json_file: #Opens file as json
        print("Searching through JSON file...","\n")
        data = json.load(json_file)     #loads the information and puts it into the data list
        for p in data['people']:        #Looks through all of the people in the JSON file to see if any of the id numbers match
            if msg == (p['id']):
                    #Parses JSON file to set variables equal to the needed values
                    id = p['id']
                    firstName = p['first_name']
                    lastName = p['last_name']
                    email = p['email']
                    print('Name:\t\t' + firstName + ' ' + lastName)
                    print('University ID:\t' + msg)
                    print('Email:\t\t' + email)

                    #Encodes the variables back to UTF-8 and sends back to the client
                    id = id.encode('UTF-8')
                    conn.send(len(id).to_bytes(2, byteorder='big'))
                    conn.send(id)
                    fullName = firstName + ' ' + lastName
                    fullName = fullName.encode('UTF-8')
                    conn.send(len(fullName).to_bytes(2, byteorder= 'big'))
                    conn.send(fullName)
                    email = email.encode('UTF-8')
                    conn.send(len(email).to_bytes(2, byteorder= 'big'))
                    conn.send(email)
                    found = True

        #Error Checking
        if found == False:
            print(notFound)
            notFound = notFound.encode('UTF-8')
            conn.send(len(notFound).to_bytes(2, byteorder = 'big'))
            conn.send(notFound)
            
    break
#Closes Socket
soc.close()
print("\n<------------------------------------------------------------------------->")
print("                     ELLIS'S PYTHON SERVER SAYS GOODBYE                     ")
print("<------------------------------------------------------------------------->\n")

print("<------------------------------------------------------------------------->")
print("Created By: \tEllis Tran")
print("Date Created: \tDecemeber 2, 2018")
print("Last Edited: \tDecember 7, 2018")
print("<------------------------------------------------------------------------->")
    
 
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	