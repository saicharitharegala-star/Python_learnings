# Assignment 6: Tkinter Calculator

This assignment demonstrates a simple GUI calculator built with Python's `tkinter` library.

## Files

- `tkinter_calculator.py`
  - A graphical calculator application with buttons for digits, basic arithmetic operations, clear, and equals.

## What it does

- Creates a `tkinter` window sized 500x500
- Displays a text entry field for input and results
- Provides buttons for digits `0` through `9`
- Supports addition, subtraction, multiplication, and division
- Clears the display with a `clear` button
- Evaluates the entered expression when the `=` button is pressed

## Key concepts

- `tkinter` GUI creation
- Widgets: `Button`, `Entry`, `Tk`
- Event handling with `command`
- Basic arithmetic logic and state management

## How to run

1. Open a terminal and navigate to this folder.
2. Run the script with Python:
   ```bash
   python tkinter_calculator.py
   ```

## Notes

- This calculator works with integer input only.
- Division uses Python's `/` operator, which returns a float when the result is not whole.
- The app stores the first operand and operation until `=` is pressed.
