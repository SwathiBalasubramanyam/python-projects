import requests

from pprint import PrettyPrinter

BASE_URL = "https://api.freecurrencyapi.com/v1/"
API_KEY = None

def setup():
    global API_KEY

    with open("currency_converter_api.txt", 'r') as api_file:
        API_KEY = api_file.readline().strip()

    if not API_KEY:
        raise Exception("API key not found, add currency_converter_api.txt file with the API key to your current directory")

    response = (requests.get(f"{BASE_URL}status?apikey={API_KEY}")).json()
    if not response['quotas']['month']['remaining']:
        raise Exception("API quota over for the month, retry later")

def get_conversion_rates(curr_code):
    res = requests.get(f"{BASE_URL}latest?apikey={API_KEY}&currencies={curr_code}")
    print(f"One USD is approximately equivalent to {res.json()['data'][curr_code]} {curr_code}")

def get_currencies():
    response = requests.get(f"{BASE_URL}currencies?apikey={API_KEY}")

    currency_data = response.json()['data']

    for key, val in currency_data.items():
        print(key, val["symbol"], val["name"])

    while True:
        base_currency = input("Please enter the base currency for which you want to get the conversion rate or type Q to quit: ")

        if base_currency in ["Q", "q"]:
            return

        if base_currency not in currency_data:
            continue

        get_conversion_rates(base_currency)


def main():
    setup()
    get_currencies()

if __name__ == "__main__":
    main()