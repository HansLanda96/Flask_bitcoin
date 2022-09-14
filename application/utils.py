import requests


def get_rate():
    req = requests.get('https://bitpay.com/api/rates')
    return req.json()


def currency_input(currency: str):
    data = get_rate()
    for item in data:
        if item['code'].lower() == currency.lower() or item['name'].lower() == currency.lower():
            rate = item
            return rate
