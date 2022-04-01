''''
LAMBDA FUNCTIONS

'ANONYMOUS FUCNTIONS '




'''

res=lambda x : x**2
print(res(2))


'''

FILTER METHOD

it tests is each element is true or not

'''

lst=[23,1,221,0,-132]

def func(x):
    if x>2:
        return True
    else:
        return False

x=filter(func,lst)
print(tuple(x))



'''
GENERATOR FUNCTION

'''

def func():
    yield 1 
    yield 2 
    yield 3

x=func()
print(x.__next__())
print(x.__next__())
print(x.__next__())


'''
MAP FUNCTION

'''

lst=[2,3,5,10]
def func(x):
   return x+x

res=map(func,lst)
print(list(res))



'''

reduce function

'''

from functools import reduce

d=reduce(lambda a,b: a+b,[1,2,3,4])
print(d)

