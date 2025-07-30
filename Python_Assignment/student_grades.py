#student grades
students_gradebook = {}  # Starts with empty gradebook

while True:
    print("\nOptions:")
    print("1. Add/Update your grade")
    print("2. View all grades")
    print("3. Exit..")
    
    choice = input("Enter your choice ? (1-3): ")
    
    if choice == "1":
        name = input("Enter student name: ")
        grade = input(f"Enter {name}'s grade (A-F): ").upper()
        students_gradebook[name] = grade
        print(f"{name}'s grade updated to {grade}")
        
    elif choice == "2":
        print("\nCurrent Grades:")
        for name, grade in students_gradebook.items():
            print(f"{name}: {grade}")
            
    elif choice == "3":
        print("byeeeeeeeeee!")
        break
        
    else:
        print("Please enter 1, 2 or 3")
