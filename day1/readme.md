# Python Basics: Introduction and Examples

## Printing in Python

```python
print("Hello world")  # Code to print hello world
```

- **Purpose**: This line prints "Hello world" on the terminal.  
- **Syntax**: `print(<variable/data>)`

### Examples of `print()` Function

```python
print(1)  # This is integer data type
print(1.2)  # This is float data type
print([1, 2, 3, 4, 5, "Nishchit"])  # This is list data type
```

---

## Variables in Python

### Definition:
A variable is a location in computer memory that stores data.

### Examples of Variables:
```python
name = "Nishchit"  # name variable stores the string "Nishchit"
python1 = "3.12.7"  # python1 variable stores the string "3.12.7"
python2 = "3.13"
num1 = 53  # num1 variable stores integer 53
num2 = 6  # num2 variable stores integer 6
```

---

## Basic Arithmetic Operations

### Addition
```python
addition = num1 + num2
print("The result of addition is", addition, "subtraction")
```

### Subtraction
```python
subtraction = num1 - num2
```

### Multiplication
```python
multiplication = num1 * num2
```

### Division
```python
division = num1 / num2
```

### Integral Division
```python
integral_division = num1 // num2
```

### Modular Division
```python
modular_div = num1 % num2
```

### Power Operation
```python
power = num1 ** num2
```

---

## String Formatting

### Concatenation
Concatenating strings and variables:
```python
print("The result of subtraction is " + str(subtraction))
```

### Using f-strings
```python
print(f"The result of multiplication is {multiplication}, subtraction is {subtraction}")
print(f"The result of division is {division} and the result of integral division is {integral_division}")
print(f"{num1} to the power {num2} is {power}")
print(f"The result of modular division is {modular_div}")
```

---

## Working with Lists

### Example List
```python
fruits = ['apples', 'bananas', 'grapes', 'strawberries', 'mangoes', 'pineapples', 'a']
```

### Indexing
Accessing a specific element in the list:
```python
new_list = fruits[2]  # Accesses the 3rd element: 'grapes'
```

### Slicing
Extracting a subset of the list:
```python
sliced_list = fruits[1:5]  # Accesses elements from index 1 to 4: ['bananas', 'grapes', 'strawberries', 'mangoes']
```

### Notes on Indexing and Slicing:
- **Indexing**: Use square brackets `[]` with the desired index (starting from 0).  
- **Slicing**: Use `:` to specify a range. The start index is inclusive, and the end index is exclusive.

---

### Summary

This session covered the following:
1. **Printing** in Python using `print()` with different data types.
2. **Variables** and their use in storing data.
3. Basic **arithmetic operations** and how to use operators.
4. String manipulation with **concatenation** and **f-strings**.
5. Introduction to **lists**, including indexing and slicing.

By practicing these concepts, you will build a strong foundation in Python programming!