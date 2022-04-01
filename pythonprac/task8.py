'''

practicing all lists

'''

l=[1,2,3,4]
print(l[1])

l=[1,2,3,[4,5,7]]
print(l[3][2])

l=[1,2,3,4]
l.append([1,2])
print(l)


l=[1,2,3,4]
l.extend([1,2])
print(l)


r=l.copy()
l.append([2])
print(r)

l.clear()
print(l)

print(l.count(2))

#print(l.index(2))

# l=[1,2,3,4]
# l.insert(1,'c')
# print(l)

# l.remove(2)
# print(l)

l=[1,2,3,9,5]
l.sort(reverse=True)
print(l)


l=[1,2,3,5]
l[::-1]