# Basic Calculator

A command-line calculator that performs basic arithmetic operations such as addition, subtraction, multiplication, and division. It also supports advanced operations like exponentiation and square root and keeps a history of all calculations.

## Features

- **Basic Operations**: Addition, subtraction, multiplication, and division.
- **Advanced Operations**: Exponentiation and square root.
- **Error Handling**: Handles invalid inputs and division by zero using `try/except`.
- **History**: Keeps a record of all calculations performed during the session.

## Concepts Learned

- **Functions**: Modular code structure using functions for each operation.
- **Error Handling**: Using `try/except` blocks to handle input errors and exceptions.
- **Input/Output**: Taking user input and displaying results on the command line.

## How to Use

1. Run the program in a command-line interface.
2. Enter the type of operation you want to perform when prompted.
3. Enter the numbers when asked.
4. View the result of the calculation.
5. Continue with more calculations or view the history of past calculations.

## Example Usage

```plaintext
Welcome to the calculator!

Choose an operator: add, sub, mult, div, pow, sqrt, history: sqrt
Enter first number: 25
Result: 5.0

Do you want to perform another calculation? (y/n): y

Choose an operator: add, sub, mult, div, pow, sqrt, history: history

Calculation History:
sqrt(25.0) = 5.0

Do you want to perform another calculation? (y/n): n

Goodbye!
```

## Future Enhancements

- Implement support for more complex mathematical functions like logarithms or trigonometric functions.
- Add a graphical user interface (GUI) version of the calculator.