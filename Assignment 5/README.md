# Assignment 5: Lists and Dictionaries

This assignment covers fundamental Python concepts for working with lists and dictionaries.

## Files

### 1. **List_slicing.py**
Demonstrates list slicing and manipulation operations.

**What it does:**
- Creates a list of numbers from 1 to 10
- Extracts the first five elements using list slicing
- Reverses the extracted elements using slice notation
- Prints all three lists for comparison

**Key concepts:**
- List creation with `range()`
- List slicing with `[:5]` syntax
- Reversing lists with `[::-1]` syntax

**Output example:**
```
Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Extracted list (first 5 elements): [1, 2, 3, 4, 5]
Reversed extracted list: [5, 4, 3, 2, 1]
```

### 2. **Students_marks.py**
Demonstrates dictionary operations and user input handling.

**What it does:**
- Stores student names and their marks in a dictionary
- Prompts the user to enter a student's name
- Searches for the student in the dictionary
- Displays the student's marks if found, or an error message if not

**Key concepts:**
- Creating dictionaries with key-value pairs
- Taking user input with `input()`
- Checking if a key exists in a dictionary with `in` operator
- Accessing dictionary values by key

**Sample data:**
- Alice: 98
- John: 89
- Simpson: 78
- Sai: 100

**Example usage:**
```
Enter the name of the student: alice
alice's marks: 98
```

## How to Run

1. Navigate to the Assignment 5 folder
2. Run the desired file using Python:
   ```bash
   python List_slicing.py
   python Students_marks.py
   ```

## Learning Objectives

- Understand and apply list slicing techniques
- Work with dictionaries for data storage and retrieval
- Handle user input and conditional logic
- Use string formatting in print statements
