
input = input("What's the expression: ")

x, op, z = input.split(" ")

x = float(x)
z = float(z)

if op == "+":
    print(x+z)
elif op == "-":
    print(x-z)
elif op == "*":
    print(x*z)
elif op == "/":
    print(x/z)
