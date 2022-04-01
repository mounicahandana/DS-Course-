'''

PRACTICING STRING OPERATIONS AND METHODS 


'''

s='Siri chandana '
s="siri chandana"
s='''siri chandana'''


s='siri'
print(len(s))

print(s.capitalize())

print(s.center(9,"*"))

print(s.count('i'))


siri="this is siri"
print(siri.endswith('siri'))


print('i am testing {}'.format('siri'))

s="my name is {b} {c} {a}".format(a='kiran',b='python',c='class')
print(s)





v='*'.join(siri)
print(v)    
   #we can join list,tuple and string



siri="                      this is is book is                                     "
print(len(siri))

c=siri.strip()
print(len(c))



s='Hi i am practicing'
print(s.title())



s="I am practicing"
print(s.removesuffix('class'))


s='this is siri and i am practicing'
print(s.replace('t',' r',2))# (old,new,count) 


