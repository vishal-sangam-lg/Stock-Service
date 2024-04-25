# Volume weighted average price (VWAP)
# Formula:
# cumulative_vol_price = cumulative sum of volume * typical price
# where typical price = (high + low + close) / 3
# cumulative_vol = cumulative sum of volume
# VWAP = cumulative_vol_price / cumulative_vol

import pandas as pd


def get_vwap(high_prices, low_prices, close_prices, volumes):
    """Takes lists of high low close volume as input, returns vwap of given data"""
    # Convert str to float
    for i in range(0, len(volumes)):
        high_prices[i] = float(high_prices[i])
        low_prices[i] = float(low_prices[i])
        close_prices[i] = float(close_prices[i])
        volumes[i] = float(volumes[i])

    data = {'high': high_prices, 'low': low_prices, 'close': close_prices, 'volume': volumes}
    df = pd.DataFrame(data)
    df['cumulative_vol'] = df['volume'].cumsum()
    df['cumulative_vol_price'] = (df['volume'] * (df['high'] + df['low'] + df['close']) / 3).cumsum()
    df['VWAP'] = df['cumulative_vol_price'] / df['cumulative_vol']
    # print(df)
    vwap = df['VWAP'].tolist()
    return vwap
