'''
TOTAL PRACTICE 

POLYMORPHISM

INHERITANCE

DATA ABSTRACTION

ENCAPSULATION


'''

#polymorphism

#method overloading

# class mover:
#     def func(self,a=None,b=None):
#         print(a,b)
# obj=mover()
# obj.func(23,25)

#method overriding


# class Parent:
#     def func(self,a,b):
#         print(a,b)
    
# class Child(Parent):
#     def func(self,c,d):
#         print(c,d)
#         super().func(4,5)

# obj=Child()
# obj.func(23,24)


#inheritance

'''
SINGLE INHERITANCE
'''

# class Parent:
#     def func(self,a,b):
#         print(a,b)

# class Child(Parent):
#     def func1(self,c,d):
#         print(c,d)

# obj=Child()
# obj.func1(10,111)
# obj.func(19,189)


'''

MULTILEVEL INHERITANCE

'''

# class Parent:
#     def func(self,a,b):
#         print(a,b)

# class Child(Parent):
#     def func1(self,c,d):
#         print(c,d)

# class Grandchild(Child):
#     def func2(self,g,h):
#         print(g,h)

# obj=Grandchild()
# obj.func1(10,111)
# obj.func(19,189)
# obj.func2(23,34)

'''
MULTIPLE INHERITANCE 

'''

# class Parent:
#     def func(self,a,b):
#         print(a,b)

# class Mother:
#     def func1(self,c,d):
#         print(c,d)

# class Child(Parent,Mother):
#     def func2(self,g,h):
#         print(g,h)

# obj=Child()
# obj.func1(10,111)
# obj.func(19,189)
# obj.func2(23,34)

'''
HEIRARCHY

'''


# class Parent:
#     def func(self,a,b):
#         print(a,b)

# class Child1(Parent):
#     def func1(self,c,d):
#         print(c,d)

# class Child(Parent):
#     def func2(self,g,h):
#         print(g,h)

# obj=Child()
# obj1=Child1()
# obj.func2(10,111)
# obj.func(23,34)
# obj1.func(19,189)
# obj1.func1(10,111)



'''
DATA ABSTRACTION

'''

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

'''
public,private and protect

'''

class pub:
    def func(self,a):
        self._y=a
class chill(pub):
    def func1(self,b):
        self._z=b

        print(self._y)
o=chill()
o.func(11)
o.func1(10)

#private

# class pub:
#     def func(self,a):
#         self.__y=a
# class chill(pub):
#     def func1(self,b):
#         self.__z=b

#         print(self.__y)
# o=chill()
# o.func(11)
# o.func1(10)




'''
CONSTRCTORS R USED TO INITIALOZE VARIABLES

'''

class con:
    def __init__(self,a,b,c):
        self.x=a
        self.o=b
        self.z=c
    def func(self):
        print(self.x,self.o,self.z)
o=con(2,3,4)
o.func()
        
















