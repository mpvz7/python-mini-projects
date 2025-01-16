import random
import string

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    
    chars = string.ascii_lowercase
    password = ''

    # Add at least one of each type of character
    if use_uppercase:
        password += random.choice(string.ascii_uppercase)
        chars += string.ascii_uppercase
    if use_digits:
        password += random.choice(string.digits)
        chars += string.digits
    if use_special_chars:
        password += random.choice(string.punctuation)
        chars += string.punctuation
            
    # Add random characters to the remaining length
    for _ in range(length-len(password)):
        password += random.choice(chars)
    
    return password

def main():
    input("Welcome to the Password Generator. Press Enter to continue...")
    
    password_valid = False

    while password_valid == False:
        
        # User input for preferences
        length = int(input("\nEnter the length of the password: "))
        use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Use digits? (y/n): ").lower() == 'y'
        use_special_chars = input("Use special characters? (y/n): ").lower() == 'y'
        
        #Check if the password length is enough
        if length > use_uppercase + use_digits + use_special_chars:
            print("The password length must be greater than the number of uppercase letters, digits, and special characters")
            password_valid = True
    
    password = generate_password(length, use_uppercase, use_digits, use_special_chars)
    
    print(f"\nYour password is: {password}")
    
    # Save the password to a file
    save = input("\nDo you want to save this password to a file? (y/n): ").lower() == 'y'
    if save:
        with open("generated_password.txt", "w") as file:
            file.write(password)
            print("Password saved to generated_password.txt")

if __name__ == "__main__":
    main()