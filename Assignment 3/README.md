# Assignment 3: Functions and modules in python

This assignment demonstrates the use of mathematical operations in Python through recursive functions and the built-in `math` module.

## Files Overview

### 1. Factorial.py
**Purpose:** Calculates the factorial of a given number using recursion.

**How it works:**
- Implements `factorial_recursive(num)` function that uses recursion to compute factorials
- Uses a base case: factorial of 0 and 1 equals 1
- For other numbers, uses the formula: `n! = n × (n-1)!`
- Includes validation to reject negative numbers (factorial is undefined for negatives)

**Usage:**
```bash
python Factorial.py
# Enter a positive integer when prompted
```

**Example:**
```
Enter a number to calculate its factorial: 5
The factorial of 5 is: 120
```

**Key Concepts:**
- Recursion and base cases
- Input validation
- Mathematical calculations

---

### 2. Math_module.py
**Purpose:** Demonstrates the use of Python's built-in `math` module to perform various mathematical operations.

**Functions:**
- `calculate_square_root(num)`: Computes the square root using `math.sqrt()`
  - Validates that the number is non-negative
  
- `calculate_logarithm(num)`: Computes the natural logarithm using `math.log()`
  - Validates that the number is positive
  
- `calculate_sine(num)`: Computes the sine of a number using `math.sin()`
  - Note: input is expected in radians

**Usage:**
```bash
python Math_module.py
# Enter a number when prompted
```

**Example:**
```
Enter a number : 16
The square root of 16 is: 4.0
The logarithm of 16 is : 2.772588722239781
The sine of 16 is : -0.28790331666170143
```

**Key Concepts:**
- Using Python's `math` module
- Input validation for mathematical operations
- Working with different mathematical functions

---

## Running the Programs

Both programs are interactive and require user input. To run them:

```bash
# For Factorial
python Factorial.py

# For Math Module Functions
python Math_module.py
```

## Requirements
- Python 3.x
- No external dependencies (both use only Python built-in libraries)

## Learning Outcomes
- Understanding recursion and its base cases
- Proper input validation for mathematical operations
- Familiarity with Python's `math` module
- Working with user input and formatted output
