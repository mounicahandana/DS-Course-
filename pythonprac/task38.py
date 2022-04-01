'''
PRACTICING DEBUGGING

'''


def addition(*x):
    temp=0
    for i in range(len(x)):
        temp=temp+x[i]
        
    return temp

lst=[1,2,3]
add=addition(1,2,3)
print(add)

