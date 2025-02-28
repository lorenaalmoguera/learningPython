import os
import shutil

# Create directories safely
os.makedirs("my_first_directory/my_second_directory", exist_ok=True)

# Change to the first directory
os.chdir("my_first_directory")
print("Current Directory:", os.getcwd())

# Change to the second directory correctly
os.chdir("my_second_directory")
print("Now in:", os.getcwd())

# Go back to the root before deletion
os.chdir("..")  # Go back to my_first_directory
os.chdir("..")  # Go back to the original directory

# Remove directories safely
shutil.rmtree("my_first_directory")  # Removes all subdirectories and files
print("Directories removed successfully.")
