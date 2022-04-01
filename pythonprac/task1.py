'''
Calculating simple interest and compound interest 

'''

#simple interest calculation 

principalAmount = float(input('enter the principal amount'))
rate= float(input('enter the rate '))
time= float(input('enter the time'))

simpleInterest= ((principalAmount*rate*time)/100)

print('Simple Interest is',simpleInterest)

#Compound interest Calculation 

compoundInterest= principalAmount*(1+((rate/100)**time-1))

print('compound interest is',compoundInterest)