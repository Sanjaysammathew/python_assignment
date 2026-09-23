# Employee Management Console


# List to store employees
employees = []


# 1. Add Employee
def add_employee():

    employee_id = int(input("Enter Employee ID: "))
    name = input("Enter Employee Name: ")
    department = input("Enter Department: ")
    salary = float(input("Enter Salary: "))

    employee = {
        "id": employee_id,
        "name": name,
        "department": department,
        "salary": salary
    }

    employees.append(employee)

    print("Employee added successfully!")


# 2. View Employees
def view_employees():

    if len(employees) == 0:
        print("No employees available.")

    else:
        print("\n----- Employee List -----")

        for employee in employees:
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("Salary:", employee["salary"])
            print("------------------------")


# 3. Search Employee
def search_employee():

    search_id = int(input("Enter Employee ID to search: "))

    found = False

    for employee in employees:

        if employee["id"] == search_id:

            print("\nEmployee Found")
            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Department:", employee["department"])
            print("Salary:", employee["salary"])

            found = True
            break

    if found == False:
        print("Employee not found.")


# 4. Find Highest Salary
def highest_salary():

    if len(employees) == 0:
        print("No employees available.")
        return

    highest = employees[0]

    for employee in employees:

        if employee["salary"] > highest["salary"]:
            highest = employee

    print("\n----- Highest Salary Employee -----")
    print("ID:", highest["id"])
    print("Name:", highest["name"])
    print("Department:", highest["department"])
    print("Salary:", highest["salary"])


# 5. Display Employees by Department
def employees_by_department():

    department = input("Enter Department: ")

    # List comprehension
    result = [
        employee
        for employee in employees
        if employee["department"].lower() == department.lower()
    ]

    if len(result) == 0:
        print("No employees found in this department.")

    else:
        print("\n----- Employees in", department, "-----")

        for employee in result:

            print("ID:", employee["id"])
            print("Name:", employee["name"])
            print("Salary:", employee["salary"])
            print("------------------------")



while True:

    print("\n===== EMPLOYEE MANAGEMENT =====")
    print("1. Add Employee")
    print("2. View Employees")
    print("3. Search Employee")
    print("4. Find Highest Salary")
    print("5. Display Employees by Department")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    match choice:

        case 1:
            add_employee()

        case 2:
            view_employees()

        case 3:
            search_employee()

        case 4:
            highest_salary()

        case 5:
            employees_by_department()

        case 6:
            print("Exiting...")
            break

        case _:
            print("Invalid choice. Please enter 1-6.")