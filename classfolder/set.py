# ........................ " Sets " .............................
# The elements in the set cannot be duplicates.
# The elements in the set are mutable(can be modified).
# There is no index attached to any element in a python set. 
# So they do not support any indexing or slicing operation.
# We can add or remove items from it.
# defined with {}
# A set is created by placing all the(elements)inside curly braces {},
# separated by comma , or by using the built-in set() function.



# print(suresh[0])















'''
# add
# remove
# discard
# clear
# copy
# update
'''

# suresh={1,2,3,4}
# suresh.add('kiran')
# suresh.remove(100)
# suresh.discard(100)
# suresh.update([1,2,3,4,5,6])
# print(suresh)

# d=set()
# print(type(d))


# set operations
# union
# intersection
# difference
# symmeteric diff
# disjoint 
# subset
# superset

# s1={1,2,3,5}
# s2={1,2,3,4,5}


# print(s2.issuperset(s1))

# print(s1.union(s2))
# print(s1.intersection(s2))
# print(s1.symmetric_difference(s2))







'''
Frozen sets in Python are sets that cannot be changed after creation.
In addition, they cannot contain duplicate values.
'''


# # creating a dictionary
# Student = {"name": "Ankit", "age": 21, "sex": "Male",
# 		"college": "MNNIT Allahabad", "address": "Allahabad"}

# # making keys of dictionary as frozenset
# key = frozenset(Student)

# # printing keys details
# print('The frozen set is:', key)








# # creating a list
# favourite_subject = ["OS", "DBMS", "Algo"]

# # making it frozenset type
# f_subject = frozenset(favourite_subject)

# # below line will generate error

# f_subject[1] = "Networking"




# from functions import *

# d=add(2,3)
# c=sub(2,1)
# v=mul(2,3)
# print(d,c,v)
# # div(2,4)


s={'siri',1,2,3}
l=list(s)
for i,j in enumerate(s):
    print(i,j)