mylist = [10, 5, 7, 2, 1]
print("Original list contents:", mylist)

mylist[0] = 1111
print("New list contents:", mylist)

print("My list has a total of: ", len(mylist), " characters")

#we can also delete elements such as:

del mylist[2]

print(mylist, "has a total of ", len(mylist), " characters")

mylist.append(50)

mylist.insert(0,222)

print(mylist, " we have added new numbers so now we have ", len(mylist))

mylist[0], mylist[1], mylist[2] = mylist[2], mylist[1], mylist[0]
mylist[3], mylist[4], mylist[5] = mylist[5], mylist[4], mylist[3]

print(mylist, "we have a new order")

del mylist