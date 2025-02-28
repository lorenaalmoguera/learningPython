def introduction(first_name, last_name, age):
    print("Hello, my name is ", first_name, last_name, " and I am ", age, " years old.")

introduction("Lorena", "Almoguera Romero", 24)
introduction(age=24, first_name="Lorena", last_name="Almoguera Romero")

def message():
    print("Enter a value: ")
    return int(input())

a = message()
print(a)

def sum(a,b,c):
    print(a, "+", b, "+", c, "=", a+b+c)

sum(5,10,50)

value = None

def checkValue(value):
    if value is None:
        print("Sorry, you don't carry any value")
    else:
        print("The value of is: ", value)

checkValue(value)
checkValue(value=10)

def checkIfEven(value):
    if (value % 2) == 0:
        return True
    else:
        return False
b = message()
print("Check if b = ", b ," is an even number")
if(checkIfEven(b) == True):
    print("It is an even number")
else:
    print("It is not an even number")

def leapYear():
    year=int(input("Please introduce the year number: "))
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print("The year ", year, " is a leap year!")
    else:
        print("The year ", year, " is NOT a leap year!")
    return

leapYear()

def bmi(weight, height):
    return weight / height ** 2

print(bmi(90,1.65))

def ft_and_inch_to_m(ft, inch = 11):
    return ft * 0.3048 + inch * 0.0254


print(ft_and_inch_to_m(6))


def is_a_triangle(a, b, c):
    return a + b > c and b + c > a and c + a > b


a = float(input('Enter the first side\'s length: '))
b = float(input('Enter the second side\'s length: '))
c = float(input('Enter the third side\'s length: '))

if is_a_triangle(a, b, c):
    print('Yes, it can be a triangle.')
else:
    print('No, it can\'t be a triangle.')

