'''
practicing usage of print function, variables ,comments, datatypes and type conversions 

'''

# print function 

print('My name is siri')

a=10
print('variable is',a)

a=int(input('enter a number'))
print(a)

#variables 

a=10
print(a)

a=c=d=10
print(d)

a,b=10,20
print(a,b)


#comments 

#This is single line comment 

'''
hi 
I 
am
Multiline
Comment

'''

#DataTypes

a=2
print(type(a))

a=2.3
print(type(a))

a='siri'
print(type(a))

a=True
print(type(a))

com= 1+2j
print(type(com))


#TypeConversions
 
a=2          #implicit conversion        
b=float(2)
print(b)

a=2.9
b=int(a)     #explicit conversion
print(b)

a=2
b=complex(a)
print(b)

a=2.8
b=complex(a)
print(b)

a=0
c=bool(a)
print(c)

a=0.0
d=bool(a)
print(d)

a=8
b=str(a)
print(b)

a=8.9
b=str(a)
print(b)

s='siri'
a=bool(s)
print(a)

s=''
a=bool(s)
print(a)









