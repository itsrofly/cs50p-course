import requests
import sys
import json

# Expects the user to specify as a command-line argument the number of Bitcoins, that they would like to buy. If that argument cannot be converted to a float, the program should exit via sys.exit with an error message.

def main():
    if len(sys.argv) < 2:
        sys.exit("Missing command-line argument")
    else:
        try:
            buyprice = convert_bitcoin(float(sys.argv[1]))
            print(buyprice)
        except:
            sys.exit("Command-line argument is not a number")

# Queries the API for the CoinDesk Bitcoin Price Index at https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object, among whose nested keys is the current price of Bitcoin as a float. Be sure to catch any exceptions, as with code like:

def convert_bitcoin(n):
    try:
        bitcoin = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json").json()

        btc = float(bitcoin["bpi"]["USD"]["rate"].replace(",", ""))
        price = btc * n
        return f"${price:,.4f}"
    except requests.RequestException as error: # New discovery, as, we can refer to a error
        print(error)


if __name__ == "__main__":
    main()