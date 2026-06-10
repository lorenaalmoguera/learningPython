list = {}


def List():
    while True:
        try:
            grocery = input().upper()

        except EOFError:
            print()
            break
        else:
            if grocery in list:
                list[grocery] += 1
            else:
                list[grocery] = 1

    for grocery in sorted(list):
        print(f"{list[grocery]} {grocery}")

def main():

    List()

main()

