coins = {
       25,
       10,
       5
}


def insert():

    total = 50
    given = 0
    while given < total:
        amountdue = total - given
        print(f"Amount due: {amountdue}" )
        coin = int(input("Insert Coin: "))
        if coin in coins:
            given += coin

        change_owed = given - total
        print(f"Change owed: {change_owed}")

def main():
    insert()


main()
