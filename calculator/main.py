def calculator(op, num1, num2=0):
    if op == 'add':
        return num1 + num2
    elif op == 'sub':
        return num1 - num2
    elif op == 'mult':
        return num1 * num2
    elif op == 'div':
        return "Error: Division by zero." if num2 == 0 else num1 / num2
    elif op == 'pow':
        return num1 ** num2
    elif op == 'sqrt':
        return "Error: Cannot take the square root of a negative number." if num1 < 0 else num1 ** 0.5

def main():
    print('Welcome to the calculator!')
    history = []
    
    next_calculation = True
    while next_calculation:
        op = input('\nChoose an operator: add, sub, mult, div, pow, sqrt, history: ').strip().lower()
        
        if op == 'history':
            print("\nCalculation History:")
            for record in history:
                print(f"{record[0]}({record[1]}, {record[2]}) = {record[3]}" if record[0] != 'sqrt' else f"{record[0]}({record[1]}) = {record[3]}")
        else:
        
            if op not in ['add', 'sub', 'mult', 'div', 'pow', 'sqrt']:
                print("Error: Invalid operator.")
                continue
            
            try:
                num1 = float(input('Enter first number: '))
                num2 = float(input('Enter second number: ')) if op != 'sqrt' else 0
                result = calculator(op, num1, num2)
                print(f"Result: {result}")
                history.append((op, num1, num2, result))
            except ValueError:
                print("Error: Please enter valid numbers.")
            
        next_calculation = input("\nDo you want to perform another calculation? (y/n): ").strip().lower() == 'y'
    
    print('\nGoodbye!')

if __name__ == "__main__":
    main()
