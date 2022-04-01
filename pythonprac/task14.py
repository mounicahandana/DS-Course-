'''
DICTIONARY DOCUMENTATION 

DICTIONARY Datatype is unordered and the values can be accesses using key values 

lets see CRUD Operations
'''

#CREATE OPERATION

d={'1':'siri','2':'chandana'}
print(d)

#READING DATA FROM DICT

print(d['1'])

print(d.get('1'))

print(d.values())

print(d.keys())

print(d.items())

for i,j in d.items():
    print(i,j)

#updating 

d.update({'address':'newyork'})
print(d)

#deleting

d.pop('address')
print(d)

d.clear()
print(d)


#nested dictionary

d=  {
     'name':'siri',
     'address': {'street':'jk'}
    } 

print(d['address']['street'])