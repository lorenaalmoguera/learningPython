def snakeCase(input):
    result = ""
    i = 0
    for i in input:
        if i.isupper():
            result += "_"
            result += i.lower()
        else:
            result += i
    return result

def main():

    print(snakeCase(input("camelCase: ")))

main()



