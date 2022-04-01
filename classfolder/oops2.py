'''                 object oriented programming                        '''

# class(template)
'''
1.we will define class by using 'class' 
2.blue print to create a objects
3.collection of objects is called class
'''
#ex fruits


















# object
# physical entity(real)
'''
1.an instance of a class
2.memory is created when it declared
'''
#ex apple,orange,mango

























# attribute (variable) data members
'''
age=20 
color='blue'
'''






















# method(behaviour) or functions
'''
eat() 
sleep()
'''
















# self keyword
'''
we can access the attributes and methods of the class(current class only)
'''






# class Class_name:
#     #constructor
#     #attributes
#     #methods









# class Naveen:
#     a=10 #attribute
#     def display(self):
#         print(self.a)
    
# ram=Naveen()  # object declaration
# # object name . method name ()
# ram.display()


























# __init__

'''
Constructors are generally used for instantiating an object. 
The task of constructors is to initialize(assign values)
to the data members of the class when an object of the class 
is created.
In Python the __init__() method is called the constructor
and is always called when an object is created

does'nt support multiple constructor
'''



# class Naveen:
#     def __init__(self,a,b,c):
#         self.x=a
#         self.y=b
#         self.f=c
        
#     def display(self):
#         print(self.x)
    
# ram=Naveen(10,1,2)  # object declaration
# # object name . method name ()
# ram.display()




# class Mobiles:
#     def __init__(self,Name,cam,Batt,Proces,price):
#         self.c=Name
#         self.x=cam
#         self.b=Batt
#         self.p=Proces
#         self.a=price
#     def output(self):
#         print('Mobile Name:',self.c)
#         print('Mobile Camera:',self.x)
#         print('Mobile Battery:',self.b)
#         print('Mobile process:',self.p)
#         print('Mobile Price:',self.a)
# mn=input('Enter the Mobile Name:')
# mc=input('Enter the Mobile Camera:')
# mb=input('Enter the Mobile Battery:')
# mp=input('Enter the Mobile Process:')
# mpp=input('Enter the Mobile Price:')
# suresh=Mobiles(mn,mc,mb,mp,mpp)
# suresh.output()














# inheritance
# single parent child
# multiple
# multilevel
# hierar








# class Parent:
# #     def output(self):
# #         print('this is parent class')

# # class Child(Parent):
# #     def outputChild(self):
# #         print('this is child class')

# # i=Child()
# # i.output()
# # i.outputChild()





# # class Father:
# #     def output(self):
# #         print('this is parent class')
# # class Mother:
# #     def outputM(self):
# #         print('this is mother class')
# # class Child(Father,Mother):
# #     def outputChild(self):
# #         print('this is child class')      

# # ice=Child()
# # ice.output()
# # ice.outputM()
# # ice.outputChild()



# class GrandFather:
#     def output(self):
#         print('this is gf class')
# class Father(GrandFather):
#     def outputf(self):
#         print('this is father class')
# class Child(Father):
# #     def outputChild(self):
# #         print('this is child class')      
# # ice=Child()
# # ice.output()
# # ice.outputf()
# # ice.outputChild()



# class Father:#100cr
#     def output(self):
#         print('this is father class')
# class Child1(Father):#50cr
#     def outputf(self):
#         print('this is child 1 class')
# class Child2(Father):#50cr
#     def outputChild(self):
#         print('this is child  2 class')      
# ice=Child1()
# cream=Child2()
# ice.output() #child 1 of parent
# ice.outputf()
# cream.output() # child 2 of parent
# cream.outputChild() # child 2




# class Father:#100cr
#     def output(self):
#         print('this is father class')
# class Child1(Father):#50cr
# #     def outputf(self):
# #         print('this is child 1 class')
# # obj=Father()
# # obj.outputf()



# class Father:
#     def funv(self):
#         print('this is father')

# class Mother:
#     def fun(self):
#         print('this is Mother')
# class Done:
#     def fun2(self):
#         print('this is class')

# class Child(Father,Mother,Done):
#     def func(self):
#         print('this is child')
# obj=Child()
# obj.funv()
# obj.fun()
# obj.func()
# obj.fun2()
































# Polymorphism
# Encapsulation
# Data Abstraction 
# poly-many
# morph = forms
# 1.method overloading 
# 2.method overridding















# class Methodoverlod:
#     def something(self,a=None,b=None,c=None):
#         print(a,b,c)
# obj=Methodoverlod()
# obj.something(1,2,3)
# obj.something(1,2)
# obj.something(1)

# task 29
# research the different approuches to overcome the method overloading









# class Methodoverri:
#     def display(self):
#         print("this is parent class")

# class Child(Methodoverri):
#     def display(self):
#         print("this is child class")
#         super().display()
      
# obj=Child()
# obj.display()
















#encapsulation

# binding of class (methods and variables(attributes))
# public 
# and 
# private __
# protected _









# class GFather:
#     def __init__(self,a):
#         self.__y=a
# class Father(GFather):
#     def display1(self):
#         print(self.__y)
# class Child2(Father):
#     def display2(self):
#         print("child2",self.__y)

# obj=Child2(12)
# obj.display2()




















# #abstraction
# #abs method there is no body
# #abs class can not  create object
# #a class contain one or more abstract methods then it said to be a abc






from abc import ABC,abstractmethod
class Parent(ABC):
    @abstractmethod
    def done(self):
        print('hi i am abstract method')
    def func2(self):
       print('this is parent')

class Child(Parent):
    def done(self,a):
        print('this is child',a) 
obj=Child()
obj.done(10)
obj.func2()





# task 30
# total practice


# task 31
# html tags







