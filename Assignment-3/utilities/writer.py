
import csv


SECONDARY_FIELDS = ["student_id","sports","clubs","certifications", "achievements"]

def read_students(file_path):
    try:
        with open(file_path,"r") as file:

            reader = csv.DictReader(file)
            return list(reader)

    except FileNotFoundError:
        print("Error: File not found.")

    except Exception as e:
        print("Error:", e)

    return []


def write_students(file_path, students):
    try:
        with open(file_path,"w") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=SECONDARY_FIELDS
            )

            writer.writeheader()
            writer.writerows(students)
            return True

    except Exception as e:
        print("Error:", e)

    return False


def display_students(file_path):
    students = read_students(file_path)

    students = sorted(students, key=lambda student: student["student_id"])

    print("\nSECONDARY STUDENT DETAILS")

    for index, student in enumerate(students, start=1):
        print(
            f"{index}. ID: {student['student_id']} | "
            f"Sports: {student['sports']} | "
            f"Clubs: {student['clubs']} | "
            f"Certifications: {student['certifications']} | "
            f"Achievements: {student['achievements']}"
        )


def append_student(primary_file, secondary_file):

    print("\nADD EXTRA DETAILS")

    student_id = input("Student ID: ").strip()

    if not student_id:
        print("Error: Student ID cannot be empty.")
        return

    primary_students = read_students(primary_file)
    student_exists = False

    for student in primary_students:
        if student["student_id"] == student_id:
            student_exists = True
            break

    if not student_exists:
        print("Error: Student ID does not exist in primary file.")
        return

    secondary_students = read_students(secondary_file)

    for student in secondary_students:
        if student["student_id"] == student_id:
            print("Error: Student ID already has extra details.")
            return

    sports = input("Sports: ").strip()
    clubs = input("Clubs: ").strip()
    certifications = input("Certifications: ").strip()
    achievements = input("Achievements: ").strip()

    if not sports or not clubs or not certifications or not achievements:
        print("Error: All fields are required.")
        return

    student = {
        "student_id": student_id,
        "sports": sports,
        "clubs": clubs,
        "certifications": certifications,
        "achievements": achievements
    }

    try:
        with open(secondary_file, "a") as file:

            writer = csv.DictWriter(
                file,
                fieldnames=SECONDARY_FIELDS
            )

            writer.writerow(student)

        print("Extra details added successfully.")

    except FileNotFoundError:
        print("Error: File not found.")

    except Exception as e:
        print("Error:", e)


def search_student(file_path):

    print("\nSEARCH STUDENT")

    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Error: Student ID cannot be empty.")
        return

    students = read_students(file_path)

    for student in students:

        if student["student_id"] == student_id:

            print(
                f"ID: {student['student_id']} | "
                f"Sports: {student['sports']} | "
                f"Clubs: {student['clubs']} | "
                f"Certifications: {student['certifications']} | "
                f"Achievements: {student['achievements']}"
            )
            return

    print("Student not found.")


def display_secondary_file(file_path):
    students = read_students(file_path)

    print("\nSECONDARY FILE DETAILS")

    if not students:
        print("No student details found.")
        return

    for student in students:
        print(
            f"ID: {student['student_id']} | "
            f"Sports: {student['sports']} | "
            f"Clubs: {student['clubs']} | "
            f"Certifications: {student['certifications']} | "
            f"Achievements: {student['achievements']}"
        )

def update_student(file_path):

    print("\nUPDATE STUDENT")

    student_id = input("Enter Student ID: ").strip()

    if not student_id:
        print("Error: Student ID cannot be empty.")
        return

    students = read_students(file_path)

    for student in students:

        if student["student_id"] == student_id:

            sports = input("Sports: ").strip()
            clubs = input("Clubs: ").strip()
            certifications = input("Certifications: ").strip()
            achievements = input("Achievements: ").strip()

            if not sports or not clubs or not certifications or not achievements:
                print("Error: All fields are required.")
                return

            student["sports"] = sports
            student["clubs"] = clubs
            student["certifications"] = certifications
            student["achievements"] = achievements

            if write_students(file_path, students):
                print("Student updated successfully.")
            return

    print("Student not found.")

    

