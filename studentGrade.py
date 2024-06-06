students = {}

# Function to add a student
def add_student():
    name = input("Enter student name: ")
    students[name] = {}
    print(f"Student {name} added successfully.")

# Function to record grades for a student
def record_grade():
    name = input("Enter student name: ")
    if name in students:
        physics = int(input("Enter Physics marks: "))
        math = int(input("Enter Math marks: "))
        biology = int(input("Enter Biology marks: "))
        chemistry = int(input("Enter Chemistry marks: "))
        students[name] = {
            'Physics': physics,
            'Math': math,
            'Biology': biology,
            'Chemistry': chemistry
        }
        print(f"Grades recorded for {name}.")
    else:
        print(f"Student {name} not found.")

# Function to calculate the average grade for a student
def average_grade():
    name = input("Enter student name: ")
    if name in students:
        grades = students[name].values()
        average = sum(grades) / len(grades)
        print(f"Average grade for {name}: {average:.2f}")
    else:
        print(f"Student {name} not found.")


def main():
    while True:
        print("\n1. Add Student")
        print("2. Record Grades")
        print("3. Calculate Average Grade")
        print("4. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            record_grade()
        elif choice == '3':
            average_grade()
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
