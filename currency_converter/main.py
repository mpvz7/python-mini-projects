import requests
import json
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load environment variables
load_dotenv()
API_KEY = os.getenv("EXCHANGE_API_KEY")
API_URL = f'https://v6.exchangerate-api.com/v6/{API_KEY}/latest/'

CACHE_FILE = "cache.json"

def load_cache():
    """Load cached exchange rates from a file."""
    if os.path.exists(CACHE_FILE):
        with open(CACHE_FILE, 'r') as f:
            return json.load(f)
    return {"rates": {}, "timestamp": None}

def save_cache(data):
    """Save exchange rates and timestamp to cache."""
    with open(CACHE_FILE, 'w') as f:
        json.dump(data, f, indent=4)

def fetch_exchange_rates(base_currency):
    """Fetch exchange rates from API using API key."""
    try:
        print(f"Fetching exchange rates for {base_currency}...")
        
        response = requests.get(API_URL+base_currency)
        response.raise_for_status()
        data = response.json()
        return {"rates": data["conversion_rates"], "timestamp": datetime.now().isoformat()}
    except requests.exceptions.RequestException as e:
        print("Error fetching exchange rates:", e)
        return None

def get_exchange_rates(base_currency, cache_lifetime=24):
    """Get exchange rates from cache or API."""
    cache = load_cache()
    if cache["rates"] and cache["timestamp"]:
        cache_time = datetime.fromisoformat(cache["timestamp"])
        if datetime.now() - cache_time < timedelta(hours=cache_lifetime):
            print("Using cached exchange rates.")
            return cache["rates"]
    
    # Fetch new exchange rates and save to cache
    rates = fetch_exchange_rates(base_currency)
    if rates:
        save_cache(rates)
        return rates["rates"]
    else:
        return None

def convert_currency(amount, rate_from, rate_to):
    """Convert amount from one currency to another."""
    return amount * (rate_to / rate_from)

def main():
    print(API_URL)
    print("Welcome to the Currency Converter!")
    base_currency = "USD"  # Set a default base currency
    rates = get_exchange_rates(base_currency)
    if not rates:
        print("Unable to fetch exchange rates. Please try again later.")
        return

    next = True
    while next:
        # Get user inputs
        source_currency = input("Enter the source currency (e.g., USD): ").strip().upper()
        target_currency = input("Enter the target currency (e.g., EUR): ").strip().upper()
        try:
            amount = float(input("Enter the amount to convert: "))
        except ValueError:
            print("Invalid amount. Please enter a numeric value.")
            continue

        # Validate the currencies
        if source_currency not in rates or target_currency not in rates:
            print("Invalid currency code. Please try again.")
            continue

        # Perform the conversion
        converted_amount = convert_currency(amount, rates[source_currency], rates[target_currency])
        print(f"{amount:.2f} {source_currency} = {converted_amount:.2f} {target_currency}")

        # Ask if the user wants to continue
        next = input("Do you want to convert another currency? (y/n): ").strip().lower() == 'y'
            
    print("Thank you for using the currency converter!")

if __name__ == "__main__":
    main()