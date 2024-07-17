# Prompt the user to input two numbers and an operation choice


num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose an operation (+ for addition, - for subtraction, * for multiplication, / for division): ")

# Perform the calculation based on the operation chosen
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:  # Check for division by zero
        result = num1 / num2
    else:
        result = "Cannot divide by zero"
else:
    result = "Invalid operation"

# Display the result to the user
print("Result: ", result)
