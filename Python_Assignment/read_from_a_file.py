# read text from a file
filename = "my_notes.txt"
#opeing a file in read mode and stroing notes in content and printing it. 
#using try catch if file not found
try:
    with open(filename, "r") as file:
        content = file.read()
    print("\nFile contents:")
    print(content)
except FileNotFoundError:
    print(f"File not exist in system")
