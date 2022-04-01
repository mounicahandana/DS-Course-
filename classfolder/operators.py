

# Operators

'''

operator precedence : 

**
unary positive+x

* , /, // , %

+ , -

<< , >> 

&

^

|

== , += , -= <= >= , is , is not 

not 

and 

or


'''


'''
if
else
elif
nested if
short hand if
short hand else


'''

a= 1+6/3*5+2
print(a)


a= (3+6)/3*5+2
print(a)





if True: #condition
    print('this is true')#statement


a=1000
b=90
if a<b:
    print('this is corrst')
elif a>b: 
    print('this is elif')
else: 
    print('this is wrong')




# short hand if 

a=50
b=20
if a>b: print('a is greater than b')

#short hand if else

a=50
b=20
print('a is greter than b') if a>b else  print('a is less than b')


# #task 4 

# total operators and conditional statements practice

# #task 5 

# calculator code take operators from teh user 

# if else elif var input 

#task 6 

#practice for , while , break , continue , pass , nested for 



''''

LOOPING or iterative STATEMENTS

for
nested for 
while


pass
continue  #jumping statements
break


'''


#while loop working 

siri =100
while siri<110:
    print ('practiving')
    siri+=1
else:
    print('completed')



#for loop 

name = 'siri'
for i in name: 
    print(i)

# for loop with range 

for i in range(100,10,-2):
    print(i)


#break

name='siri'
for j in name:
    if j=='i':
        break
    else:
        print('HI')
print(j)


#continue

name='siri'
for j in name:
    if j=='i':
       continue
    else:
        print('HI')
print(j)

#pass 

'''
when we write condition and when we want to write the staetemsnt inside the condition later 
then we use pass

'''

if True: 
    pass


#nested for 

for i in range(1,1001):
    for j in range(1,11):
        print(i*j,end=' ')
    print()






