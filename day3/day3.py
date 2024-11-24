# Initialize a variable
a = 0
# Infinite loop using `while True`
while True:
    print(a)  # Print the current value of `a`
    a += 1    # Increment `a` by 1
    # This loop will run forever unless interrupted manually (e.g., Ctrl+C).

# This `while False` block will never execute since the condition is always False.
while False:
    print(a)  # This code is unreachable.
    a += 1

# Reset `a` to 0
a = 0
# Loop that continues as long as `a` is less than or equal to 10
while a <= 10:
    print(a)  # Print the current value of `a`
    a += 1    # Increment `a` by 1

# Reset `a` to 0
a = 0
# Loop that prints numbers until 10 but breaks when `a` equals 5
while a <= 10:
    print(a)  # Print the current value of `a`
    if a == 5:  # Check if `a` equals 5
        break   # Exit the loop if `a` is 5
    a += 1      # Increment `a` by 1

# Reset `a` to 0
a = 0
# Loop to demonstrate `continue` behavior
while a <= 10:
    a += 1      # Increment `a` by 1
    if a == 5:  # Skip the iteration when `a` equals 5
        continue
    print(a)    # Print the current value of `a` (skips 5)

# Loop to print numbers 1 to 10 on the same line
a = 1
while a <= 10:
    print(a, end="\n")  # Print `a` with a newline character
    a += 1              # Increment `a` by 1

# Printing a string with a newline character (`\n`) for line breaks
print("My name is Nishchit. \n I graduated from KMC Bagbazar")

# Function to calculate the area of a circle given its radius
def area_of_circle(r):
    return (22 / 7) * (r ** 2)  # Formula: π * r^2 (approximating π as 22/7)

# Call the function with radius 7 and print the result
print(area_of_circle(7))

# Function to calculate the area of a triangle given base and height
def area_of_triangle(b, h):
    return (1 / 2) * b * h  # Formula: 1/2 * base * height

# Calculate the area of two triangles and sum their areas
triangle1 = area_of_triangle(5, 7)
triangle2 = area_of_triangle(9, 10)
total_area = triangle1 + triangle2
print("Total area of triangle is", total_area)

# Function with no input parameters, returning a string
def name():
    return "Your name is Nishchit"

# Call the function and print the returned string
print(name())

# Function with no return value but prints output
def age():
    print("Your age is 20")

# Call the `age` function multiple times
age()
age()
age()

# Input validation using `try-except`
num1 = 0
num2 = 0
try:
    num1 = int(input("Enter any number: "))  # Prompt user for first number
    num2 = int(input("Enter another number: "))  # Prompt user for second number
except ValueError:  # Handle non-integer inputs
    print("Please enter a number")

# Print the sum of the two numbers
print("Your sum is", num1 + num2)

# Demonstrating the `random` module
import random

# List of fruits
mylist = ['apples', 'bananas', 'strawberries', 'mangoes']

# Randomly select one fruit from the list
print(random.choice(mylist))

# Shuffle the list randomly
random.shuffle(mylist)
print(mylist)

# Generate a random integer between 1 and 6
print(random.randint(1, 6))

# Demonstrating the `os` module
import os

# Print the current working directory
print(os.getcwd())

# List all files and directories in the current directory
print(os.listdir())

# Uncomment the following line to create a new folder named 'folder 2'
# os.mkdir('folder 2')
