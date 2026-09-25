import csv

FIELDS = ["student_id","name",  "age","course","email"]

def read_students(file_path):
    try:
        with open(file_path, "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            return list(reader)
    except Exception as e:
        print("Error:", e)

    return []


def write_students(file_path, students):
    try:
        with open(file_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writeheader()
            writer.writerows(students)
            return True

    except Exception as e:
        print("Error:", e)

    return False

def append_students(file_path):
    print("Append Students")
    students = {
        "student_id": input("Enter Student ID: "),
        "name": input("Enter Student Name: "),
        "age": input("Enter Student Age: "),
        "course": input("Enter Student Course: "),
        "email": input("Enter Student Email: "),
    }
    try :
        with open(file_path, "a") as file:
            writer = csv.DictWriter(file, fieldnames=FIELDS)
            writer.writerow(students)
            print("Successfully Appended Students")
    except FileNotFoundError:
        print("Error:File Not Found")
    except Exception as e :
        print("Error:", e)
def search_student(file_path):

    print("\n SEARCH STUDENT ")

    keyword = input("Enter ID, name or course: ").lower()

    students = read_students(file_path)

    found = False

    for student in students:

        if (
            keyword in student["student_id"].lower()
            or keyword in student["name"].lower()
            or keyword in student["course"].lower()
        ):

            print(
                f"ID: {student['student_id']} | "
                f"Name: {student['name']} | "
                f"Age: {student['age']} | "
                f"Course: {student['course']} | "
                f"Email: {student['email']}"
            )

            found = True

    if not found:

        print("Student not found.")