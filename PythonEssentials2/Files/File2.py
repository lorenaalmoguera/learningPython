from os import strerror

nofile ='text.txt'
yesfile = r"C:\Users\loren\Documents\GitHub\learningPython\PythonEssentials2\Files\File2.py"

try:
    counter = 0
    stream = open(yesfile, "rt")
    char = stream.read(1)
    while char != '':
        print(char, end='')
        counter += 1
        char = stream.read(1)
    stream.close()
    print("\n\nCharacters in file:", counter)
except IOError as e:
    print("I/O error occurred: ", strerror(e.errno))

try:
    character_counter = line_counter = 0
    stream = open(yesfile, 'rt')
    line = stream.readline()
    while line != '':
        line_counter += 1
        for char in line:
            print(char, end='')
            character_counter += 1
        line = stream.readline()
    stream.close()
    print("\n\nCharacters in file:", character_counter)
    print("Lines in file:     ", line_counter)
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
    


from os import strerror

try:
	file = open('newtext.txt', 'wt') # A new file (newtext.txt) is created.
	for i in range(10):
		s = "line #" + str(i+1) + "\n"
		for char in s:
			file.write(char)
	file.close()
except IOError as e:
	print("I/O error occurred: ", strerror(e.errno))
    

