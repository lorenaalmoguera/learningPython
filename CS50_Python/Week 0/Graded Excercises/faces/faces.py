
def convert(input):
    input = input.replace(':)', '🙂')
    input = input.replace(':(', '🙁')

    return input

def main():

    string = input()
    print(convert(string))


main()
