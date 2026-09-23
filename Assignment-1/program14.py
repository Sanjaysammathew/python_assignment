# Dictionary Collection Demonstration

# 1. Creating a dictionary
student = {
    "name": "Sanjay",
    "age": 21,
    "department": "Computer Technology",
    "mark": 85
}

print("Original Dictionary:", student)


# 2. Accessing values using keys
print("\nName:", student["name"])
print("Age:", student["age"])


# 3. Accessing using get()
print("Department:", student.get("department"))


# 4. Adding a new key-value pair
student["city"] = "Coimbatore"
print("\nAfter adding city:", student)


# 5. Updating an existing value
student["mark"] = 90
print("After updating mark:", student)


# 6. Adding multiple key-value pairs - update()
student.update({
    "email": "sanjay@gmail.com",
    "phone": "9876543210"
})
print("After update():", student)


# 7. Checking whether a key exists
print("\nIs 'name' present?", "name" in student)


# 8. Getting all keys
print("\nKeys:", student.keys())


# 9. Getting all values
print("Values:", student.values())


# 10. Getting key-value pairs
print("Items:", student.items())


# 11. Removing using pop()
removed = student.pop("phone")
print("\nRemoved value:", removed)
print("After pop():", student)


# 12. Removing the last inserted item - popitem()
removed_item = student.popitem()
print("\nRemoved item:", removed_item)
print("After popitem():", student)


# 13. Copying a dictionary
student_copy = student.copy()
print("\nCopied Dictionary:", student_copy)


# 14. Finding number of key-value pairs
print("\nDictionary length:", len(student))


# 15. Iterating through keys
print("\nKeys using loop:")
for key in student:
    print(key)


# 16. Iterating through values
print("\nValues using loop:")
for value in student.values():
    print(value)


# 17. Iterating through keys and values
print("\nKeys and Values:")
for key, value in student.items():
    print(key, ":", value)


# 18. Removing all elements
student.clear()
print("\nAfter clear():", student)