
# variables
name = input("What's your name? ").strip().title() # <- it will return the same thing the user has inputed but without lifespace on right or left

print(f"hello, {name}")

"""
    everything between here is a comment
"""


print("Hello, world")
print("Your name is " + name)
print(name)
print("Hi", name)

## modify the print function

print("hello, ", end="")
print(name)

friend = input("What's your friendsname? ")
friend = friend.capitalize()
print(f"hello, {friend}")