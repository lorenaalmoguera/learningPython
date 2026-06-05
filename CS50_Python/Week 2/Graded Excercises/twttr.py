vowels = {
    "a",
    "e",
    "i",
    "o",
    "u"
}

def noVowels(str):
    result = ""
    i = 0
    for i in str:
        if i.lower() not in vowels:
            result += i

    return result


def main():
    print(noVowels(input("Input: ")))


main()
