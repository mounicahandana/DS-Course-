'''
A function is a block of code which only runs when it is called.
'''

def Funcname(**a): # function defination or declaration
# #     # statements
    print('this is function',a) # function body
Funcname(name='kiran',rollno=12)#function call





# # def teja(a,b,c='pavan'):
# #     print('something',a,b,c)
# # teja(1,2)
# # teja(1,2,3)
# # teja(1,2,4)


# def outside(a):
#     print('outside',a)
#     def inside(b):
#         print('inside',b)
#     inside(20)
# outside(10)


# module collection of functions

def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    print('kiran',a%b)



#task 16

# practice all sets

#task 17

# practice all function topic


# task 18

# write a Atm program using functions (credit,debit,mini statement) 


'''

FUNCTIONS ARE VERY IMPORTANT . THEY ARE VERY IMPORTANT IT IS JUST A BLOCK OF CODE . WE CAN DO REUSABLITY OF CODE

'''

def func(a):
    print(a)
func(2)



def arb(*a):#arbitrary arguments
    print('hi',a)
arb(1,2,3)#parameters   #output - list


def karg(**a):
    print('hi',a)               #output- dictionary
karg(name='siri',rollno=000)


def deft(a=None,b='default',c='default'):
    print(a,b,c)
deft()