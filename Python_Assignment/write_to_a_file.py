#as per the question - file name is given 
filename = "my_notes.txt"
notes = input("Enter your Notes?\n")
#opening file in write mode
with open(filename, "w") as file:
    file.write(notes)

print(f"Saved to {filename}!")
