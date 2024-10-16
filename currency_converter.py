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

def get_currencies():
    response = requests.get(f"{BASE_URL}currencies?apikey={API_KEY}")

    for key, val in response.json()['data'].items():
        print(key, val["symbol"], val["name"])


def main():
    setup()
    get_currencies()

if __name__ == "__main__":
    main()