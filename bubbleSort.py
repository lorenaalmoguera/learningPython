myList = [20,5,3,8,20,11]

i = 0

print(myList)
flag = True
while flag:
    flag = False
    for i in range(len(myList) -1 ):
        if myList[i] > myList[i+1]:
            flag = True
            myList[i] , myList[i+1] = myList[i+1] , myList[i]

print(myList)

myList = [20,5,3,8,20,11]
print()
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
