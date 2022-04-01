'''

PYTHON PROGRAM FOR ATM USING FUNCTIONS


'''


from st18 import *
s=5000
while s>=0:
    #print(type(s))
    d=int(input('ENTER 1 FOR CREDIT,ENTER 2 FOR DEBIT OR ENTER 3 FOR CHECKING BALANCE'))
    if d==1:
        c=int(input('enter the amount u wnt to credit'))
        s=Credit(s,c)
        print(s)
    if d==2:
        deb=int(input('enter the amount u wnt to debit'))
        s=Debit(s,deb)
        print(s)
    if d==3:
        print('Balance Amount is {} Rupees'.format(s))
if s<0:
    print('BALANCE IS NULL')


    

