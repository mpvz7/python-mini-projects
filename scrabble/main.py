def main():
    dictionary = set()
    total_score = 0
    score_history = []

    # Open and read the file
    with open('words.txt') as f:
        words = f.read().splitlines()
        dictionary = set(words)

    # Map the letters to their scores
    letter_scores = {
        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3,
        'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
    }

    user_continue = True

    while user_continue:
        # Get the user input
        word = input('Enter your word: ').lower()
        
        # Check if the word is in the dictionary
        if word in dictionary:
            try:
                word_score = sum([letter_scores[letter] for letter in word])
                print(f'The score of the word "{word}" is {word_score}')
                total_score += word_score
                score_history.append((word, word_score))
            except KeyError:
                print("Error: The word contains invalid characters.")
        else:
            print(f'The word "{word}" is not in the dictionary.')
        
        # Ask the user if they want to continue
        user_continue = input('Do you want to continue? (y/n): ').strip().lower() == 'y'

    # Display the score history
    print("\nScore History:")
    for word, score in score_history:
        print(f'"{word}": {score}')

    print(f"Total score for all valid words: {total_score}")

if __name__ == '__main__':
    main()
