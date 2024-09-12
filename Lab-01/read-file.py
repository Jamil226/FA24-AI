# --------------------------------------------------
# Open the file in read mode
# --------------------------------------------------

with open('input/history.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    print(line.strip())  # Print each line, stripping leading/trailing whitespace


# --------------------------------------------------
#Reading Line by Line
# --------------------------------------------------


with open('input/file.txt', 'r') as file:
    
    for line in file:
        print(line.strip()) 

# --------------------------------------------------
# Example with Exception Handling
# --------------------------------------------------

try:
    with open('input/file.txt', 'r') as file:
        # Read the entire content of the file
        content = file.read()
        print(content)  # Print the entire content
except FileNotFoundError:
    print("The file does not exist.")
except IOError:
    print("An error occurred while reading the file.")

