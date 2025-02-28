line = input("Please enter an input: ")
i,j = 0, len(line) -1

is_palindrome = True

while i < j:
    if line[i] != line[j]:
        is_palindrome = False
        break
    i += 1
    j -= 1
if is_palindrome:
    print("Yes")
else:
    print("No")