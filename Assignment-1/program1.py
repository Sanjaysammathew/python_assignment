#1. Student Result Analyzer
# Create a program that:
# 1.	Accepts student name.
# 2.	Accepts marks for 5 subjects.
# 3.	Calculates total.
# 4.	Calculates average.
# 5.	Determines grade.
# 6.	Determines Pass/Fail.
# 7.	Validates that marks are between 0 and 100.

# Get the student's name
student_name = input("Enter your name: ")

# Empty list to store the marks
student_marks = []

# List of subjects
subjects = ["English", "Tamil", "Maths", "Science", "Social Science"]

print(f"\nStudent Name: {student_name}")


# Get marks for each subject
for subject in subjects:

    # Keep asking until the user enters a valid mark
    while True:

        mark = int(input(f"Enter your {subject} marks: "))

        # Check whether mark is between 0 and 100
        if 0 <= mark <= 100:
            student_marks.append(mark)
            break
        else:
            print("Invalid mark! Please enter a mark between 0 and 100.")


# Display all the marks
print("\n Marks ")

for i in range(len(subjects)):
    print(f"{subjects[i]} : {student_marks[i]}")


# Calculate total marks
total = sum(student_marks)

print(f"\nTotal Mark: {total}")


# Calculate average
average = total / 5

print(f"Average Mark: {average:.2f}")


# Determine grade
match total:


    case x if x >= 480:
        grade = "A"


    case x if x >= 400:
        grade = "B"


    case x if x >= 250:
        grade = "C"


    case _:
        grade = "F"


print(f" {student_name} Grade: {grade}")


# Determine Pass or Fail
if  grade == "F":
    status = "fail"
else:
    status = "pass"



print(f"  {student_name} Status: {status}")






