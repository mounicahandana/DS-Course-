''''

SETS ARE MUTABLE BUT UNORDERED AND IT WILL NOT ALLOW DUPLICATES

LETS DO CRUD OPERATION

'''

#creating sets 

s={'name','1',2,3}
print(type(s))

#reading

for i in s:
    print(i)

#updating

s.add(7)
print(s)

s.update([10,11,12])
print(s)

#deleting

s1={2,3,4}
s1.remove(2)
s1.discard(11)
print(s1)

#set operations

s1={1,2,3,5}
s2={1,2,3,4,5}


print(s2.issuperset(s1))

print(s1.union(s2))
print(s1.intersection(s2))
print(s1.symmetric_difference(s2))

