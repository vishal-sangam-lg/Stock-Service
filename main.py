import requests
from rsi import get_rsi
from ema import get_ema
from macd import get_macd
from vwap import get_vwap
from bollinger_band import get_bb
from support_resistance import get_support_resistance
from datetime import datetime
import json
import os

# # ALPHAVANTAGE_API_KEY = "B3FWNEAFOCJIT13J"
# # ALPHAVANTAGE_API_KEY = "LQBNTY1ZJK62O7EC"
# # ALPHAVANTAGE_API_KEY = "XIVI0MADROMALCJN"
# # ALPHAVANTAGE_API_KEY = "F69Q9S510OU2FFIW"
ALPHAVANTAGE_API_KEY = "H1BOIQG8NDJNQ33U"

def get_stock_data_if_not_present_locally():
    today_date = datetime.today().date()
    print(today_date)
    
    # Define the folder name
    folder_name = "StockData"

    # Check if the folder exists, if not, create it
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

    # Define the file path with today's date and folder name
    file_path = os.path.join(folder_name, f"{today_date}.json")

    if os.path.exists(file_path):
        print(f"File '{file_path}' already exists.")
    else:
        print("Fetching data...")
        url = f'https://www.alphavantage.co/query?function=TIME_SERIES_WEEKLY&symbol=RELIANCE.BSE&apikey=${ALPHAVANTAGE_API_KEY}'
        r = requests.get(url)
        data = r.json()

        # Write data to JSON file
        with open(file_path, "w") as json_file:
            json.dump(data, json_file)

def get_stock_data():
    get_stock_data_if_not_present_locally()

    today_date = datetime.today().date()
    folder_name = "StockData"
    file_path = os.path.join(folder_name, f"{today_date}.json")

    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

        # Daily data
        # daily_data = data['Time Series (Daily)']
        # Weekly data
        weekly_data = data['Weekly Time Series']
        open_prices = []
        close_prices = []
        low_prices = []
        high_prices = []
        volumes = []

        for day in weekly_data:
            open_prices.append(weekly_data[day]['1. open'])
            close_prices.append(weekly_data[day]['4. close'])
            low_prices.append(weekly_data[day]['3. low'])
            high_prices.append(weekly_data[day]['2. high'])
            volumes.append(weekly_data[day]['5. volume'])

        # Filtering latest data
        recent_open_prices = open_prices[:100]
        recent_close_prices = close_prices[:100]
        recent_high_prices = high_prices[:100]
        recent_low_prices = low_prices[:100]
        recent_open_prices.reverse()
        recent_close_prices.reverse()
        recent_high_prices.reverse()
        recent_low_prices.reverse()

        stock_data = {
            "open": recent_close_prices,
            "close": recent_close_prices,
            "high": recent_high_prices,
            "low": recent_low_prices,
        }

        return stock_data
    else:
        return "500: Internal Error, Could'nt fetch stock data. File doesn't exist"


def get_macd_data():
    get_stock_data_if_not_present_locally()

    today_date = datetime.today().date()
    folder_name = "StockData"
    file_path = os.path.join(folder_name, f"{today_date}.json")

    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

        weekly_data = data['Weekly Time Series']
        close_prices = []

        for day in weekly_data:
            close_prices.append(weekly_data[day]['4. close'])

        recent_close_prices = close_prices[:100]

        macd = get_macd(recent_close_prices)

        stock_data = {
            "macd": macd,
        }

        return stock_data
    else:
        return "500: Internal Error, Could'nt fetch stock data. File doesn't exist"
        


def get_bb_data():
    get_stock_data_if_not_present_locally()

    today_date = datetime.today().date()
    folder_name = "StockData"
    file_path = os.path.join(folder_name, f"{today_date}.json")

    # Check if the file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as json_file:
            data = json.load(json_file)

        weekly_data = data['Weekly Time Series']
        close_prices = []

        for day in weekly_data:
            close_prices.append(weekly_data[day]['4. close'])

        recent_close_prices = close_prices[:100]
        recent_close_prices.reverse()

        bb = get_bb(recent_close_prices)

        stock_data = {
            "lower_band": bb["lower_band"],
            "upper_band": bb["upper_band"],
            "close": recent_close_prices
        }

        return stock_data
    else:
        return "500: Internal Error, Could'nt fetch stock data. File doesn't exist"
    
