try:
    value = int(input('Enter a natural number: '))
    print('The reciprocal of ', value, ' is ', 1/value)
except ValueError:
    print('I cannot do anything with this value')
except ZeroDivisionError:
    print('Division by zero is not allowed')
except:
    print('Something strange has happened here... Sorry!')

while True:
    try:
        number = int(input("Enter an integer number: "))
        print(number/2)
        break
    except:
        print("Warning: the value entered is not a valid number. Try again...")

