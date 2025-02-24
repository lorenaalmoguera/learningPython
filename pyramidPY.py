blocks = int(input("Give me a number of layers to build a pyramid: "))

ask = "*"

if blocks % 2 == 0:
    for i in range(1, blocks + 1):
        spaces = " " * (blocks - i)
        stars = ask * (2 * i - 1)
        print(spaces + stars)
else:
    print("must be an even number")

blocksnew = int (input("Give me a number of blocks to build a pyramid with: "))
totallayers = int(blocksnew / 2)
if blocksnew % 2 == 0:
    for i in range(0,totallayers):
        if i == 0:
            print(ask)
        else:
            print(ask*(i+1))
else:
    print("must be an even number")