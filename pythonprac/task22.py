'''
try except finally else raise

'''


try:
    a=1/0
except:
    print('error')
else:
    print('no error')
finally:
    print('it will print whether there is error ot not')


s='siri'
try:
    number=int(s) # risky code 
    raise ValueError
except ValueError:
    print('string canot convert into int')