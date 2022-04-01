'''

strings are immutable and indexed and we can perform lot of operations in string


'''

s='Siri chandana '
s="siri chandana"
s='''siri chandana'''


#to find the length
s='siri'
print(len(s))

#to make the first letter capital
print(s.capitalize())

#to print the string at center 
print(s.center(9,"*"))

#to count the occurance of specific letter

print(s.count('i'))

#we can see whether the substring startswith or endswith  and it returns boolean value

siri="this is siri"
print(siri.endswith('siri'))


#format is very important we can change values according to our choice in output
print('i am testing {}'.format('siri'))

s="my name is {b} {c} {a}".format(a='kiran',b='python',c='class')
print(s)




#this is for joining lists or strings or tupless

v='*'.join(siri)
print(v)    
   #we can join list,tuple and string


#to remove the front and back spaces in a string

siri="                      this is is book is                                     "
print(len(siri))

c=siri.strip()
print(len(c))


#to make the first letter in words capital

s='Hi i am practicing'
print(s.title())


#to remove back suffix if the suffiz is not there it wil raise an erro

s="I am practicing"
print(s.removesuffix('class'))


#to replace the substring with other substring 
s='this is siri and i am practicing'
print(s.replace('t',' r',2))# (old,new,count) 


