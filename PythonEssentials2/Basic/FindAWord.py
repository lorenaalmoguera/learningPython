line = input("Introduce a string: ")
word = input("Introduce a word that you'd like to find: ")

fnd = line.find(word)
found = True
found = fnd != -1  # If not found, it returns -1

while fnd != -1:
    fnd = line.find(word, fnd + 1)  # Look for next occurrenc
if found == True:
    print("The word has been found.")
else:
    print("The word has not been found.")

