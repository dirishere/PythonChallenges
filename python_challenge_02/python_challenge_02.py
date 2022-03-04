import requests
import json

global currency_code
global user_code
global user_amount


def print_welcome_message():
    print("Welcome to the Banker app! The application has two modes of operation. \n "
          "[1] Checking the current exchange rate of the selected currency. \n "
          "[2] Currency converter.")


def select_currency():
    global user_code
    is_selected = False
    while not is_selected:
        codes = ['USD', 'CHF', 'EUR', 'UAH', 'RBL']
        user_code = input("What currency do you want to check? [USD, CHF, EUR, UAH, RBL]: ")
        if user_code.upper() not in codes:
            print("Currency not supported. Try again: ")
        else:
            is_selected = True
    return user_code


def provide_amount_to_convert():
    global user_amount
    try:
        user_amount = int(input("Enter the amount to be converted [PLN]: "))
    except ValueError:
        print("This value should be a number. Come back when you understand what you are doing...")
        exit(-2)
    return user_amount


def get_currency_price(provided_currency_code):
    global currency_code
    currency_code = provided_currency_code
    if provided_currency_code.upper() == "RBL":
        print("Make pace, not war. Currency is not supported!")
        exit(-2)
    else:
        response_API = requests.get(f"http://api.nbp.pl/api/exchangerates/rates/a/{currency_code}/?format=json")
        json_data = response_API.text
        return json_data


def print_currency_data(json_data):
    parse_json = json.loads(json_data)
    print("Date:", parse_json['rates'][0]['effectiveDate'])
    print("AVG Price [PLN]:", parse_json['rates'][0]['mid'])


def data_to_calculate(json_data):
    parse_json = json.loads(json_data)
    return float(parse_json['rates'][0]['mid'])


def print_calculated_price(calculated_price):
    print(f"Amount after conversion [{currency_code.upper()}]:", round(calculated_price, 2))


def exchange_checker_mode():
    currency = select_currency()
    price = get_currency_price(currency)
    return print_currency_data(price)


def converter_mode():
    currency = select_currency()
    json_data = get_currency_price(currency)
    price_to_calculate = data_to_calculate(json_data)
    calculated_price = provide_amount_to_convert()/price_to_calculate
    return print_calculated_price(calculated_price)


def select_mode():
    mode = input("Which operating mode do you choose? [Enter 1 or 2]: ")
    if mode == "1":
        print("Welcome to the exchange rate checker mode.")
        exchange_checker_mode()
    if mode == "2":
        print("Welcome to the currency converter mode.")
        converter_mode()


if __name__ == "__main__":
    print_welcome_message()
    select_mode()
