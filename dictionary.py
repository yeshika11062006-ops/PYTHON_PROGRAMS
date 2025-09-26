# Basic operations with Python dictionaries

# Creating a dictionary
student = {"name": "Alice", "age": 20, "grade": "A"}
print("Original dictionary:", student)

# Accessing values
print("Name:", student["name"])

# Adding a key-value pair
student["roll_no"] = 101
print("After adding roll_no:", student)

# Updating a value
student["age"] = 21
print("After updating age:", student)

# Iterating through dictionary
print("Keys and values:")
for key, value in student.items():
    print(key, ":", value)