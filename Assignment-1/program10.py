# Student Management Console

students = []


# 1. Add Student
def add_student():

    name = input("Enter student name: ")
    mark = float(input("Enter mark: "))

    student = {
        "name": name,
        "mark": mark
    }

    students.append(student)

    print("Student added successfully!")


# 2. View Students
def view_students():

    if len(students) == 0:
        print("No students found.")

    else:
        print("\n----- Student List -----")

        for student in students:
            print("Name:", student["name"])
            print("Mark:", student["mark"])
            print("------------------------")


# 3. Search Student
def search_student():

    search_name = input("Enter student name to search: ")

    found = False

    for student in students:

        if student["name"].lower() == search_name.lower():

            print("\nStudent Found")
            print("Name:", student["name"])
            print("Mark:", student["mark"])

            found = True
            break

    if found == False:
        print("Student not found.")


# 4. Calculate Average
def calculate_average():

    if len(students) == 0:
        print("No students available.")
        return

    total = 0

    for student in students:
        total += student["mark"]

    average = total / len(students)

    print("Average Mark:", average)


# 5. Find Topper
def find_topper():

    if len(students) == 0:
        print("No students available.")
        return

    topper = students[0]

    for student in students:

        if student["mark"] > topper["mark"]:
            topper = student

    print("\n----- Topper -----")
    print("Name:", topper["name"])
    print("Mark:", topper["mark"])


# 6. Display Passed Students
def display_passed_students():

    # Assuming 40 is the passing mark
    passed_students = [
        student
        for student in students
        if student["mark"] >= 40
    ]

    if len(passed_students) == 0:
        print("No students passed.")

    else:
        print("\n----- Passed Students -----")

        for student in passed_students:
            print(
                "Name:", student["name"],
                "| Mark:", student["mark"]
            )


# --------------------------------
# Main Program
# --------------------------------

while True:

    print("\n===== STUDENT MANAGEMENT =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Calculate Average")
    print("5. Find Topper")
    print("6. Display Passed Students")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            add_student()

        case 2:
            view_students()

        case 3:
            search_student()

        case 4:
            calculate_average()

        case 5:
            find_topper()

        case 6:
            display_passed_students()

        case 7:
            print("Exiting...")
            break

        case _:
            print("Invalid choice. Please enter 1-7.")