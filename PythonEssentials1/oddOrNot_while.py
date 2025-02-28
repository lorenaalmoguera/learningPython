cont_odd = 0
cont_eve = 0

maxnum = int (input("Enter the amount of numbers you wish to check: "))

while maxnum != 0:
    if maxnum % 2 == 0:
        print(maxnum, " is an even number!")
        cont_eve+=1
    else:
        print(maxnum, " is NOT an even number!")
        cont_odd+=1
    maxnum-=1

print("Total amount of even numbers: ", cont_eve)
print("Total amount of odd numbers: ", cont_odd)

