# Clean Code Refactoring Exercises

## Overview

**Objective:** Practice refactoring code to adhere to clean code principles and improve code quality.

## Goals

In this section, we aim to:

- Enhance readability and maintainability of code by applying clean code principles.
- Foster an understanding of the importance of refactoring in software development.
- Encourage the development of efficient and scalable code.

**Note:** Pay special attention to naming conventions, code simplicity, and separation of concerns throughout this exercise.

## Exercise

In this exercise, you will be given a series of code snippets that do not follow clean code principles. Your task is to refactor these snippets to improve their readability, maintainability, and performance.

### Exercise 1 - Variable Naming and Function Decomposition

```python
def calculate_sum(n):
    if n <= 0:
        return 0
    else:
        result = sum(range(n + 1))
        return result
```

### Exercise 2 - Loop Simplification and Conditionals

```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

### Exercise 3 - Exception Handling and Edge Cases

```python
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

### Exercise 4 - Modular Code and Reusability

```python
def print_numbers(n):
    for i in range(n):
        if is_prime(i):
            print(f"{i} is prime")
        else:
            print(f"{i} is not prime")
```

### Exercise 5 - Input Validation and Function Calls

```python
def main():
    num = int(input("Enter a number: "))
    sum_result = calculate_sum(num)
    factorial_result = factorial(num)
    print(f"Sum of numbers from 0 to {num}: {sum_result}")
    print(f"Factorial of {num}: {factorial_result}")
    print_numbers(num)
```

### Exercise 6 - Code Duplication and Modularization

```python
def main():
    num = int(input("Enter a number: "))
    sum_result = calculate_sum(num)
    factorial_result = factorial(num)
    print(f"Sum of numbers from 0 to {num}: {sum_result}")
    print(f"Factorial of {num}: {factorial_result}")
    print_numbers(num)
```

### Exercise 7 - Simplifying Conditional Blocks

```python
def calculate_sum(n):
    if n <= 0:
        return 0
    else:
        result = sum(range(n + 1))
        return result
```

### Exercise 8 - Optimizing Loop and Conditional Logic

```python
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
```

### Exercise 9 - Recursive Functions and Error Handling

```python
def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
```

### Exercise 10 - Main Function Refactoring

```python
import random
import sys
import os
import math

def main():
    num = int(input("Enter a number: "))
    sum_result = calculate_sum(num)
    factorial_result = factorial(num)
    print(f"Sum of numbers from 0 to {num}: {sum_result}")
    print(f"Factorial of {num}: {factorial_result}")
    print_numbers(num)
```

### Exercise 11 - Advanced Refactoring: Math Functions and Error Handling


```python
import math

def calculate_sum(n):
    if n <= 0:
        return 0
    elif n > 0 and n <= 10:
        result = 0
        for i in range(n):
            result += i
        return result
    elif n > 10 and n <= 50:
        result = 0
        for i in range(n):
            result += i
        return result
    elif n > 50 and n <= 100:
        result = 0
        for i in range(n):
            result += i
        return result
    else:
        result = 0
        for i in range(n):
            result += i
        return result

def is_prime(num):
    if num < 2:
        return False
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result

def print_numbers(n):
    for i in range(n):
        if is_prime(i):
            print(f"{i} is prime")
        else:
            print(f"{i} is not prime")

def calculate_power(x, y):
    if y < 0:
        return None
    elif y == 0:
        return 1
    else:
        result = 1
        for i in range(y):
            result *= x
        return result

def calculate_square_root(x):
    if x < 0:
        return None
    else:
        return math.sqrt(x)

def calculate_hypotenuse(a, b):
    if a < 0 or b < 0:
        return None
    else:
        return math.sqrt(a**2 + b**2)

def calculate_fibonacci(n):
    if n < 0:
        return None
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for i in range(2, n + 1):
            a, b = b, a + b
        return b

def calculate_factorial_sum(n):
    if n < 0:
        return None
    else:
        sum_result = 0
        for i in range(n + 1):
            sum_result += factorial(i)
        return sum_result

def calculate_exponential_sum(x, n):
    if n < 0:
        return None
    else:
        sum_result = 0
        for i in range(n + 1):
            sum_result += calculate_power(x, i) / factorial(i)
        return sum_result

def main():
    num = int(input("Enter a number: "))
    sum_result = calculate_sum(num)
    factorial_result = factorial(num)
    print(f"Sum of numbers from 0 to {num}: {sum_result}")
    print(f"Factorial of {num}: {factorial_result}")
    print_numbers(num)
    power_result = calculate_power(2, 3)
    square_root_result = calculate_square_root(16)
    hypotenuse_result = calculate_hypotenuse(3, 4)
    print(f"2^3 = {power_result}")
    print(f"Square root of 16: {square_root_result}")
    print(f"Hypotenuse of 3 and 4: {hypotenuse_result}")
    fibonacci_result = calculate_fibonacci(10)
    factorial_sum_result = calculate_factorial_sum(5)
    exponential_sum_result = calculate_exponential_sum(2, 5)
    print(f"Fibonacci sequence up to 10: {fibonacci_result}")
    print(f"Factorial sum up to 5: {factorial_sum_result}")
    print(f"Exponential sum of 2 up to 5 terms: {exponential_sum_result}")

if __name__ == "__main__":
    main()
```


## Wrapping Up

- After completing these exercises, you should have a better understanding of how to apply clean code principles to improve the readability, maintainability, and efficiency of code. Remember, clean code is not just about making code work; it's about making code work well for humans and machines alike.
- Be aware that if your mentor not understand the code, tomorrow in production code, you will have the same problem with another team member, so pay attention to the feedback and make the necessary changes.

## Action Items :pencil:

- **The Importence of Clean Code:** Discuss your mentor about the necceary of Clean Code and why it is so important.
- **Refactor for Readability:** Ensure your code is easily understandable at a glance. Use meaningful variable and function names, and break down complex functions into smaller, more manageable pieces.
- **Optimize for Maintainability:** Write code that is easy to modify and extend. This often means adhering to SOLID principles and avoiding unnecessary dependencies between components.
- **Improve Efficiency:** Where applicable, optimize your code for performance. However, do not compromise readability for the sake of marginal performance gains.
- **Embrace Refactoring:** View refactoring as an ongoing process, not a one-time task. As you learn more and your application evolves, continually refactor to maintain and improve code quality.
- **Seek Feedback:** Share your refactored code with peers or mentors. Getting feedback is invaluable for learning and improving your coding and refactoring skills.
