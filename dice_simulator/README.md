# Dice Simulator

The Dice Simulator is a Python program that simulates the rolling of different types of dice, such as a D6 (six-sided dice), D20 (twenty-sided dice), D12 (twelve-sided dice), and others. This simulator allows users to choose the type of dice, roll multiple times, and view the total of their rolls. It also keeps a history of all rolls made during the session.

## Features

- Select from various types of dice (D6, D12, D20, etc.).
- Perform multiple rolls and view the total of all rolls.
- Keep an ongoing history of all rolls during the session.
- Simple text-based user interface.

## How to Use

1. Run the script to start the dice simulator.
2. Choose the type of dice you want to roll (e.g., D6 for six-sided dice).
3. Specify the number of times you want to roll the selected dice.
4. View the result of each roll and the total.
5. The program keeps a history of all your rolls, which you can view at any time.
6. Repeat the process or exit the program.

## Requirements

- Python 3.x

## Running the Program

To run the Dice Simulator, execute the following command in your terminal:

```bash
python main.py
```

## Example

```bash
Welcome to the Dice Simulator!
Choose your dice type (e.g., D6, D12, D20): D6
How many times would you like to roll the D6? 3

Rolling the D6...
You rolled:  5, 3, 5
Total: 13

Do you want to see the roll history? (y/n): n

Do you want to roll another dice? (y/n): y
Choose your dice type (e.g., D6, D12, D20): D12
How many times would you like to roll the D12? 5

Rolling the D12...
You rolled:  8, 1, 4, 7, 6
Total: 26

Do you want to see the roll history? (y/n): y

Roll History:
D6: 5, 3, 5 (Total: 13)
D12: 8, 1, 4, 7, 6 (Total: 26)

Do you want to roll another dice? (y/n): n

Thank you for using the Dice Simulator!
```

## Concepts Learned

- **Random Number Generation**: Using Python's `random` module to simulate dice rolls.
- **Functions**: Encapsulating logic in functions for modular code.
- **Lists**: Storing and manipulating roll results and history.
- **Errors**: Handling input's errors.

## Contributing

Contributions are welcome! Feel free to submit issues or pull requests to enhance the functionality of the Dice Simulator.