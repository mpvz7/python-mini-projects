import json
import random

def main():
    
    try: 
        # Load the quotes from JSON file
        with open('quotes.json') as f:
            quotes = json.load(f)
    except FileNotFoundError:
        quotes = []
            
    # Get the user input
    print("Welcome to Quote Generator!")
    user_continue = True
    while user_continue:
        user_choice = input("\nChoose a number :\n1. Generate a random quote.\n2. Add a new quote.\n3. View all quotes.\n4. Exit the program.\n").strip()
        
        if user_choice == '1':
            # Get a random quote
            if quotes:
                quote = random.choice(quotes)
                print(f'\n"{quote["quote"]}"')
                print(f'-- {quote["category"]}')
            else:
                print("\nNo quotes available. Please add some quotes first.")
            
        elif user_choice == '2':
            # Add a new quote
            new_quote = input("Enter the quote: ").strip()
            new_category = input("Enter the category: ").strip()
            quotes.append({"quote": new_quote, "category": new_category})
            
            # Writing to the JSON file
            with open('quotes.json', 'w') as file:
                json.dump(quotes, file, indent=4)
            print("Quote added successfully!")
            
        elif user_choice == '3':
            # View all quotes
            if quotes:
                for i, quote in enumerate(quotes, 1):
                    print(f'{i}. "{quote["quote"]}"')
                    print(f'-- {quote["category"]}\n')
            else:
                print("\nNo quotes to display. Please add some quotes first.")
                
        elif user_choice == '4':
            # Exit the program
            print("Thank you for using Quote Generator!")
            user_continue = False
            
        else:
            print("\nInvalid choice. Please try again.")
            continue


if __name__ == '__main__':
    main()