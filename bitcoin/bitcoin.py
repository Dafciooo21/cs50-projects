#imports the necessary modules
import sys
import requests


#it checks if the command-line argument provided by the user is exactly 2 (the script name and the argument)
#it is converted to a float and passed to the btc_price function
def main():
    if len(sys.argv) == 2:

        try:
            n = float(sys.argv[1])
            print(btc_price(n))
        except ValueError:
            sys.exit("Command-line argument is not a number")

    else:
        sys.exit("Missing command-line argument")

#calculates the current price of a specified number of Bitcoins
#fetch the current price of 1 BTC in USD
def btc_price(num):
    try:
        response = requests.get(f"https://api.coindesk.com/v1/bpi/currentprice.json")
        result = response.json()
        price = result["bpi"]["USD"]["rate_float"]
        total = price * num
        return f"${total:,.4f}"
    except requests.RequestException:
        return None


main()
