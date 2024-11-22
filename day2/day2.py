# Python Lesson: Working with different data structures, conditionals, and loops

# Working with lists
my_list = ["a", "b", "c", "h", "e"]  # A list containing some characters
list2 = ["f", "g", "h"]  # Another list for later extension

# Updating an element in the list
my_list[3] = "d"  # Replacing the 4th element ('h') with 'd'

# Adding a new element to the list
my_list.append("f")  # Append adds 'f' to the end of the list
print(my_list)  # ['a', 'b', 'c', 'd', 'e', 'f']

# Removing an element by its index
my_list.pop(0)  # Removes the first element ('a')
print(my_list)  # ['b', 'c', 'd', 'e', 'f']

# Extending the list by adding elements of another list
my_list.extend(list2)  # Adds all elements of list2 to my_list
print(my_list)  # ['b', 'c', 'd', 'e', 'f', 'f', 'g', 'h']

# Removing an element by its value
my_list.remove("e")  # Removes the first occurrence of 'e'
print(my_list)  # ['b', 'c', 'd', 'f', 'f', 'g', 'h']

# Working with tuples
tuple1 = (1, 2, 3, 4)  # A tuple with immutable elements
# Uncommenting the following line would raise an AttributeError because tuples are immutable
# tuple1.append(5)

# Working with sets
list3 = [2, 2, 3, 4, 4, 7, 7]  # A list with duplicate elements
unique_list = list(set(list3))  # Convert list to a set to remove duplicates, then back to a list
print(unique_list)  # [2, 3, 4, 7] (order may vary as sets are unordered)

set1 = {1, 3, 4, 5, 5, 6, 6, 7}  # A set automatically removes duplicates
print(set1)  # {1, 3, 4, 5, 6, 7}

# Sorting a list in reverse order
my_list = ["cricket", "football", "basketball", "tennis"]  # A list of sports
my_list.sort(reverse=True)  # Sorts in descending order
print(my_list)  # ['tennis', 'football', 'cricket', 'basketball']

# Working with dictionaries
student = {
    "name": "abhinav", 
    "number": "23445464", 
    "address": "kathmandu", 
    "subjects": ["physics", "math", "english"]
}  # A dictionary representing a student
print(student["subjects"])  # Accessing the list of subjects

# Adding a new key-value pair
student["grade"] = 12  # Adds a new key 'grade' with value 12

# Removing a key-value pair and saving the value
my_number = student.pop("number")  # Removes 'number' and returns its value
print(student)  # {'name': 'abhinav', 'address': 'kathmandu', 'subjects': ['physics', 'math', 'english'], 'grade': 12}
print(my_number)  # 23445464

# Conditional statements

# if-else statement:
# The if-else structure evaluates conditions to execute specific blocks of code. 
# - If the condition is True, the code under the 'if' block executes.
# - If False, it checks 'elif' (else if) conditions in order, and executes the first match.
# - If no conditions match, the 'else' block executes (if provided).

a = 9

if a == 1:
    print("Value of a is 1")  # Executes if a equals 1
elif a == 2:
    print("Value of a is 2")  # Executes if a equals 2
elif a == 3:
    print("Value of a is 3")  # Executes if a equals 3
else:
    print("Value of a is neither 1 nor 2 nor 3")  # Executes if all other conditions are False

# match-case statement:
# Introduced in Python 3.10, match-case is a modern way to compare a value with multiple options.
# - It works similarly to a "switch-case" in other languages.
# - The 'case' blocks check specific patterns (values or conditions).
# - The default block is specified using 'case _:' and executes when no cases match.

match a:
    case 1:
        print("The value of a is 1")  # Executes if a equals 1
    case 2:
        print("The value of a is 2")  # Executes if a equals 2
    case 3:
        print("The value of a is 3")  # Executes if a equals 3
    case 4:
        print("The value of a is 4")  # Executes if a equals 4
    case _:
        print("The value of a is neither 1 nor 2 nor 3 nor 4")  # Executes if no other case matches

# Loops: Using for loop
# A for loop iterates over *iterable objects*. An iterable object is anything that can be traversed (iterated).
# Examples of iterables: lists, tuples, dictionaries, sets, strings, and ranges.
# In a for loop, the 'i' (or any variable name) is assigned each item of the iterable, one at a time.

# Iterating over dictionary keys
for key in student:  # 'student' is a dictionary, an iterable object.
    print(key)  # Prints each key in the dictionary
print("The loop is completed")

print(student.values())  # Prints all the values in the dictionary

# Using range in for loops:
# The range function generates a sequence of numbers (an iterable).
# range(start, stop, step): 
# - start (inclusive) is the beginning value, stop (exclusive) is the ending value, and step defines the difference between numbers.
for i in range(1, 101, 2):  # Iterates from 1 to 100 with a step of 2
    print(i)  # Prints all odd numbers from 1 to 100
