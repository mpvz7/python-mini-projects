# Scrabble Checker

## Overview

The **Scrabble Checker** is a Python program that verifies if a given word is valid in Scrabble based on a dictionary and calculates the corresponding Scrabble score for the word.

## Features

- **Word validation**: Checks if a word exists in a provided Scrabble dictionary.
- **Score calculation**: Computes the Scrabble score based on the letters in the word.
- **Custom dictionary**: Allows the use of a custom word list for validation.

## Concepts Learned

- **Dictionaries**: Used for storing letter scores and validating words.
- **File handling**: Reads the word list from a text file to verify word validity.
- **Loops and conditions**: Utilized to process input and calculate scores.

## How to Use

1. **Prepare the Dictionary**:
   - Ensure you have a dictionary file (`dictionary.txt`) with valid Scrabble words, each word on a new line.

2. **Run the Program**:
   - Execute the program using a Python environment:
     ```bash
     python scrabble_checker.py
     ```

3. **Input a Word**:
   - Enter a word when prompted. The program will:
     - Check if the word is valid.
     - Calculate and display the Scrabble score if the word is valid.

4. **Invalid Words**:
   - If the word is not in the dictionary, the program will indicate it is invalid.

## Example

```bash
Enter your word: apple
The score of the word "apple" is 9
Do you want to continue? (y/n): y
Enter your word: mouse
The word "mouse" is not in the dictionary.
Do you want to continue? (y/n): y
Enter your word: computer
The score of the word "computer" is 14
Do you want to continue? (y/n): n

Score History:
"apple": 9
"computer": 14
Total score for all valid words: 23
```