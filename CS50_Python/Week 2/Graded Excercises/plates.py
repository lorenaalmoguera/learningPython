def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) > 6 or len(s) < 2:
        return False

    if not s.isalnum():
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    number_has_started = False

    for i in s:
        if i.isdigit():
            if not number_has_started and i == "0":
                return False

            number_has_started = True

        elif number_has_started:
            return False
    return True






main()
