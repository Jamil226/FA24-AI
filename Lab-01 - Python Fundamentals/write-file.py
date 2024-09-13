# Define the content to write to the file

content = """This is an example text file.
It contains some sample text.
It contains some sample1 text.
You can modify or add more lines as needed."""

# Open the file in write mode (creates the file if it doesn't exist)
with open('output/my-file1.txt', 'w') as file:
    file.write(content)  # Write the content to the file

print("File 'my-file1.txt' created and content written.")
