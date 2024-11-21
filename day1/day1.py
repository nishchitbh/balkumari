print("Hello world")  # Code to print hello world
"""
This line prints hello world on terminal
Syntax: print(<variable/data>)
"""
print(1)  # This is integer data type
print(1.2)  # This is float data type
print([1, 2, 3, 4, 5, "Nishchit"])  # This is list data type


# Variable: A location on computer memory that stores data.
name = "Nishchit"  # name variable stores "Nishchit" string
python1 = "3.12.7"  # python1 variable stores "3.12.7" string
python2 = "3.13"
num1 = 53  # num1 variable stores integer 5
num2 = 6  # num2 variable stores integer 6

addition = num1 + num2  # Addition is done using + operator
print("The result of addition is", addition, "subtraction")
subtraction = num1 - num2  # Subtraction is done using - operator
multiplication = num1 * num2  # Multiplication is done using * operator
division = num1 / num2  # Division is done using / operator
integral_division = num1 // num2  # Integral division is done using // operator
modular_div = num1 % num2 # Modular division is done using % operator
print(
    "The result of subtraction is " + str(subtraction)
)  # Concatenation: Adding two strings
power = num1**num2  # Power operation is done using ** operator

# f-strings
print(f"The result of multiplication is {multiplication}, subtraction is {subtraction}")
print(
    f"The result of division is {division} and the result of integral division is {integral_division}"
)
print(f"{num1} to the power {num2} is {power}")
print(f"The result of modular division is {modular_div}")

fruits = ['apples', 'bananas', 'grapes', 'strawberries', 'mangoes', 'pineapples', 'a']
new_list = fruits[2] # Indexing is done using square brackets after variable name and index inside it
sliced_list = fruits[1:5] # Slicing is done using square brackets with 2 values separated by colon. The first value is the starting value and the second value is the ending value + 1.