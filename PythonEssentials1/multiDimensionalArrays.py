# A four-column/four-row table ‒ a two dimensional array (4x4)


table = [[":(", ":)", ":(", ":)"],
         [":)", ":(", ":)", ":)"],
         [":(", ":)", ":)", ":("],
         [":)", ":)", ":)", ":("]]

#print(table)
print(table[0][0])  # outputs: ':('
print(table[0][3])  # outputs: ':)'

print()

cube = [[[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':(', 'x', 'x']],
 
        [[':)', 'x', 'x'],
         [':(', 'x', 'x'],
         [':)', 'x', 'x']],
 
        [[':(', 'x', 'x'],
         [':)', 'x', 'x'],
         [':)', 'x', 'x']]]

print(cube[0][0][0])  # outputs: ':('
print(cube[2][2][0])  # outputs: ':)'
 


