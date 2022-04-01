'''

METHOD OVERLOADING APPROACHES

'''

class over:
    def func(self,a='default',b='default',c='default'):
        print(a,b,c)


obj=over()
obj.func(1,2)



class over:
    def func(self,a=None,b=None,c=None):
        print(a,b,c)


obj=over()
obj.func(1,2)






