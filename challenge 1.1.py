def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

# Prompt the user for input
number = int(input("Enter a number: "))

# Calculate the factorial
factorial_value = factorial(number)

# Print the result
print(f"The factorial of {number} is {factorial_value}")