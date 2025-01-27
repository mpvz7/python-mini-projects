import requests
import xml.etree.ElementTree as ET
import os
import json

# File to store read articles
READ_ARTICLES_FILE = "read_articles.json"

# Load previously read articles
def load_read_articles():
    if not os.path.exists(READ_ARTICLES_FILE):
        return set()
    with open(READ_ARTICLES_FILE, "r") as file:
        return set(json.load(file))

# Save read articles
def save_read_articles(read_articles):
    with open(READ_ARTICLES_FILE, "w") as file:
        json.dump(list(read_articles), file)

# Fetch and parse RSS feed
def fetch_rss_feed(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return ET.fromstring(response.content)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching RSS feed: {e}")
        return None

# Display articles from the RSS feed
def display_feed(feed, read_articles):
    items = feed.findall(".//item")
    for item in items:
        title = item.find("title").text
        link = item.find("link").text
        description = item.find("description").text

        if title in read_articles:
            continue

        print(f"\nTitle: {title}")
        print(f"Link: {link}")
        print(f"Description: {description}\n")

        mark_as_read = input("Mark this article as read? (y/n): ").strip().lower()
        if mark_as_read == "y":
            read_articles.add(title)

# Main function
def main():
    print("Welcome to the RSS Reader!")

    # Load previously read articles
    read_articles = load_read_articles()

    # Get RSS feed URLs from the user
    urls = input("Enter RSS feed URLs separated by commas: ").split(",")

    for url in urls:
        url = url.strip()
        print(f"\nFetching feed from {url}...\n")
        feed = fetch_rss_feed(url)
        if feed is not None:
            display_feed(feed, read_articles)
        else:
            print(f"Could not fetch or parse feed from {url}.")

    # Save updated read articles
    save_read_articles(read_articles)
    print("\nThank you for using the RSS Reader!")

if __name__ == "__main__":
    main()
