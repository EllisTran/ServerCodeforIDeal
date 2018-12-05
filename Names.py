import json
names = []
data = {}
data['student'] = []
data['people'] = []

'''

The code in the comments are How to add things to an array list in python then turn it into a JSON format file

data['student'].append({
    'name': 'Ellis Tran',
    'id': '010743018',
    'email': 'ektran@uark.edu'	
})

data['people'].append({
    'name': 'John Magness',
    'id': '010795668',
    'email': 'jmagness@uark.edu'
})

data['people'].append({
    'name': 'Andrew Mclellan',
    'id': '010817558',
    'email': 'agmclell@uark.edu'
})

data['people'].append({
    'name': 'Patrick Dougherty',
    'id': '010770857',
    'email': 'pdougherty@uark.edu'
})

with open('MOCK_DATA.txt', 'w') as outfile:  #Opens file
   json.dump(data, outfile) #dumps the data into json format

'''
   
insert_idNumber = input("What is your id number?: ") #This is how you do user input in Python
print()

#

with open('MOCK_DATA.json') as json_file: #Opens file as json
   data = json.load(json_file) #loads the information and puts it into the data list
   for p in data['people']: 
      if insert_idNumber == (p['id']):
         print(('Name: ' + p['first_name'] + ' ' + p['last_name']))
         print('University ID: ' + p['id'])
         print('Email: ' + p['email'])
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 
		 