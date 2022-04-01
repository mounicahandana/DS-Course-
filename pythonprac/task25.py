
from typing import Type


print('-------------------WELCOME TO RJ SUPER MARKET---------------------- ')
print()
print('HI CAN YOU PLEASE ENTER YOUR NAME,ADDRESS AND PHONENUMBER')
print()
name=input('ENTER YOUR NAME HERE ')
print()
add=input('ENTER YOUR ADDRESS HERE ')
print()
while True: 
    phno=input('ENTER YOUR PHONE NUMBER: ')
    try:
    
        if len(phno)!=10:
            raise ValueError('THE PHONENUMBER IS WRONG ')
        else:
            break
        
    except ValueError as ve:
         print(ve)

print('--HI {} WELCOME TO E-SUPER STORE'.format(name))

print('Availaible items with prices are')

print()

ItemsAvailaible={'SUGAR':20,'RICE':30}

a=ItemsAvailaible.items()

for i,j in a:
    print('1 kg {} cost is {} Rupees '.format(i,j))
    print()
li=[]
ind=0
q=[]
pr=[]
total=0
rpr=0
spr=0

while True:
    
    dec=input('If you like to order anything type YES or else type NO  ')


    
    if dec=='YES':

        item=input('ENTER THE ITEM NAME IN CAPITALS')
        quantity=int(input('PLEASE ENTER HOW MANY KG YOU WANT'))
        if ind==0:
            li.insert(ind,item)
            q.insert(ind,quantity)
            if item=='SUGAR':
                pr.insert(ind,(20*quantity))
            elif item=='RICE':
                pr.insert(ind,(30*quantity))
                ind=ind+1


          
        else:
     
            li.insert(ind,item)
            q.insert(ind,quantity)
            if  item=='SUGAR':
                        pr.insert(ind,(20*quantity))
            elif item=='RICE':
                        pr.insert(ind,(30*quantity))
                 

        if item=='SUGAR':
            total=(total+(20*quantity))
        elif item=='RICE':
            total=(total+(30*quantity))
        ind=ind+1

        

        
        
        
        
        
        
        #orderingItems(item,quantity,ind)
        
    elif dec=='NO':


        
        print('WE ARE GENERATING BILL FOR YOU NOW: ')
        # count=0
        # print(li)
        # print(q)
        # print(pr)
        # print(total)

        print('---------------RJY SUPERMARKET------------------------')
        print('NAME  :',name)
        print()
        print('address    :',add)
        print()
        print('phoneNumber  :',phno)
        print('\n\n\n')
        
        headings=['sno','items','quantity','price']
        for i in range(len(headings)):
            print(headings[i],end='\t')
        print('\n\n\n')
        for i in range(len(li)):
            print(i,li[i],q[i],pr[i],sep='\t')
            print()
        
        print('\n\n')
        print('THE TOTAL AMOUNT YOU HAVE TO PAY IS {} RUPEES'.format(total))
        print('\n\n')
        print('--------------------THANK YOU FOR SHOPPING WITH US--------------------------')
    


        






        
        
        break
    else:
        print('type your decision in capital letters')














  












