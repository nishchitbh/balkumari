## Python Basics: Data Structures, Conditionals, and Loops  

This document serves as a comprehensive guide to understanding Python's basic data structures, conditional statements, and loops. It also includes concepts such as iterable objects, sorting, and key methods for working with different data types.  

---

## Table of Contents  

1. [Understanding Data Structures](#1-understanding-data-structures)  
   - [Lists](#lists)  
   - [Tuples](#tuples)  
   - [Sets](#sets)  
   - [Dictionaries](#dictionaries)  
2. [Conditional Statements](#2-conditional-statements)  
   - [if-else Statement](#if-else-statement)  
   - [match-case Statement](#match-case-statement)  
3. [Loops](#3-loops)  
   - [What are Iterables?](#what-are-iterables)  
   - [For Loop](#for-loop)  
   - [Using Range in Loops](#using-range-in-loops)  
4. [Sorting](#4-sorting)  
5. [Conclusion](#5-conclusion)  

---

## 1. Understanding Data Structures  

Data structures in Python are tools used to organize and manage data efficiently.  

### Lists  

**Lists** are:  
- **Ordered**: The elements retain the order in which they were added.  
- **Mutable**: You can modify them (add, remove, or update elements).  
- Allow **duplicate elements**.  

#### Common List Operations:  

```python  
# Creating a list
my_list = ["a", "b", "c", "h", "e"]  
list2 = ["f", "g", "h"]  

# Updating an element
my_list[3] = "d"  # Replaces 'h' with 'd'  

# Adding elements
my_list.append("f")  # Adds 'f' to the end  

# Removing elements by index
my_list.pop(0)  # Removes the first element ('a')  

# Extending a list
my_list.extend(list2)  # Appends all elements of `list2`  

# Removing elements by value
my_list.remove("e")  # Removes the first occurrence of 'e'  

print(my_list)  # Output: ['b', 'c', 'd', 'f', 'f', 'g', 'h']  
```  

---

### Tuples  

**Tuples** are:  
- **Immutable**: Once created, they cannot be changed.  
- Used to store fixed collections of items.  
- **Ordered**: The order of elements is maintained.  

#### Example:  

```python  
# Creating a tuple
tuple1 = (1, 2, 3, 4)  

# Attempting to modify a tuple raises an error
# tuple1.append(5)  # Uncommenting this will raise an AttributeError  
```  

---

### Sets  

**Sets** are:  
- **Unordered**: Elements do not maintain a specific order.  
- **Mutable**: Elements can be added or removed.  
- Do not allow **duplicate elements** (automatically removes duplicates).  

#### Example:  

```python  
# Creating a set
list3 = [2, 2, 3, 4, 4, 7, 7]  
unique_list = list(set(list3))  # Removes duplicates and converts back to a list  

print(unique_list)  # Output: [2, 3, 4, 7]  

set1 = {1, 3, 4, 5, 5, 6, 6, 7}  
print(set1)  # Output: {1, 3, 4, 5, 6, 7}  
```  

---

### Dictionaries  

**Dictionaries** are:  
- **Key-value pairs**: Store data in `key: value` format.  
- **Mutable**: Both keys and values can be added, removed, or updated.  
- Keys must be **unique**; values can be duplicated.  

#### Example:  

```python  
# Creating a dictionary
student = {  
    "name": "abhinav",  
    "number": "23445464",  
    "address": "kathmandu",  
    "subjects": ["physics", "math", "english"]  
}  

# Accessing values
print(student["subjects"])  # ['physics', 'math', 'english']  

# Adding key-value pairs
student["grade"] = 12  

# Removing a key-value pair
my_number = student.pop("number")  # Removes 'number'  

print(student)  # {'name': 'abhinav', 'address': 'kathmandu', 'subjects': ['physics', 'math', 'english'], 'grade': 12}  
print(my_number)  # 23445464  
```  

---

## 2. Conditional Statements  

Conditional statements allow you to execute code based on certain conditions.  

---

### if-else Statement  

The `if-else` structure evaluates conditions and executes blocks of code accordingly.  

- **if**: Executes when the condition is `True`.  
- **elif**: Executes when the previous condition(s) were `False` and its own condition is `True`.  
- **else**: Executes when no conditions were `True`.  

#### Example:  

```python  
a = 9  

if a == 1:  
    print("Value of a is 1")  
elif a == 2:  
    print("Value of a is 2")  
elif a == 3:  
    print("Value of a is 3")  
else:  
    print("Value of a is neither 1 nor 2 nor 3")  
# Output: Value of a is neither 1 nor 2 nor 3  
```  

---

### match-case Statement  

Introduced in Python 3.10, `match-case` is a cleaner alternative to `if-else`.  

- **case**: Matches specific patterns or values.  
- **case _:** Serves as the default when no other cases match.  

#### Example:  

```python  
match a:  
    case 1:  
        print("The value of a is 1")  
    case 2:  
        print("The value of a is 2")  
    case _:  
        print("The value of a is neither 1 nor 2")  
```  

---

## 3. Loops  

Loops allow repetitive execution of code.  

---

### What are Iterables?  

An **iterable object** is any object you can iterate (loop) through. Examples include:  
- Lists, tuples, dictionaries, sets, strings, and ranges.  
- **Iterating** means accessing each item in the object one at a time.  

---

### For Loop  

A `for` loop is used to iterate over iterable objects.  

#### Example:  

```python  
# Iterating over dictionary keys
for key in student:  
    print(key)  # Outputs each key  

# Printing values
print(student.values())  # Outputs all values in the dictionary  
```  

---

### Using Range in Loops  

The `range()` function generates a sequence of numbers.  

- **Syntax**: `range(start, stop, step)`  
   - `start` (inclusive): Starting number (default is 0).  
   - `stop` (exclusive): Ending number.  
   - `step`: The difference between each number (default is 1).  

#### Example:  

```python  
# Printing odd numbers from 1 to 100
for i in range(1, 101, 2):  
    print(i)  # Outputs all odd numbers  
```  

---

## 4. Sorting  

**Sorting** is the process of arranging elements in a particular order.  

- **Ascending Order**: From smallest to largest (default).  
- **Descending Order**: From largest to smallest.  

#### Example:  

```python  
# Sorting a list in reverse order
my_list = ["cricket", "football", "basketball", "tennis"]  
my_list.sort(reverse=True)  # Sorts in descending order  

print(my_list)  # ['tennis', 'football', 'cricket', 'basketball']  
```  

---

## 5. Conclusion  

In this lesson, we covered:  
- Basic **data structures**: Lists, tuples, sets, dictionaries.  
- Using **conditional statements** to make decisions.  
- Automating repetitive tasks using **loops**.  
- Understanding **iterable objects** and the `range()` function.  
- Sorting lists in a specific order.  

These concepts form the foundation of Python programming and will help you tackle more complex problems effectively.  