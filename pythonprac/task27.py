'''
ALGORITHM : 

NUMBER GUESSING 

u will have three number with ou 

u have to ask user 

if the number givn by user is same 

thn sa congrats

or else give 2 more cchances

HAVE TO USE FUNCTION


'''

def numberGuessing(a):
    lst=[21,31,41]
    if a in lst:
        return True
    else:
        return False
    

print('WELCOME TO NUMBER GUESSING GAME')
for i in range(1,4):

    mnum=int(input('enter a number between 0 and 50 REMEMBER you have only 3 chances left'))
    bool=numberGuessing(mnum)
    if bool==True:
        print('CONGRATULATIONS YOUR GUESS IS RIGHT')
        break
    else:
        print('OOPS! YOU HAVE {} CHANCES LEFT'.format(3-i))


