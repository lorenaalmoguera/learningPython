def CheckInput():

    while True:
        user_input = input("Fraction: ")
        x, sep, z = user_input.partition("/")

        try:
            if not sep:
                raise ValueError
            x = int(x)
            z = int(z)

            if x < 0 or z <= 0 or x > z:
                raise ValueError

        except ValueError:
                pass
        else:
            return x, z


def division(x,z):
    try:
        res = round((x / z)*100)

        if res <= 1:
            print("E")
        elif res >= 99:
            print("F")
        else:
            print(f"{res}%")
    except ZeroDivisionError:
        print("")


def main():
    x, z = CheckInput()
    division(x,z)

main()
