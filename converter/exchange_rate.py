import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"

def get_exchange_rates():
    response = requests.get(API_URL)
    data = response.json()
    return data['rates']
