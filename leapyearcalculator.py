year=int(input("Please introduce the year number: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("The year ", year, " is a leap year!")
else:
    print("The year ", year, " is NOT a leap year!")