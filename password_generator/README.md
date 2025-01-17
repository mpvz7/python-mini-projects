# Password Generator

This is a simple Python project that generates secure, random passwords of varying lengths and complexities. You can customize the password by including or excluding special characters, digits, and uppercase letters.

## Features
- Generate random passwords with a customizable length.
- Include or exclude special characters, numbers, and uppercase letters.
- Option to save generated passwords in a file.

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/mpvz7/python-mini-projects.git

2. Navigate to the project directory:
   ```bash
   cd python-mini-projects/password_generator
   ```

## Usage

1. Run the `main.py` script:
   ```bash
   python main.py
   ```

2. The program will prompt you for:
   - The length of the password.
   - Whether you want to include uppercase letters, digits, and special characters.
   
3. It will then generate and display a random password based on your input.

4. (Optional) If you'd like to save the password, the program will offer an option to save it to a file.

## Example Output

```
Welcome to the Password Generator!

Enter the length of the password: 12
Use uppercase letters? (y/n): y
Use digits? (y/n): y
Use special characters? (y/n): y

Your password is: Z1]ErnF5B!%1

Do you want to save this password to a file? (y/n): y
Password saved to generated_password.txt
```

## Code Explanation

The `main.py` file uses the Python `random` module to generate a secure password. It takes user input to customize the password's characteristics and then randomly selects characters from appropriate sets (letters, numbers, special characters) to form the password. If an option is selected, it ensures that the corresponding character type appears at least once in the generated password.

## Contributing

Feel free to contribute by submitting issues or creating pull requests.