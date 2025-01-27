# RSS Reader

The **RSS Reader** is a simple command-line application that allows you to fetch, read, and manage RSS feeds. It supports reading articles from multiple feeds, marking articles as read, and saving this information for future use.

---

## Features

- **Support for multiple feeds**: Enter multiple RSS feed URLs, and the program fetches the latest articles from each feed.  
- **Mark articles as read**: Avoid re-reading articles by marking them as read, with progress saved in a local JSON file (`read_articles.json`).  
- **Article summaries**: Displays the title, link, and description of each article for quick consumption.  
- **Error handling**: Gracefully handles invalid URLs, parsing errors, and network issues.  

---

## How to Use

1. **Install required libraries**:  
   Ensure you have Python installed. You also need the `requests` library, which you can install using pip:  
   ```bash
   pip install requests
   ```

2. **Run the program**:  
   Save the code as `rss_reader.py` and execute it from the terminal:  
   ```bash
   python rss_reader.py
   ```

3. **Enter RSS Feed URLs**:  
   When prompted, input one or more RSS feed URLs separated by commas. Example:  
   ```
   https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml, https://feeds.bbci.co.uk/news/rss.xml
   ```

4. **Interact with the program**:  
   - View articles one by one with their title, link, and description.  
   - Mark articles as read to skip them in future sessions.  
   - Exit the program, and your progress will be saved.

---

## File structure

- **rss_reader.py**: The main program.  
- **read_articles.json**: Stores the titles of articles you've marked as read.  

---

## Example output

```
Welcome to the RSS Reader!

Enter RSS feed URLs separated by commas: https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml

Fetching feed from https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml...

Title: Example Article Title
Link: https://example.com/article
Description: This is a short description of the article.

Mark this article as read? (y/n): y

Thank you for using the RSS Reader!
```

---

## Dependencies

- **Python** (>=3.6)  
- **Libraries**:  
  - `requests` (for fetching RSS feeds)  
  - `xml.etree.ElementTree` (for parsing XML data)  

Install dependencies using pip:  
```bash
pip install requests
```

---

## Improvements

- **Enhanced Parsing**: Use `feedparser` for better handling of complex RSS feeds.  
- **Favorite Articles**: Add functionality to save favorite articles in a separate file.  
- **GUI Version**: Build a graphical interface using `tkinter` or `PyQt`.  
- **Categories**: Group articles by categories or tags.