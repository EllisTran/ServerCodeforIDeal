import json
data = {}
t = []
data['student'] = []
data['people'] = []
import time, sys
import threading
import socket           # Import socket module
soc = socket.socket()         # Create a socket object
host = "localhost" # Get local machine name
port = 2004                # Reserve a port for your service.
waitingforClient = True
#serverSocket = socket(AF_INET, SOCK_STREAM)
soc.bind((host, port))       # Bind to the port
soc.listen(5)                 # Now wait for client connection.
notFound = "Sorry, ID number not found"
found = False

index = 0
global stillThreading
stillThreading = True


print("\n<------------------------------------------------------------------------->\n")

def waiting(stringWaiting, index):
    global stillThreading
    while stillThreading == True:
        x = index % 4
        dots = x *'.' + (3-x) * ' '
        sys.stdout.write("\r" + stringWaiting + dots)
        time.sleep(0.5)
        sys.stdout.flush()
        index+=1
    stillThreading = True

    

def Threading(stringWaiting):
    t
     = threading.Thread(target=waiting, args = (stringWaiting, 0))
    print(threading.active_count())
    t.start()

Threading("Waiting for connection from client")

while True:
    conn, addr = soc.accept()     # Establish connection with client.
    stillThreading = False
    index +=1
    print ("\nGot connection from",addr,"\n")
    print(threading.active_count())
    Threading("Waiting to receive ID number from client")
    print(threading.active_count())
    msg = conn.recv(1024)                   #Receive message from Client
    msg = msg.decode('UTF-8')               #Decode that and put it in Unicode
    msg = msg[2:]                           #Cut off the beginning of the UTF-8 message
    stillThreading = False

    print("\n","\nID number received:",msg)
    with open('MOCK_DATA.json') as json_file: #Opens file as json
        print("Searching through JSON file...","\n")
        data = json.load(json_file) #loads the information and puts it into the data list
        #print(json.dumps(data, indent = 4)+ "\n")
        for p in data['people']:        #Looks through all of the people in the JSON file to see if any of the id numbers match
            if msg == (p['id']):
                    #Parses JSON file to set variables equal to the needed values
                    id = p['id']
                    firstName = p['first_name']
                    lastName = p['last_name']
                    email = p['email']
                    print('Name: ' + firstName + ' ' + lastName)
                    print('University ID: ' + msg)
                    print('Email: ' + email)

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
            notFound = notFound.encode('UTF-8')
            conn.send(len(notFound).to_bytes(2, byteorder = 'big'))
            conn.send(notFound)
            print("Sorry, ID number not found")
    break
#Closes Socket
soc.close()
print(threading.active_count())
print("\n<------------------------------------------------------------------------->")
    
 
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	