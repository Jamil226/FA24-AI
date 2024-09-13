
# count = 1
# while count <= 5:
#     print(count)
#     count += 1

number = -1
while number <= 0:
    number = float(input("Enter a positive number: "))
    if number <= 0:
        print("The number must be positive.")
print(f"You entered a positive number: {number}")
