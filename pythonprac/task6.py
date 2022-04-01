'''

practicing all LOOPS

'''

#while loop 

i=int(input('Enter the number'))
while i<100:
    print('I AM WHILE LOOP')
    i+=1
else:
    print('DONE')

#for LOOP 

a=input('Enter the name')
for i in a:
    print(i,end=' ')

for i in range(1,10,4):
    print(i)


#nested for loop 


for i in range(1,10):
    for j in range(1,21):
        print(i*j,end=' ')
    print()

#break loop 

name='siri'
for j in name:
    if j=='i':
        break
    else:
        print('HI')
print(j)


#continue loop 

name='siri'
for j in name:
    if j=='i':
        continue
    else:
        print('HI')
print(j)


#pass

if True:
    pass
    
