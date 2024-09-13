# -------------------------------------
# Iterate over each element in the list
# -------------------------------------
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)  

# --------------------------------------
# Iterate over each element in the tuple
# --------------------------------------

colors = ("red", "green", "blue")
for color in colors:
    print(color)  # Prints each color in the tuple

# -----------------------------------------
# Iterate over each character in the string
# -----------------------------------------

word = "hello"
for char in word:
    print(char)  # Prints each character in the string

# Iterate over a sequence of numbers from 0 to 4
for i in range(5):
    print(i)  # Prints numbers from 0 to 4

# -----------------------
# Using range() Function
# -----------------------

# Iterate over a sequence of numbers from 2 to 5
for i in range(2, 6):
    print(i)  # Prints numbers from 2 to 5

# Iterate over a sequence of numbers from 0 to 8 with a step of 2
for i in range(0, 10, 2):
    print(i)  # Prints even numbers from 0 to 8

# -------------------------------------
# Iterate over the keys in the dictionary
# -------------------------------------

person = {"name": "Alice", "age": 30}
for key in person:
    print(key)  # Prints each key in the dictionary

# Iterate over the values in the dictionary
for value in person.values():
    print(value)  # Prints each value in the dictionary

# Iterate over key-value pairs in the dictionary
for key, value in person.items():
    print(f"{key}: {value}")  # Prints each key-value pair in the dictionary

# --------------------------------------------------
# Iterate over a 2D list (matrix) using nested loops
# --------------------------------------------------


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:  # Outer loop iterates over each row
    for elem in row:  # Inner loop iterates over each element in the row
        print(elem, end=" ")  # Prints each element in the row with a space
    print()  # Moves to the next line after printing all elements in the row
