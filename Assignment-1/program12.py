# List Collection Demonstration

# 1. Creating a list
fruits = ["Apple", "Banana", "Orange", "Mango"]

print("Original List:", fruits)


# 2. Accessing elements
print("\nFirst element:", fruits[0])
print("Last element:", fruits[-1])


# 3. Adding elements - append()
fruits.append("Grapes")
print("\nAfter append():", fruits)


# 4. Adding element at a specific position - insert()
fruits.insert(1, "Pineapple")
print("After insert():", fruits)


# 5. Adding multiple elements - extend()
fruits.extend(["Watermelon", "Papaya"])
print("After extend():", fruits)


# 6. Changing an element
fruits[0] = "Strawberry"
print("After changing element:", fruits)


# 7. Removing an element - remove()
fruits.remove("Banana")
print("After remove():", fruits)


# 8. Removing last element - pop()
removed = fruits.pop()
print("After pop():", fruits)
print("Removed element:", removed)


# 9. Removing element using index - pop(index)
removed = fruits.pop(1)
print("After pop(1):", fruits)
print("Removed element:", removed)


# 10. Finding length - len()
print("\nLength of list:", len(fruits))


# 11. Checking whether element exists - in
print("Is Mango present?", "Mango" in fruits)


# 12. Finding index - index()
if "Mango" in fruits:
    print("Index of Mango:", fruits.index("Mango"))


# 13. Counting elements - count()
fruits.append("Mango")
print("Number of Mango:", fruits.count("Mango"))


# 14. Sorting - sort()
fruits.sort()
print("After sort():", fruits)


# 15. Reverse the list - reverse()
fruits.reverse()
print("After reverse():", fruits)


# 16. Copying the list - copy()
new_fruits = fruits.copy()
print("Copied List:", new_fruits)


# 17. Slicing
print("First three elements:", fruits[:3])


# 18. Iterating through list
print("\nElements using loop:")
for fruit in fruits:
    print(fruit)


# 19. Clearing the list
fruits.clear()
print("\nAfter clear():", fruits)