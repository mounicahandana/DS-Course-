''''
pattern 1

'''


for i in range(5):
    for j in range(5):
        print('*',end=' ')
    print()


'''
pattern 2
'''

for i in range(1,6):
    for j in range(5):
        print(i,end=' ')
    print()


'''
pattern 3

'''

for i in range(1,6):
    for j in range(1,i+1):
        print(i, end=' ')
    print()

'''
pattern 4

'''


for i in range(5):
    for j in range(i+1,6):
      
        print('*',end=' ')
    print()


'''
pattern 5

'''


for i in range(1, 6):

    for j in range(6, 0, -1):

        if j > i:

            print(' ', end=' ')

        else:

            print('*', end=' ')

    print()

'''
pattern 6

'''





m = (2 * 6) - 2

for i in range(0, 6):

    for j in range(0, m):

        print(end=' ')

    m = m - 1 # decrementing m after each loop

    for j in range(0, i + 1):

        # printing full Triangle pyramid using stars

        print('*', end=' ')

    print(' ')
