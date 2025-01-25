import string
from collections import Counter
import matplotlib.pyplot as plt

def load_stop_words(file='stop_words.txt'):
    """Load stop words from a file."""
    try:
        with open(file, 'r') as f:
            return set(word.strip().lower() for word in f)
    except FileNotFoundError:
        print(f"Stop words file '{file}' not found. Proceeding without it.")
        return set()

def analyze_text(file_path, stop_words):
    """Analyze the text file for word count, sentence count, and word frequency."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
    except FileNotFoundError:
        print(f"File '{file_path}' not found.")
        return None

    # Normalize text: lowercased and stripped of punctuation
    translator = str.maketrans('', '', string.punctuation)
    words = text.translate(translator).lower().split()
    sentences = text.split('.')
    
    # Remove stop words
    words = [word for word in words if word not in stop_words]

    # Calculate word frequencies
    word_counts = Counter(words)
    
    return {
        "word_count": len(words),
        "sentence_count": len([s for s in sentences if s.strip()]),
        "most_common_words": word_counts.most_common(10),
        "word_counts": word_counts
    }

def plot_word_frequency(word_counts):
    """Plot the most frequent words using a bar chart."""
    words, counts = zip(*word_counts.most_common(10))
    plt.bar(words, counts, color='skyblue')
    plt.title("Top 10 Most Frequent Words")
    plt.xlabel("Words")
    plt.ylabel("Frequency")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    print("Welcome to the Text Analyzer!")
    file_path = input("Enter the path to the text file to analyze: ").strip()
    stop_words = load_stop_words()  # Load stop words from file
    
    result = analyze_text(file_path, stop_words)
    if result:
        print("\nAnalysis Results:")
        print(f"- Total words: {result['word_count']}")
        print(f"- Total sentences: {result['sentence_count']}")
        print("- Most common words:")
        for word, count in result['most_common_words']:
            print(f"  {word}: {count}")
        
        if input("\nWould you like to see a bar chart of the word frequencies? (y/n): ").strip().lower() == 'y':
            plot_word_frequency(result["word_counts"])

if __name__ == "__main__":
    main()