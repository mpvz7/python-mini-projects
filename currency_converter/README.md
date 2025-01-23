# Currency Converter

A command-line tool to convert a specified amount from one currency to another using real-time exchange rates fetched from the ExchangeRate-API. This project demonstrates how to make API requests, handle JSON data, and securely manage API keys.

---

## Features

- Converts between multiple currencies.
- Fetches real-time exchange rates using the ExchangeRate-API.
- Caches the latest rates to reduce API calls.
- Error handling for invalid inputs or API issues.
- Securely stores the API key using environment variables.

---

## Prerequisites

Before running the project, ensure you have the following:

1. **Python 3.8 or later** installed on your system.
2. Install the required libraries:
    - `python-dotenv`

---

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/mpvz7/currency_converter.git
   cd currency_converter
   ```

2. Install the required dependencies:

   ```bash
   pip install python-dotenv
   ```

3. Create a `.env` file to store your API key securely:

   ```bash
   echo "EXCHANGE_API_KEY=your_actual_api_key" > .env
   ```

   Replace `your_actual_api_key` with your API key from [ExchangeRate-API](https://www.exchangerate-api.com/).

---

## Usage

Run the `main.py` file:

```bash
python main.py
```

Follow the prompts:

1. Enter the base currency (e.g., `USD`).
2. Enter the target currency (e.g., `EUR`).
3. Enter the amount to convert.

### Example:

```plaintext
Welcome to the Currency Converter!

Enter the base currency (e.g., USD): USD
Enter the target currency (e.g., EUR): EUR
Enter the amount to convert: 100

Exchange rate (USD -> EUR): 0.91
Converted amount: 91.00 EUR
```

---

## API Key Management

To keep your API key secure:

1. Store your key in a `.env` file.
2. Add `.env` to your `.gitignore` file to prevent it from being pushed to version control.

Example `.gitignore`:

```plaintext
.env
\cache.json
```

---

## Notes

- If the API key is invalid or missing, the program will exit with an error.
- For better performance, the program caches the exchange rates and only updates them when needed.