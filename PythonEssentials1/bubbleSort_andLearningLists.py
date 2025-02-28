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

newList = myList[:] # makes it so that we are able to change it later on
# if we don't add the [:] if we change the value, it'll change on both 
# my_list[start:end]

myList[0] = 69

print(myList)
print(newList)

theBestList = myList[0:3] #will only copy the values from 0 to 3 

print(theBestList)

del theBestList[0:2] 

print(theBestList)

del theBestList[:]

print(theBestList)

#toLookThroughAList

print(7 in myList)
print(7 not in myList)
print(myList)

largest = myList[0]

for i in myList[1:]:
    if i > largest:
        largest = i
print(largest)

to_find = 9
found = False
for i in range(len(myList)):
    found = myList[i] == to_find
    if found:
        break

if found:
    print("Element found at index: ", 1)
else:
    print("absent")

bets = [5,7,69,10,5,6,3,0]
hits = 0

for i in myList:
    if i in bets:
        hits +=1

print("Total de aciertos: ", hits)

nuevaLista = [0, 0, 4, 5, 10, 5, 8, 10, 4, 5, 6, 7, 8, 9]

# Contar las ocurrencias de cada número en la lista
conteo = {}
for num in nuevaLista:
    conteo[num] = conteo.get(num, 0) + 1

# Crear una nueva lista excluyendo los números que aparecen más de una vez
nuevaLista = [num for num in nuevaLista if conteo[num] == 1]

# Imprimir la lista resultante y el número de elementos únicos
print("Lista después de eliminar los valores repetidos:", nuevaLista)
print("Total de elementos únicos:", len(nuevaLista))


