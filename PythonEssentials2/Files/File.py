import errno

file_path = r"C:\Users\loren\Documents\GitHub\learningPython\PythonEssentials2\Files\prueba.txt"

try:
    print(f"Trying to open file: {file_path}")
    s = open(file_path, "rt")
    print("File opened successfully!")
    # Actual processing goes here (e.g., read content)
    content = s.read()
    print("File content:", content)
    s.close()
except OSError as exc:
    print(f"Error occurred: {exc}")  # Debugging print
    if exc.errno == errno.ENOENT:
        print("The file doesn't exist.")
    elif exc.errno == errno.EMFILE:
        print("You've opened too many files.")
    else:
        print("The error number is:", exc.errno)
