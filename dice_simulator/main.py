import random

def get_dice_type():
    """Prompt the user to select a dice type and validate the input."""
    dice_type = ""
    while not (dice_type.startswith('D') and dice_type[1:].isdigit()):
        dice_type = input("Choose your dice type (e.g., D6, D12, D20): ").upper()
        if not (dice_type.startswith('D') and dice_type[1:].isdigit()):
            print("Invalid input. Please enter a valid dice type like D6, D12, D20.")
    return dice_type

def get_number_of_rolls(dice_type):
    """Prompt the user to enter the number of rolls and handle non-integer inputs."""
    num_rolls = 0
    while num_rolls <= 0:
        try:
            num_rolls = int(input(f"How many times would you like to roll the {dice_type}? "))
            if num_rolls <= 0:
                print("Please enter a positive integer.")
        except ValueError:
            print("Invalid input. Please enter a positive integer.")
    return num_rolls

def roll_dice(dice_type, num_rolls):
    """Simulate rolling the dice of the specified type and number of times."""
    sides = int(dice_type[1:])
    rolls = [random.randint(1, sides) for _ in range(num_rolls)]
    total = sum(rolls)
    
    print(f"\nRolling the {dice_type}...")
    print("You rolled: ", ", ".join(map(str, rolls)))
    print(f"Total: {total}")
    
    return (dice_type, rolls, total)

def display_history(history):
    """Display the roll history."""
    print("\nRoll History:")
    for dice_type, rolls, total in history:
        print(f"{dice_type}: {', '.join(map(str, rolls))} (Total: {total})")

def dice_simulator():
    """Main function to simulate dice rolls and manage user interaction."""
    print("Welcome to the Dice Simulator!")
    history = []
    continue_rolling = True

    while continue_rolling:
        dice_type = get_dice_type()
        num_rolls = get_number_of_rolls(dice_type)
        roll_result = roll_dice(dice_type, num_rolls)
        history.append(roll_result)
        
        if input("\nDo you want to see the roll history? (y/n): ").lower() == 'y':
            display_history(history)
        
        continue_rolling = input("\nDo you want to roll another dice? (y/n): ").lower() == 'y'
        
    print("\nThank you for using the Dice Simulator!")

if __name__ == "__main__":
    dice_simulator()
