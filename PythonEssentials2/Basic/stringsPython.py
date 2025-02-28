word = str(input("Introduce una palabra: "))

print("La palabra ", word, " tiene una longitud de: ", len(word), " caracteres")

multiline='''Tambien 

podemos tener strings

que
ocupen

muchas lineas'''

print(multiline)

print()

str1 = "Alejandro"
str2 = "es"
str3 = "mi"
str4 = "amigo"
esp= " "

print(str1 + esp + str2 + esp + str3 + esp + str4)
print((str1 + esp) * 4)

print(ord(esp)) #imprimirá el caracter ascii solo para caracteres singulares

print(chr(97))