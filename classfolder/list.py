'''
1.A list in Python is used to store the sequence of various types of data. 
2.Python lists are mutable type.
3.we can modify its element after it created. 
4.Items in the list are separated with the comma (,) 
and enclosed with the square brackets [].
5.List in Python are ordered. 
6.The elements in a list are indexed according to a definite sequence and the indexing ,
of a list is done with 0 being the first index. 
7.which allows duplicating of elements
'''

sampath=[1,2.2,'kiran',True] # declare
# print(sampath[2])
# sampath[2]='deepak'
# print(sampath)
# print(sampath[-1])

# sampath=[1,2.2,'kiran',True,1,2,3,4,5,6,7,8]
# print(sampath[:-1]) 

'''
whenever they take negetive values starting value should be lower and ending value should be higher 

if u give step then its okay 




'''


# l=[1,2,3,4,[1,2,3,4]]
# print(l[4][3])
 

# list methods


'''
append
extend
+
insert
remove
clear
pop
sort
reverse
count
copy
index

'''


# swamy.append(['raju',1,2,4,5])  
# #d=swamy.append(['raju',1,2,4,5])
#  print(d)#cant print
# print(swamy)
# swamy.extend(['raju',1,2,4,5])
# print(swamy)

# s=swamy.copy()  #try by removing copy() #if you keep copy() then it is immutable 
# swamy.append(['raju',1,2,4,5])
# print(s)

# swamy.clear()

# print(swamy.count(3))
# print(swamy.index(2))#index(element)

# list=[1,2,3,4,5,6,7,8,'vamsi']
# for i in list:
#     if i==list.index(2):
#         print(i)
# swamy=[2,1,2,3,4,5,9,7,8]
# print(swamy.index(9))   
# swamy=[2,1,2,3,4,5,9,7,8]
# swamy.insert(0,'kiran')#insert(index,new element)
swamy=[2,1,2,3,4,5,9,7,8]
# swamy.pop(0)
# swamy.remove(2)
# print(swamy)
# swamy.reverse()
swamy.sort(reverse=True)
print(swamy)


l=[1,2,3]
a=l.copy()
l.append(3)
print(a)




# list = ["EVEN" if i % 2 == 0 else 'odd' for i in range(10)]
# print(list)


# newlist = []

# for x in ["apple", "banana", "cherry", "kiwi", "mango"]:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)



# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# newlist = [x for x in fruits if "a" in x]
# print(newlist)


