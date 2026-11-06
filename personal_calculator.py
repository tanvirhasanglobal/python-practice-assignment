name = input("Enter your name: ")
age = input("Enter your age: ")
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

sum_result = first_number + second_number
subtraction_result = first_number - second_number
multiplication_result = first_number * second_number
division_result = first_number / second_number if second_number != 0 else "undefined (cannot divide by zero)"

print(f"Hello, {name}! You are {age} years old.")
print(f"The sum of {first_number} and {second_number} is: {sum_result}")
print(f"The difference between {first_number} and {second_number} is: {subtraction_result}")
print(f"The product of {first_number} and {second_number} is: {multiplication_result}")
print(f"The quotient of {first_number} and {second_number} is: {division_result}")