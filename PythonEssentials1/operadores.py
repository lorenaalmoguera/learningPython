a = int(input("Por favor, introduce un numero: "))
b = int(input("Por favor, introduice otro numero: "))

if a == b: 
    print(a, " y ",b ," son equivalentes")
elif a > b:
    print(a, " (a) es mayor a (b)", b)
else:
    print(b, " (b) es mayor a (a) ", a)

print("Es cierto que: a = b? Es:", a == b)  # Devuelve True o False

plant = str(input("Please give me your favorite plant"))

if plant == "Rose" or plant == "rose" :
    print("Yes ! The rose is the most beautiful flower")
elif plant == "Tulip" or plant == "tulip":
    print("Have you seen wicked?")
else:
    print("I'm not familiar with that flower!")