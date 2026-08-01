# Assignment 3: Factorial and Math Module Programs

This assignment contains two Python programs that demonstrate recursion and the use of Python's built-in `math` module.

## Files

### 1. Factorial.py
A program that calculates the factorial of a given number using **recursive function**.

**Features:**
- Takes a non-negative integer as input from the user
- Uses a recursive approach to calculate factorial
- Handles edge cases (negative numbers, 0, and 1)
- Displays the calculated factorial value

**How to run:**
```bash
python Factorial.py
```

**Example:**
```
Enter a non-negative integer to calculate it's factorial: 5
The factorial of 5 is 120
```

**Key Concepts:**
- Recursion: Function calling itself to solve a problem
- Base case: Condition to stop recursion (n == 0 or n == 1)
- Error handling: Checks for invalid inputs

---

### 2. Math_module.py
A program that demonstrates mathematical operations using Python's `math` module.

**Features:**
- Takes a number as input from the user
- Calculates three mathematical operations:
  1. **Square Root** - Returns the square root of the number
  2. **Logarithm** - Returns the natural logarithm of the number
  3. **Sine** - Returns the sine value of the number (in radians)
- Includes validation for domain-specific constraints

**How to run:**
```bash
python Math_module.py
```

**Example:**
```
Enter a number : 16
The square root of 16 is 4.0
The logarithm of 16 is 2.772588722239781
The sine of 16 is -0.28790331666062016
```

**Key Concepts:**
- Importing modules: Using `import math`
- Math functions: `math.sqrt()`, `math.log()`, `math.sin()`
- Input validation: Checking constraints before calculations

---

## Learning Objectives

✅ Understanding recursion and how functions call themselves  
✅ Working with Python's built-in `math` module  
✅ Input validation and error handling  
✅ Writing functions with clear logic and documentation  
✅ Using formatted strings (f-strings) for output  

---

## Requirements

- Python 3.x
- No external libraries required (uses only the built-in `math` module)

---

## Notes

- Both programs accept user input, so ensure you provide valid numeric inputs
- For Factorial.py: Use non-negative integers only
- For Math_module.py: Be careful with domain constraints (e.g., negative numbers for logarithm)
