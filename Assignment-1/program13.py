# Set Collection Demonstration

# 1. Creating a set
fruits = {"Apple", "Banana", "Orange", "Mango"}

print("Original Set:", fruits)


# 2. Adding an element - add()
fruits.add("Grapes")
print("\nAfter add():", fruits)


# 3. Adding multiple elements - update()
fruits.update(["Pineapple", "Papaya"])
print("After update():", fruits)


# 4. Checking whether an element exists - in
print("\nIs Mango present?", "Mango" in fruits)


# 5. Removing an element - remove()
fruits.remove("Banana")
print("After remove():", fruits)


# 6. Removing an element safely - discard()
fruits.discard("Orange")
print("After discard():", fruits)


# 7. Removing an arbitrary element - pop()
removed = fruits.pop()
print("After pop():", fruits)
print("Removed element:", removed)


# 8. Finding number of elements - len()
print("\nNumber of elements:", len(fruits))


# 9. Copying a set - copy()
new_fruits = fruits.copy()
print("Copied Set:", new_fruits)



set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

print("\nSet 1:", set1)
print("Set 2:", set2)


# 10. Union
print("\nUnion:", set1.union(set2))


# 11. Intersection
print("Intersection:", set1.intersection(set2))


# 12. Difference
print("Difference (set1 - set2):", set1.difference(set2))
print("Difference (set2 - set1):", set2.difference(set1))


# 13. Symmetric Difference
print("Symmetric Difference:",
      set1.symmetric_difference(set2))



small_set = {1, 2}
large_set = {1, 2, 3, 4, 5}

# 14. Subset
print("\nIs small_set subset of large_set?",
      small_set.issubset(large_set))


# 15. Superset
print("Is large_set superset of small_set?",
      large_set.issuperset(small_set))


# 16. Disjoint
set3 = {10, 20}

print("Are set1 and set3 disjoint?",
      set1.isdisjoint(set3))


# 17. Length
print("\nLength of set1:", len(set1))


# 18. Clear
set3.clear()
print("After clear():", set3)