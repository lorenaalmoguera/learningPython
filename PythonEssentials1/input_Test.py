print("This is a program to show how input() works")
myInput = input()
print("Hmmm can you give me an input?", myInput, "...Oh Okay")

print("Now let's prompt the user...")
mySecondInput = input("This is a prompt ")
print("Hmm...", mySecondInput, "...Oh Okay")

print("Let's do a calculation from the user's input")
print()

myNumber = float(input("Please... Introduce a number: "))
result = myNumber % 2

#this will check if the number is even or uneven
if result != 0:
    str(result) #will convert it to a string
    print("This is an uneven number ", result)
else:
    str(result) #will convert it to a string
    print("This is an even number ", result)

name="Lorena"
print(name*3) #this will print the name 3 times 


