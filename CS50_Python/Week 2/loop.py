
def main():

    i = 3
    while i != 0:
        print("meow")
        i = i-1

    i = 0
    names = ["Mario", "Luigi", "Diasy", "Yoshi"]
    for i in range(len(names)-1):
        print(write_letter(names[i], names[i+1]))

def write_letter(receiver, sender):
    return f"""

    Dear {receiver},

    This is a letter from your friend.

    Kind regards,  
    {sender}
    """

main()
