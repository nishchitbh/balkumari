
## **1. `while` Loop**
### **What is a `while` loop?**
A `while` loop in Python is a control flow statement that repeatedly executes a block of code as long as a given condition is `True`.

### **Syntax of `while` Loop**
```python
while condition:
    # Code block to execute repeatedly
```
- **Condition**: A logical statement that evaluates to `True` or `False`.
- If the condition is `True`, the code inside the loop is executed.
- If the condition is `False`, the loop stops.

### **How It Works**
- The condition is checked before each iteration (looping cycle).
- If the condition remains `True`, the code block executes.
- If the condition becomes `False`, the loop exits.

### **Example**
```python
a = 0
while a < 5:  # The loop will run as long as `a` is less than 5
    print(a)  # Print the current value of `a`
    a += 1    # Increment `a` by 1
# Output: 0 1 2 3 4
```

---

## **2. `break` and `continue` Statements**
### **`break`**
- The `break` statement is used to exit a loop before the condition becomes `False`.
- It is often used to terminate a loop based on a specific condition.

**Example:**
```python
a = 0
while a < 10:
    print(a)
    if a == 5:
        break  # Exit the loop when `a` equals 5
    a += 1
# Output: 0 1 2 3 4 5
```

### **`continue`**
- The `continue` statement skips the current iteration and proceeds to the next one.
- Useful when you want to ignore certain values but continue looping.

**Example:**
```python
a = 0
while a < 10:
    a += 1
    if a == 5:
        continue  # Skip the rest of the code for this iteration
    print(a)
# Output: 1 2 3 4 6 7 8 9 10 (5 is skipped)
```
---

## **3. Functions**
### **What is a Function?**
- A **function** is a reusable block of code that performs a specific task.
- Functions help make code modular, organized, and easier to debug.

### **Types of Functions**
1. **Built-in Functions**: Functions provided by Python, such as `print()`, `len()`, or `input()`.
2. **User-Defined Functions**: Functions you define yourself using the `def` keyword.

### **Syntax**
```python
def function_name(parameters):
    # Code block
    return value  # Optional
```

### **Examples**
1. **Function with a Single Parameter**
    ```python
    def area_of_circle(radius):
        return (22 / 7) * (radius ** 2)  # Calculate the area
    print(area_of_circle(7))  # Output: 154
    ```

2. **Function with Multiple Parameters**
    ```python
    def area_of_triangle(base, height):
        return (1 / 2) * base * height
    print(area_of_triangle(5, 7))  # Output: 17.5
    ```

3. **Function with No Parameters**
    ```python
    def greet():
        return "Hello, Nishchit!"
    print(greet())  # Output: Hello, Nishchit!
    ```

4. **Function with No Return Value**
    ```python
    def show_age():
        print("Your age is 20")
    show_age()  # Output: Your age is 20
    ```

---

## **4. Handling User Input**
- The `input()` function allows users to interact with the program by providing inputs.
- Use `int()` or `float()` to convert the input string into a number.

**Example:**
```python
num1 = int(input("Enter a number: "))
num2 = int(input("Enter another number: "))
print("Sum:", num1 + num2)
```

- To handle invalid inputs (like letters instead of numbers), use a `try-except` block:
    ```python
    try:
        num1 = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a number.")
    ```

---

## **What is a Library in Python?**
A **library** is a collection of pre-written code that you can use to perform specific tasks without writing the code from scratch. Libraries in Python consist of modules (files with Python code) that provide functions, classes, and variables for various purposes.

Think of a library as a toolbox: instead of building a hammer every time you need one, you can simply use the one from the toolbox.

---

## **Why Use Libraries?**
1. **Saves Time**: Libraries allow you to reuse existing solutions for common problems.
2. **Specialized Tools**: They provide specific functionalities like mathematical operations, file handling, data visualization, etc.
3. **Efficient Code**: Libraries are optimized for performance and reliability.
4. **Ease of Use**: Many libraries are well-documented and easy to integrate into your projects.

---

## **Types of Libraries in Python**
Python libraries can be broadly categorized into three types:

### **1. Standard Libraries**
- These are built into Python and do not require installation. You can directly import and use them in your code.
- Examples:
  - **`math`**: For mathematical operations like square roots, trigonometry, etc.
  - **`os`**: For interacting with the operating system (e.g., file handling, directory management).
  - **`datetime`**: For working with dates and times.

**Example:**
```python
import math
print(math.sqrt(16))  # Output: 4.0
```

---

### **2. Third-Party Libraries**
- These are developed by the Python community and need to be installed using a package manager like `pip`.
- Examples:
  - **`numpy`**: For numerical computations.
  - **`pandas`**: For data manipulation and analysis.
  - **`matplotlib`**: For data visualization.

**Example:**
```bash
# Install a library
pip install numpy
```
```python
import numpy as np
array = np.array([1, 2, 3])
print(array)  # Output: [1 2 3]
```

---

### **3. Custom Libraries**
- These are libraries you create yourself. If you have reusable functions or classes, you can package them into a module or library.
- **How to Create a Custom Library**:
  - Write your functions in a `.py` file (e.g., `my_library.py`).
  - Import and use it in other programs.

**Example:**
```python
# my_library.py
def greet(name):
    return f"Hello, {name}!"
```
```python
# main.py
import my_library
print(my_library.greet("Nishchit"))  # Output: Hello, Nishchit!
```

---

## **Using a Library**
- To use a library, you need to **import** it into your program using the `import` statement.

**Example:**
```python
import random  # Import the `random` library
print(random.randint(1, 10))  # Generate a random number between 1 and 10
```

Now that you understand what libraries are and the types of libraries in Python, we can move on to a specific example: the `random` library.

## **6. Random Operations**
The `random` module provides tools for generating random data.

### **Examples**
1. **Random Choice**
    ```python
    import random
    fruits = ['apple', 'banana', 'cherry']
    print(random.choice(fruits))  # Randomly selects a fruit
    ```

2. **Random Shuffle**
    ```python
    random.shuffle(fruits)
    print(fruits)  # Randomly shuffles the order of fruits
    ```

3. **Random Integer**
    ```python
    print(random.randint(1, 10))  # Random integer between 1 and 10
    ```

---

## **7. OS Module**
The `os` module allows interaction with the operating system.

### **Examples**
1. **Current Working Directory**
    ```python
    import os
    print(os.getcwd())  # Prints the path of the current directory
    ```

2. **List Files and Folders**
    ```python
    print(os.listdir())  # Lists all files and folders in the directory
    ```

3. **Create a Folder**
    ```python
    os.mkdir('new_folder')  # Creates a folder named 'new_folder'
    ```

---

## **8. Printing on the Same Line**
The `print()` function has a parameter `end` that specifies what to print at the end of a line. By default, it’s `\n` (newline).

### **Example**
```python
a = 1
while a <= 10:
    print(a, end=" ")  # Print on the same line with a space
    a += 1
# Output: 1 2 3 4 5 6 7 8 9 10
```

---

## **9. Special Characters in Strings**
Special characters like `\n` (newline) or `\t` (tab) are used to format strings.

**Example:**
```python
print("Line 1\nLine 2")  # Output:
# Line 1
# Line 2
```
