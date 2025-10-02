# Frankfurter exchange rate API and conversion

import requests

def get_rate(usd, eur):
    try:
        response = requests.get(f"https://api.frankfurter.dev/v1/latest?base={usd}&symbols={eur}", timeout=5)
        response.raise_for_status()
        data = response.json()
        rate = data["rates"][eur]

        return rate

    except requests.exceptions.RequestException:
        print("Error getting exchange rate")
        return None

# Convert USD to EUR, return Nan if can't fetch rate    
def convert(amount):
    rate = get_rate("USD", "EUR")
    if rate is not None:
        return amount * rate
    else:
        return float("nan")