'''

FUNCTIONS ARE VERY IMPORTANT . THEY ARE VERY IMPORTANT IT IS JUST A BLOCK OF CODE . WE CAN DO REUSABLITY OF CODE

'''

def func(a):
    print(a)
func(2)



def arb(*a):#arbitrary arguments
    print('hi',a)
# l=[1,2,3]
arb(1,2,3)#parameters   #output - list


def karg(**a):
    print('hi',a)               #output- dictionary
karg(name='siri',rollno=000)


def deft(a,b,c='default'):
    print(a,b,c)
deft(1,2,7)


#module - collection of fucntions

def hihi(a):
    print('hihi')
    def hihihi(b):
        print(b)            #nested functions
    hihihi(2)
    
hihi(10)