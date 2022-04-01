'''
Lists are sequence data structures which are very important 
list can store various data types 
list is mutable and ordered(indexed)


'''

lst=[1,2,3,4]
print(lst[2])   #accessing element in lst

lst=[2,3,4]
lst[1]=4   #modifying elemnt

lst1=[1,2,3,4,5]  #ListSlicing
lst[0:4:1]
lst[::-1]
lst[::1]

''''
Methods in list

'''

l=[1,2,3,4]
l.append([1,2])
print(l)                         #apppending like adding elements


l=[1,2,3,4]                   #extending simply adding elements
l.extend([1,2])
print(l)


r=l.copy()            #copying elemts        
l.append([2])
print(r)

l.clear()
print(l)              #removing the list

print(l.count(2))      #counting specific value

#   l=[1,2,3,4]
#   l.insert(1,'c')   #inserting value
#   print(l)

# l.remove(2)     #remove(value) it will remove only first matched value
# print(l)

l=[1,2,3,9,5]
l.sort(reverse=True)      #sorting values n the list
print(l)



l=[1,2,3,4]
res=[i**2 for i in l]  #list comprehension
print(res)

res=[i**2 for i in lst if i%2==0]
print(res)






