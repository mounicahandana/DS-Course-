'''
TUPLE OPERATIONS

'''

'''
CREATION OF TUPLE

'''

t=(1,2,'siri',0.9)
print(t)

'''
Reading data from tuple 
'''

t=(1,2,3,4)
print(t[-2:])

'''
updating data

TUPLE IS IMMUTABLE


'''

'''
DELETING DATA 

'''

# t=(1,2,3)
#  del t
#  print(t)


'''
OTHER OPERATIONS ON TUPLE WHICH ARE BUILT IN FUNCTIONS

'''

# t=(1,2,3)
# a=t.count(2)
# print(a)

# print(t.index(2))

# t=(1,2,3,4,2)
# for i in range(len(t)):
#     if t[i]==2:                     #to print index of tuple 
#         print(i)  


# t=(1,2,3)
# print(max(t))
# print(min(t))
# print(sum(t))


t=(1,2,3)
t1=(4,5,6)
# print(t+t1)
# print(t*2)
#a=()
l=[]
for i in range(len(t)):
    a=t[i]+t1[i]
    l.append(a)
  
print(tuple(l))





