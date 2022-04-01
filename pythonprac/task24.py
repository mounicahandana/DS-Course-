'''
for with exception handling,and for with file handling

'''

o=open('pythonprac/st19.pdf',mode='r+')
s=o.read()
i=str(s)
l=i.split()
print(l)


for i in l:
    o.writelines([i])

import sys

randomList = ['siri',3,2]

for entry in randomList:
    try:
        print("The entry is", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of", entry, "is", r)