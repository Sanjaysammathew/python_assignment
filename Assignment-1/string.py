# String Functions Program

text = "hello world"

# 1. upper()
print("1. Uppercase:", text.upper())

# 2. lower()
text2 = "HELLO"
print("2. Lowercase:", text2.lower())

# 3. capitalize()
print("3. Capitalize:", text.capitalize())

# 4. title()
print("4. Title:", text.title())

# 5. strip()
text3 = "   hello   "
print("5. Strip:", text3.strip())

# 6. replace()
print("6. Replace:", "hello".replace("h", "H"))

# 7. split()
text4 = "a,b,c"
print("7. Split:", text4.split(","))

# 8. join()
letters = ["A", "B", "C"]
print("8. Join:", "-".join(letters))

# 9. find()
print("9. Find:", "hello".find("e"))

# 10. count()
print("10. Count:", "banana".count("a"))