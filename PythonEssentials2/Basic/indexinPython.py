str = 'My string'

#este bucle añade un espacio entre cada carácter
for ix in range(len(str)):
    print(str[ix], end= ' ')

print()

#este bucle realiza lo mismo iterando
for character in str:
    print(character, end=' ')

print()


#slices

alpha = "abdefg"

print(alpha[1:3]) #pilla el segundo y tercero 
print(alpha[3:]) #pilla a partir del tercero
print(alpha[:3]) #pilla los 3 primeros hasta el tercero
print(alpha[3:-2]) #pilla unicamente el 3
print(alpha[-3:4]) #pilla unicamente el 3
print(alpha[::2]) #pilla d edos en dos
print(alpha[1::2]) #pilla el primero y se salta de uno en uno

frase ='There was once a very old man who was very kind'

print('o' in frase)
print('a' in frase)
print('a' not in frase)

t = 'The Knights Who Say "Ni!"'
print('[' + max(t) + ']')

print(frase.index('o')) #devuelve la posicion 10 porque es la que se encuentra primero
print(frase.count('o')) #devuelve la cantidad de ocurrencias de o


