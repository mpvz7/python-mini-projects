# Text Analyzer

A Python program that analyzes a text file for:

- The total number of words.
- The total number of sentences.
- The most frequent words and their counts.

This program helps to quickly extract insights from any text document. It also provides an optional visualization of the most frequent words using a bar chart.

---

## Features
- **Word count**: Counts the total words in the file.
- **Sentence count**: Counts the total sentences.
- **Most frequent words**: Displays the top 10 most frequently occurring words.
- **Stop words exclusion**: Removes common stop words (like "the", "and", etc.) to focus on meaningful words.
- **Graphical representation**: Visualizes the most frequent words in a bar chart.
- **File format support**: Works with `.txt` files and optionally `.md` files.

---

## **Setup and Installation**

### Prerequisites:
1. **Python 3.6 or higher**.
2. Install `matplotlib`:
   ```bash
   pip install matplotlib
   ```

### Optional:
Create a `stop_words.txt` file in the project directory to include common words you'd like to exclude. Example:

```
the
and
a
an
in
on
of
to
with
at
from
by
for
```

---

## **How to Run the Program**
1. Clone this repository or download the script file.
2. Place the text file you want to analyze in the same directory as the script (e.g., `sample.txt`).
3. Run the program:
   ```bash
   python text_analyzer.py
   ```
4. Follow the prompts:
   - Enter the path to the text file (e.g., `sample.txt`).
   - Choose whether to visualize the most frequent words.

---

## **Example Usage**

### Input File:
Sample text (`sample.txt`):
```
The quick brown fox jumps over the lazy dog. The dog was not amused.
```

### Program Output:
```
Welcome to the Text Analyzer!

Enter the path to the text file to analyze: sample.txt

Analysis Results:
- Total words: 11
- Total sentences: 2
- Most common words:
  the: 3
  dog: 2
  quick: 1
  brown: 1
  fox: 1
  jumps: 1
  over: 1
  lazy: 1
  was: 1
  not: 1

Would you like to see a bar chart of the word frequencies? (y/n): y
```

### Bar Chart:
Displays a bar chart of the top 10 most frequent words.

---

## **File Structure**
```
project-directory/
├── main.py                # Main Python script
├── stop_words.txt         # (Optional) Stop words file
├── sample.txt             # Sample text file for testing
```

---

## **Concepts Learned**
This project demonstrates:
- File handling (reading `.txt` files).
- String manipulation for text analysis.
- Using dictionaries for word frequency counting.
- Excluding stop words for meaningful results.
- Generating bar charts with `matplotlib`.