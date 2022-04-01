'''
ALGORTITHM 

:

ask the user to click on 1 so that list can be shown

after that 

ask the user to add the items or not and ask him to press 1 or 2 

if press 1 add items

if press comeout

and finally ask for bil generation 

if they type yes generate the bill




'''


from datetime import datetime

name=input('Enter your name ')

listofItems='''

   sugar  : 20/kg
   boost  : 10/kg
   rice   : 50/kg
   panneer: 40/kg
   salt   : 30/kg
   dal    : 40/kg
   
'''

items={'sugar':20,
'boost':10,
'rice':50,
'panneer':40,
'salt':30,
'dal':40
}

price=0

itemList=[]
quanList=[]
priceList=[]
totalAmount=0
FinalPay=0

d=int(input('Enter the number 1 to see the list of items'))
if d==1:
    print(listofItems)

for i in range(len(items)):
    d1=int(input('If you want to buy any item click on 1 or else click on 2'))
    if d1==1:
    
        item=input('enter the item you want ')
        if item in items.keys():
            quantity=int(input('enter the quantity'))
            price=quantity*items[item]
            itemList.append(item)
            quanList.append(quantity)
            priceList.append(price)
            totalAmount=totalAmount+price
            gst=(totalAmount*5)/100
            FinalPay=totalAmount+gst

    elif d1==2:
        break
d2=input('can i generate the bill for you if you want type yes or else type no')
if d2=='yes':


    print(20*'=','SUPERMARKET',20*'=')
    print(23*' ','RAJAHMUNDRY')
    print(8*' ','SNO',8*' ','ITEMS',8*' ','QUANTITY',8*' ','PRICE')
    for i in range(len(itemList)):
        print(8*' ',i,8*' ',itemList[i],8*' ',quanList[i],8*' ',priceList[i])
    print(80*'=')
    print(8*' ',name,20*' ','DATE',20*' ',datetime.now())
    print(80*'=')
    print(10*' ','TOTAL AMOUNT',20*' ',totalAmount)
    print(80*'=')
    print(10*' ','GST',20*' ',gst)
    print(80*'=')
    print(10*' ','FINAL AMOUNT',20*' ',FinalPay)
    print()
    print(20*' ','THANK YOU',20*' ')






















