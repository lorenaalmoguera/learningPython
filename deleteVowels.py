userinput = str(input("Please give me a sentence!"))
userinput = userinput.upper()
for i in userinput:
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        continue
    print(i)

#esto lo imprimira linea a linea... pero!

sinvocales =""
for i in userinput:
    if i == "A" or i == "E" or i == "I" or i == "O" or i == "U":
        continue
    sinvocales+=i

print(sinvocales)
