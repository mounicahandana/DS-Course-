# # def add(a):
# #     """this is used to print"""
# #     print(a)
# # add(2)
# # print(print.__doc__)

# # a=2;b=5;c=4
# # print(a,b,c,end='*')




# # class Mobile:
# #     def __init__(self,name,camera):   #constructor is used to initialize the variables
# #         self.a=name
# #         self.b=camera

# #     def Output(self):
# #         print('name',self.a)
# #         print('camera',self.b)

# # obj=Mobile('opppo','20000mp')
# # obj.Output()



# # from re import L


# # l=['de','def','fefefe'] 
# # for i in l:


# from concurrent.futures import thread
# from threading import *

# class oioir(Thread):
#     def func(self):
#         print('hello')

# j=oioir()
# j.start()


# from abc import ABC,abstractmethod
# class Parent(ABC):
#     @abstractmethod
#     def fun(self):
#         pass
#     def func(self):
#         print('hello')

# class Co(Parent):
#     def func1(self):
#         print('hi')

# l=Co()



# def table(n):
#     for i in range(1,11):
#         yield n*i
      

# for i in table(15):
#     print(i)

# lst=[1,2,3,4]
# df=list(map(lambda x : x**2,lst))
# print(df)

# from threading import Thread
# from time import sleep


# class c1(Thread):
#     def func(self):
#         print('HELLO')
# class c2(Thread):
#     def func2(self):
#         print('HIIIIII')

# o=c1()
# o.start()


# import sys
# print(sys.version)

# import keyword
# print(len(keyword.kwlist))

# from re import T


# print(r"hello\bsiri")   #raw 
 

# print(print.__doc__)

# for i in range(10):
#     print(i)

# print('hi i am {q} hw can i {p} u'.format(p='siri',q='help'))


# a=2.9786785767
# b=3.87577667757
# print('his rank is {:.2f} and {:.3f}'.format(a,b))

# from math import pi
# print(pi)

# a=2
# a='helo'
# print(a)


# a='siri'
# '''
# we use + to concotenate variabel and string 
# '''
# print('hello welcome to  {} I luiek u '.format(a))


# from numpy import inner


# def gr(*a):
#     for i in a:
#         print(i)

# lst=[1,2,3]
# gr(1,2,3)


# do=lambda x:(x*2)
# print(do(79)))




'''
LAMBDA FUNCTIONS

'''

# res=lambda a,b,c:a+b+c
# print(res(2,3,4))


# def add(l):
#     sum=0
#     return l*2
# lst=[1,2,3]
# res=map(add,lst)
# print(list(res))



# y=2
# print('hi i am siri{} how may i help you '.format(y))

'''

STANDARD MODULES - https://docs.python.org/3/py-modindex.html

'''

# import s4
# # print(dir(s4))
# print(s4.__name__)

# lst=[1,2,3]
# l=[2,3,6]
# print([i*2 for i in lst if i in l])


# import decimal
# print(decimal.Decimal(2.3)+decimal.Decimal(2.5))

# print(2.3+2.5)

# import fractions
# print(fractions.Fraction(2,3))
# print(fractions.Fraction('2.5'))

# import random
# print(random.randrange(2,6))

# lst=[1,2,3,5,7]
# print(lst[::-2])


# d={1:'siri'}
# d.clear()
# print(d)

# print('|{:>20}'.format('bread'))

# print('{:^12.3}'.format('siri'))

s='siri'
# print(s.lower())
# print(s.upper())
# print(s.capitalize())
# print(s.center(20,'*'))
# print(s.count('i'))
# print(s.startswith('si'))
# print(s.endswith('t'))
# print(s.upper())




# print('{:^10}{:^10}{:^10}'.format('hi','siri','how r u'))
# print('{:*^10}'.format('cat'))


# s='siri'
# print(s.center(10,'*'))



# f=open('geekprac/demo.txt','w')
# f.write("my first file\n")
# f.write("This file\n")
# f.write("contains three lines")
# f1=open('geekprac/demo.txt','r')
# r=f1.read()
# r2=f1.read()
# for i in r:
#     print(i,end='')






# print(r)
# print(r2)

# print(f1.tell())
# f1.seek(0)
# print(f1.read())

# print(f1.readline())

# print(f1.readlines())

# f1=open('geekprac/demo.txt','w')
# l2=['jbfoie\n','kjehfoi']
# for i in l2:
#     f1.writelines([i])


# import sys
# try:

#   a=1/0


# except Exception as e:

#     print(e.__class__)


# # define Python user-defined exceptions
# class Error(Exception):
#     """Base class for other exceptions"""
#     pass


# class ValueTooSmallError(Error):
#     """Raised when the input value is too small"""
#     pass


# class ValueTooLargeError(Error):
#     """Raised when the input value is too large"""
#     pass


# # you need to guess this number
# number = 10

# # user guesses a number until he/she gets it right
# while True:
#     try:
#         i_num = int(input("Enter a number: "))
#         if i_num < number:
#             raise ValueTooSmallError('This value is too small, try again!')
#         elif i_num > number:
#             raise ValueTooLargeError
#         break
#     except ValueTooSmallError as ve:
#         print(ve)
#         print()
#     except ValueTooLargeError:
#         print("This value is too large, try again!")
#         print()

# print("Congratulations! You guessed it correctly.")




# s="siri"
# print(s.isalnum())


# l=['milk','sugar','salt']
# print('   '.join(l))

# si=2.3445
# print('{:.2f}'.format(si))

# import datetime

# d=datetime.time(2,30,12)
# print(d)

# import re

# s='siri@gmail.com diuefibe senthil245@gmail.com'

# a=re.findall('\w+@gmail.com',s)3
# print(a)



# def gen():
#     a=2
#     yield a
#     a=a+1
#     yield a

# for i in gen():
#     print(i)


# # A simple generator function
# def my_gen():
#     n = 1
#     print('This is printed first')
#     # Generator function contains yield statements
#     yield n

#     n += 1
#     print('This is printed second')
#     yield n

#     n += 1
#     print('This is printed at last')
#     yield n
    
# a=my_gen()
# next(a)


# def smart_divide(func):
#     def inner(a, b):
#         print("I am going to divide", a, "and", b)
#         if b == 0:
#             print("Whoops! cannot divide")
            

#         return func(a, b)
#     return inner


# @smart_divide
# def divide(a, b):
#     print(a/b)

# divide(2,3)



# def make_pretty(func):
#     def inner():
#         print("I got decorated")
#         return func()
#     return inner

# @make_pretty
# def ordinary():
#     print("I am ordinary")

# ordinary()


# s='     siri /wduiwhi|  '
# r=s.lstrip(' ')
# d=r.strip(' ')
# print(d)

# a=[1,2,3]
# b=[5,6,7]

# c=zip(a,b)
# print(dict(c))

# import pdb
# def func(n):
#     for i in range(n):
#         pdb.set_trace()
#         print(i)
    

# func(5)

# l=[1,2,3]
# r=[3,4,5]
# re=[]
# for i,j in zip(l,r):
#     re.append(i*j)

# print(re)


# import os
# os.chdir('C:\\Users\\SIRI\\Desktop\\FULL STACK DATA SCIENCE\\geekprac')


# import os
# # print(os.getcwd())
# os.chdir('C:\\Users\\SIRI\\Desktop\\FULL STACK DATA SCIENCE\\geekprac')


# l1=[1,2,3]
# l2=[3,4,5]
# a=zip(l1,l2)
# for i,j in a:
#     print(i+j)


