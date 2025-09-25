# list_basics.py

# Create a list
my_list = [10, 20, 30, 40, 50]
print("Original list:", my_list)

# Access elements
print("First element:", my_list[0])
print("Last element:", my_list[-1])

# Add elements
my_list.append(60)
print("After appending 60:", my_list)

# Insert element at index 2
my_list.insert(2, 25)
print("After inserting 25 at index 2:", my_list)

# Remove element
my_list.remove(30)
print("After removing 30:", my_list)

# Slicing
print("Elements from index 1 to 3:", my_list[1:4])

# Length of list
print("Length of list:", len(my_list))