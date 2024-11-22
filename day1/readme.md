# Python Basics: Introduction and Examples  

This document is an introductory guide to Python, designed for total beginners. It provides a detailed explanation of foundational concepts, such as printing, variables, arithmetic operations, string formatting, and working with lists.  

---

## Table of Contents  
1. [Printing in Python](#printing-in-python)  
   - [Purpose of `print()`](#purpose-of-print)  
   - [Examples of `print()`](#examples-of-print)  
2. [Variables in Python](#variables-in-python)  
   - [Definition](#definition-of-variables)  
   - [Examples](#examples-of-variables)  
3. [Basic Arithmetic Operations](#basic-arithmetic-operations)  
4. [String Formatting](#string-formatting)  
   - [Concatenation](#concatenation)  
   - [Using f-strings](#using-f-strings)  
5. [Working with Lists](#working-with-lists)  
   - [Indexing](#indexing)  
   - [Slicing](#slicing)  
   - [Detailed Explanation of "Inclusive" and "Exclusive"](#detailed-explanation-of-inclusive-and-exclusive)  
6. [Summary](#summary)  

---

## Printing in Python  

The `print()` function is a core feature in Python used to display information on the screen.  

### Purpose of `print()`  
- To output text, variables, or any kind of data.  
- Allows debugging by showing intermediate results of your code.  

### Syntax of `print()`  
```python  
print(<variable/data>)  
```  

### Examples of `print()`  
```python  
print("Hello world")  # Prints the string "Hello world"  
print(1)  # Prints an integer  
print(1.2)  # Prints a floating-point number  
print([1, 2, 3, 4, 5, "Nishchit"])  # Prints a list containing integers and a string  
```  

---

## Variables in Python  

### Definition of Variables  
A variable is like a container that stores data in your program.  

- **Why use variables?**  
   - To store data temporarily for calculations or manipulations.  
   - To make your code reusable and easier to read.  

- **Rules for Variable Names:**  
   - Must start with a letter or underscore (`_`).  
   - Cannot start with a number.  
   - Can contain letters, numbers, and underscores.  
   - Are case-sensitive (e.g., `name` and `Name` are different).  

### Examples of Variables  
```python  
name = "Nishchit"  # Stores the string "Nishchit"  
python1 = "3.12.7"  # Stores the string "3.12.7"  
num1 = 53  # Stores the integer 53  
num2 = 6  # Stores the integer 6  
```  

---

## Basic Arithmetic Operations  

Python supports basic arithmetic operations like addition, subtraction, multiplication, and more.  

| Operator | Operation            | Example          | Result |  
|----------|-----------------------|------------------|--------|  
| `+`      | Addition              | `5 + 2`          | `7`    |  
| `-`      | Subtraction           | `5 - 2`          | `3`    |  
| `*`      | Multiplication        | `5 * 2`          | `10`   |  
| `/`      | Division (float)      | `5 / 2`          | `2.5`  |  
| `//`     | Division (integral)   | `5 // 2`         | `2`    |  
| `%`      | Modulus (remainder)   | `5 % 2`          | `1`    |  
| `**`     | Exponentiation (power)| `5 ** 2`         | `25`   |  

### Example Code:  
```python  
addition = num1 + num2  
subtraction = num1 - num2  
multiplication = num1 * num2  
division = num1 / num2  
integral_division = num1 // num2  
modular_div = num1 % num2  
power = num1 ** num2  
```  

---

## String Formatting  

Strings can be manipulated in Python using concatenation or f-strings.  

### Concatenation  
Combining strings using the `+` operator.  

#### Example:  
```python  
result = "The result of subtraction is " + str(subtraction)  
print(result)  
```  

### Using f-strings  
A more modern and flexible method for string formatting.  

#### Example:  
```python  
print(f"The result of multiplication is {multiplication}, subtraction is {subtraction}")  
print(f"The result of division is {division} and the result of integral division is {integral_division}")  
print(f"{num1} to the power {num2} is {power}")  
print(f"The result of modular division is {modular_div}")  
```  

---

## Working with Lists  

Lists are a versatile data structure used to store ordered collections of items.  

### Indexing  
Accessing individual elements of a list using their position (index).  

- **Indexing starts at 0**: The first element has an index of `0`, the second has an index of `1`, and so on.  

#### Example:  
```python  
fruits = ['apples', 'bananas', 'grapes', 'strawberries', 'mangoes', 'pineapples']  
print(fruits[2])  # Output: 'grapes'  
```  

---

### Slicing  

Slicing allows extracting a subset of a list.  

#### Syntax:  
```python  
list[start:end:step]  
```  
- `start` (inclusive): The starting index.  
- `end` (exclusive): The index at which slicing stops.  
- `step`: The interval between elements (default is 1).  

#### Example:  
```python  
sliced_list = fruits[1:5]  # Outputs: ['bananas', 'grapes', 'strawberries', 'mangoes']  
```  

---

### Detailed Explanation of "Inclusive" and "Exclusive"  

- **Inclusive**: Includes the element at the specified index.  
  - In `fruits[1:5]`, the element at index `1` (`'bananas'`) is included.  

- **Exclusive**: Excludes the element at the specified index.  
  - In `fruits[1:5]`, the element at index `5` (`'pineapples'`) is excluded.  

#### Example with Step:  
```python  
sliced_list_with_step = fruits[0:6:2]  # Outputs: ['apples', 'grapes', 'mangoes']  
```  

---

## Summary  

This session covered:  
1. **Printing**: Using `print()` to display data and its syntax.  
2. **Variables**: Their definition, rules, and examples.  
3. **Arithmetic Operations**: Basic math operations and their usage.  
4. **String Formatting**: Using concatenation and f-strings for combining strings.  
5. **Lists**:  
   - **Indexing**: Accessing elements by their position.  
   - **Slicing**: Extracting subsets with inclusive/exclusive indices.  

By practicing these concepts, you will gain a strong understanding of Python's basics, enabling you to build more complex programs confidently.