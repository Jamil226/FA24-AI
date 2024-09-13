def number_description(number):
    if number > 0:
        if number % 2 == 0:
            return "The number is positive and even."
        else:
            return "The number is positive and odd."
    elif number < 0:
        if number % 2 == 0:
            return "The number is negative and even."
        else:
            return "The number is negative and odd."
    else:
        return "The number is zero."

# Example usage
num = int(input("Enter a number: "))
print(number_description(num))
