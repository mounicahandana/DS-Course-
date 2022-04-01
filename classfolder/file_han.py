'''
File handling in simple it means handling of files such as opening the file, reading, writing,
and many other operations.
'''

'''
open
read or write
close

'''









'''
modes

read    r
write   w
append  a
r+      read and write 
'''


# vijay=open('file_error/demo.txt','r') # file read open
# content=vijay.read()
# print(content)
# vijay.close()






# vijay=open('file_error/demo.txt','w') # file read open
# content=vijay.write('this is write function')
# vijay.close()



# vijay=open('file_error/demo.txt','r+') # file read open
# d=vijay.read()
# print(d)
# content=vijay.write('this is function')
# vijay.close()









'''
tell() method can be used to get the position of File Handle. 
tell() method returns current position of file object.
This method takes no parameters and returns an integer value. 
'''







# Python program to demonstrate
# tell() method


# Open the file in read mode
# fp = open('file_error/demo.txt', "r")

# # Print the position of handle
# print(fp.tell())

# #Closing file
# fp.close()





# # Python program to demonstrate
# # tell() method

# Opening file
# fp = open('file_error/demo.txt', "r")
# fp.read(8)

# # Print the position of handle
# print(fp.tell())

# # Closing file
# fp.close()

# f=open('classfolder/demo.txt','r')
# l=f.readlines(5)
# print(l)                                    #read the lines and convert it into list if the text is in next line in file it is second elem in list






 
'''
seek() function is used to change the position of the File Handle to a given specific position. 
File handle is like a cursor, which defines from where the data has to be read or written in the file. 
'''

'''
f.seek(0)	
Move file pointer to the beginning of a File
'''

# # Opening file
# fp = open('file_error/demo.txt', "r")
# fp.read(8)

# # Print the position of handle
# print(fp.tell())  # 8
# fp.seek(0)
# print(fp.tell())  #  0

# # Closing file
# fp.close()











file=open('classfolder/demo.txt',mode='r+') # open
content=file.read() # operation
v=str(content)
print(v)
# file.write('hi i am moni')
# content=file.read()
# print(content)
f=v.split()
print(f)
# f.insert(2,'chetan')
# print(file.tell())
# file.close()

file=open('classfolder/demo.txt',mode='w')
for i in f:
    file.writelines([i])


# task 19

'''
pdf,xl,csv,docx  read and write all files


'''
# task 20
'''
open close read readline readlines write writelines seek tell
'''

# task 21
'''
os module

'''

# task 22
'''
try except finally else raise
'''


# task 23
'''
date and time module python

'''


# task 24
'''
for with exception handling,and for with file handling
'''


# task 25
'''
super market bill genration
'''
'''''''''''''''''''''''''''''''''''''''
            kiran super market
name:
addresss:
phno:

sno              items      quantity       price
1                 sugar        1            10
2                 salt         2            20


                                     total  30
                 visit again

'''''''''''''''''''''''''''''''''''''''''''''''


'''
1.input name
2.wish 
3.set of items price  sugar 10 
4.item select
5.quantity  10*2=20
6.ask for another item
7.quantity  10*2=20
8.bill generate




'''

# function based programming ( core python )







# object based programming