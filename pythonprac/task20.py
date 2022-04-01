'''

open close read readline readlines write writelines seek tell

'''

'''
opening files 
'''

o=open('pythonprac/st19.pdf','r')
s=o.read()
print(s)


# Print the position of handle
print(o.tell())

o.seek(0)  #change the position

print(o.tell())

o=open('pythonprac/st19.pdf',mode='r+')
s=o.read()
i=str(s)
l=i.split()
print(l)


for i in l:
    o.writelines([i])

o.close()

