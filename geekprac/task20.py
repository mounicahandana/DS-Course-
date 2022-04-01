'''
file handling in simple it means handling of files such as opening the file, reading,writing 
and many other operations
'''

# file modes
'''
read
write
apeend
r+   (read and write)
'''

# sam=open('demo.txt','r')
# content=sam.read()
# print(content)
# sam.close()# output is I love my family

# sam=open('demo.txt','w')
# content=sam.write('ilove my love also')
# sam.close() # output will be replaced in demo.txt file

# sam=open('demo.txt','a')
# content=sam.write('i love my love also')
# sam.close # output will be join to old file

# sam=open('demo.txt','r+')
# s=sam.read()
# print(s)
# k=sam.write('me in alone')
# sam.close() #output is read and write


# when files having more then one line we write readlines
# sam=open('demo.txt','r')
# s=sam.readlines()
# print(s)
# sam.close #in this readlines formula the output will be convert into list type and each line will be one element

'''
tell() method can be used to get the postion of file handle.
tell() method returns current position of the file object.
this method takes no parameters and returns an integer value.

'''

# sam=open('demo.txt','r')
# s=sam.read(10)
# print(sam.tell())
# sam.close() # it will be tell the courser position of the file.


'''
seek() function is used to change the position of the file handle to give a specific position.
file handle is like curser,which defines from where the file handle is like a courser,which defines from where the data to be read or eritten in the file

'''

'''
f.seek(0)
move file pointer to the begining of a file.
'''
# sam=open('demo.txt','r')
# s=sam.read(10)
# print(sam.tell())
# sam.seek(20)     # it changes the current courser position of the file
# print(sam.tell())
# sam.close()

# sam=open('demo.txt','r+')
# s=sam.read()
# f=str(s)
# print(f)
# k=f.split()
# print(k)
# k.insert(2,'asp')
# sam.close()

# sam=open('demo.txt','w')
# for i in k:
#     sam.writelines([i])




