'''
pdf,xl,csv,docx  read and write all files

'''

siri=open('pythonprac/st19.pdf','r')
r=siri.read()
print(r)
siri.close()

siri=open('pythonprac/st19.pdf','w')
siri.write('hihihihihi')

siri=open('pythonprac/st191.xl','r')
r=siri.read()
print(r)
siri.close()

siri=open('pythonprac/st191.xl','w')
siri.write('hihihihihi')

siri=open('pythonprac/st192.csv','r')
helloo=siri.read()
print(helloo)
siri.close()


siri=open('pythonprac/st192.csv','w')
siri.write('i am writing ')


siri=open('pythonprac/st193.docx','r')
hi=siri.read()
print(hi)


siri=open('pythonprac/st193.docx','w')
siri.write('HI I AM WRITING IN THIS DOCUMENT FILE ')


