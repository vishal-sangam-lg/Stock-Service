# Exponential moving average (EMA)
# Weighted moving average in given time period
# Note: More weightage is given to the latest price

import pandas as pd


def get_ema(close_prices, period):
    """Takes close_prices and time period as input and returns
    exponential moving average of price in given time period"""
    df = pd.DataFrame(close_prices)
    ema = df.ewm(span=period, adjust=False).mean()
    ans = ema[0].tolist()
    return ans
