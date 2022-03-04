import requests
import json


def print_welcome_message():
    print("Welcome to the Banker app! The application has two modes of operation. \n "
          "[1] Checking the current exchange rate of the selected currency. \n "
          "[2] Currency converter.")


def select_currency():
    user_code = input("What currency do you want to check?\n"
                      "[USD, CHF, EUR, UAH, RBL]: ")
    return user_code


def get_currency_price(user_code):
    code = user_code
    response_API = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{code}/?format=json")
    json_data = response_API.text
    return json_data


def print_currency_data(json_data):
    data = json_data
    parse_json = json.loads(data)
    print("Date:", parse_json['rates'][0]['effectiveDate'])
    print("AVG Price [PLN]:", parse_json['rates'][0]['mid'])


def exchange_checker_mode():
    currency = select_currency()
    price = get_currency_price(currency)
    return print_currency_data(price)


def converter_mode():
    pass


def select_mode():
    mode = input("Which operating mode do you choose? [Enter 1 or 2]: ")
    if mode == "1":
        print("Welcome to the exchange rate checker mode.")
        exchange_checker_mode()
    if mode == "2":
        print("Welcome to the currency conventer mode.")
        converter_mode()


if __name__ == "__main__":
    print_welcome_message()
    select_mode()
