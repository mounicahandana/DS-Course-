'''
List methods 

'''

'''
Adding elemts in the list

'''

# lst=[1,2,3]
# lst.append(2)
# print(lst)

# lst=[1,2,3]
# lst.extend([2,3])
# print(lst)

# lst=[2,3]
# print(lst*3)

# lst=[3,4,5]
# lst.insert(2,'siri')
# print(lst)

# lst=[1,2,3]

# lst[1:1]=[4,5]    #squeezing 
# print(lst)




'''
DELETING ELLEMTS IN THE LIST 

'''

# lst=[1,2,3]
# a=lst.pop()
# print(lst)
# print(a)

# lst.clear()
# #del lst

# print(lst) 

# #del lst

# #print(lst)

# nl=[1,2,3,2,4,2]
# for i in nl:
#     nl.remove(2)   #to remove duplicate values in the list 
# print(nl)


'''
OTHER OPERATIONS

index
count
copy
sort
reverse


'''

# lst=[1,2,4]
# print(lst.index(2))

'''
to get duplicate index values

'''
# lst=[1,2,3,4,2,5,2,9,2]
# nl=[]
# temp=0
# for i in lst:
   
#     if i==2:
#         nl.append(lst.index(2,temp))
#     temp+=1
# print(nl)


l=[1,2,3,4,2]
nl=[]
for i in range(len(l)):
    if l[i]==2:
        nl.append(i)
        print(nl)


lst=[1,2,2,3]
print(lst.count(2))

l=[12,3,5]
a=l.copy()
l.append('siri')
print(a)

ml=[1,2,0,8,3]
ml.sort()
print(ml)


ml.reverse()
print(ml)

print(ml[::-1])

    



