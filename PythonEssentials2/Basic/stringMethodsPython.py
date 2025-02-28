frase = 'pitbull is the best musician of our generation'
print(frase.capitalize())
print('[' + 'hola que tal'.center(20, '*') + ']')

t="ABCD"
print(t.endswith("CD"))

print(frase.find('bull'))
print(frase.find('i', 10)) #empieza la busqueda del index a partir de la 10

the_text = """A variation of the ordinary lorem ipsum
text has been used in typesetting since the 1960s 
or earlier, when it was popularized by advertisements 
for Letraset transfer sheets. It was introduced to 
the Information Age in the mid-1980s by the Aldus Corporation, 
which employed it in graphics and word-processing templates
for its desktop publishing program PageMaker (from Wikipedia)"""

#imprimir todas las ocurrencias
fnd = the_text.find('the')
while fnd != -1:
    print(fnd)
    fnd = the_text.find('the', fnd + 1)

textoaux1 = 'a124412@'
textoaux2 = '123214'
textoaux3 = 'EstoEsUnaPrueba'
textoaux4 = 'Esto es una Prueba'
textoaux5 ='esto es una prueba'
textoaux6 = ' '
textoaux7 = 'ESTOESUNAPRUEBA'

print(textoaux1.isalnum())
print(textoaux2.isalnum())
print(textoaux3.isalpha())
print(textoaux4.isalpha())
print(textoaux2.isdigit())
print(textoaux4.islower())
print(textoaux5.islower())
print(textoaux6.isspace())
print(textoaux5.isspace())
print(textoaux7.isupper())

print()
print(",".join([textoaux1, textoaux4, textoaux7]))
print()

print(textoaux7.lower())
print(textoaux1.upper())
print()
#para quitar parte izquierda o derecha de uns tring
print("www.cisco.com".lstrip("w."))
print("pythoninstitute.org".rstrip(".org")) #si llega a ser lstrip no borraría nada

print("This is it!".replace("is", "are"))

# Demonstrating the rfind() method:
print("tau tau tau".rfind("ta"))

# Demonstrating the split() method:
print("phi       chi\npsi".split())

#Finding the beginning of a string
print("omega".startswith("om"))

print()

print("I know that I know nothing.".swapcase())

print("I know that I know nothing. Part 1.".title())