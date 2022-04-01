num1=int(input('Enter the number1'))
num2=int(input('Enter the number2'))

while (num1>0 and num2>0):
    op=input('Enter the operator')

    if op=='+':
        print(num1+num2)
    elif op=='-':
        print(num1-num2)
    elif op=='/':
        print(num1/num2)
    elif op=='//':
        print(num1//num2)
    elif op=='*':
        print(num1*num2)
    elif op=='**':
        print(num1**num2)
    else: 
       print('INVALID OPERATOR ')
       


