
# '''
#       MAXIMUM OF TWO NUMBERS

# '''

# a= int(input('enter first number'))
# b= int(input('enter secoind number'))
# if a>b:
#     print(a)
# else:
#     print(b)


# l=[1,2,3,4,5,7]
# print(l[-1::-1])

# l=[2,4,2,6,7,8]
# newl=[]
# for i in l:
#     if i==2:
#         newl.append(l.index(i))

# print(newl)

# lis=['EVEN' if (i%2==0) else 'ODD' for i in range(10)]
# print(lis)

# for i in range(1,2):
#     print(i)



# lst=[2,1,2,3,4,5]
# nl=[]
# for i in lst:
#     if i==2:
#         print(nl.append(lst.index(i)))
#         lst[i]='c'

# print(nl)

# import sys
# s=2.879
# a=sys.getsizeof(s)
# print(a)


# ls1=['siri']
# print(ls1*2)


# l=[1,2,3]
# l[1:1]=[5,6]
# print(l)

# l=[1,2,3,4,56]
# print(l[1:-1])


# s=''

# s='siri'
# l=list(s)
# print(l[::-1])

# s='siri chandana'
# print('xm' in s)

# s='siri'
# print(list(enumerate(s)))

# a=1
# print('siri is {b} {b} {c}'.format(a='siri',b='gg',c='dd'))

# s='thisissiri'
# l=list(enumerate(s))
# print(l)

# sentence = 'Python programming is fun.'
# print(sentence.index('g is', 10, -4))

# l=[1,2,3,4,2]
# print(l.index(2,1,5))

# s='py phonp'
# print(s.index('p',3,4))

# s='siri'
# print(s.center(9,'*'))

# s='siri'
# print(s.startswith('s'))

# s='this is siri'
# print(list(enumerate(s)))

# l=[1,2,3,4,2]
# nl=[]
# for i in range(len(l)):
#     if l[i]==2:
#         nl.append(i)
#         print(nl)


# s='hi this is siri'
# print(s.index('z'))


# This loop will go on until the budget is integer or float
while True:
	try:
		bg = float(input("Enter your budget : "))
		# if budget is integer or float it will be stored
		# temporarily in variable 's'
		s = bg
	except ValueError:
		print("PRINT NUMBER AS A AMOUNT")
		continue
	else:
		break

# dictionary to store product("name"), quantity("quant"),
# price("price") with empty list as their values
a ={"name":[], "quant":[], "price":[]}

# converting dictionary to list for further updation
b = list(a.values())

# variable na value of "name" from dictionary 'a'
na = b[0]

# variable qu value of "quant" from dictionary 'a'
qu = b[1]

# variable pr value of "price" from dictionary 'a'
pr = b[2]

# This loop terminates when user select 2.EXIT option when asked
# in try it will ask user for an option as an integer (1 or 2)
# if correct then proceed else continue asking options
while True:
	try:
		ch = int(input("1.ADD\n2.EXIT\nEnter your choice : "))
	except ValueError:
		print("\nERROR: Choose only digits from the given option")
		continue
	else:
		# check the budget is greater than zero and option selected
		# by user is 1 i.e. to add an item
		if ch == 1 and s>0:	

			# input products name			
			pn = input("Enter product name : ")
			# input quantity of product
			q = input("Enter quantity : ")
			# input price of the product
			p = float(input("Enter price of the product : "))

			if p>s:
				# checks if price is less than budget
				print("\nCAN, T BUT THE PRODUCT")
				continue

			else:
				# checks if product name already in list
				if pn in na:
					# find the index of that product
					ind = na.index(pn)

					# remove quantity from "quant" index of the product
					qu.remove(qu[ind])

					# remove price from "price" index of the product
					pr.remove(pr[ind])

					# insert new value given by user earlier
					qu.insert(ind, q)

					# insert new value given by user earlier
					pr.insert(ind, p)

					# subtracting the price from the budget and assign
					# it to 's' sum(pr) is because pr = [100, 200] if
					# budget is 500 then s = bg-sum(pr) = 200
					# after updating for same product at index 0 let
					# pr = [200, 200] so s = 100
					s = bg-sum(pr)

					print("\namount left", s)
				else:
					# append value of in "name", "quantity", "price"
					na.append(pn)

					# as na = b[0] it will append all the value in the
					# list eg: "name":["rice"]
					qu.append(q)

					# same for quantity and price
					pr.append(p)

					# after appending new value the sum in price
					# as to be calculated
					s = bg-sum(pr)

					print("\namount left", s)

		# if budget goes zero print "NO BUDGET"
		elif s<= 0:
			print("\nNO BUDGET")
		else:
			break

# will print amount left in variable 's'
print("\nAmount left : Rs.", s)

# if the amount left equals to any amount in price list
if s in pr:
	# then printing the name of the product which can buy
	print("\nAmount left can buy you a", na[pr.index(s)])

print("\n\n\nGROCERY LIST")

# print final grocery list
for i in range(len(na)):
	print(na[i], qu[i], pr[i])


	'''
	shopping list code : https://gist.github.com/richardbwest/d0365ebb89e89e7290e7cdb9cbc95530
	
	'''
