import csv

def display_students(file_path) :
     
    try:
        if not file_path.exists():
            print("File Doesn't Exist")
            return

        with open(file_path, "r") as file:
            reader=csv.DictReader(file)
            print("Student Details")
            for student in reader:
                print(f"student ID: {student['student_id']}"
                      f"student Name: {student['name']}"
                      f"student Email: {student['email']}"
                      f"Age: {student['age']}"
                      f"Course: {student['course']}"
                      )

    except Exception as e:
       print("Error:", e)


