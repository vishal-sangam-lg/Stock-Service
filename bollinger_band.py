# Bollinger bands
# rolling average of required length is pivot
# upper_band = pivot + standard deviation
# lower_band = pivot - standard deviation

import pandas as pd

LENGTH = 20
MULT = 2


def get_bb(close_prices):
    """Takes close_prices as input and returns an object of pivot upper_band and lower_band"""
    # Convert prices str to float
    for i in range(0, len(close_prices)):
        close_prices[i] = float(close_prices[i])
    df = pd.DataFrame(close_prices)
    df['pivot'] = df[0].rolling(window=LENGTH).mean()
    df['standard_deviation'] = MULT * df[0].rolling(window=LENGTH).std()
    df['upper_band'] = df['pivot'] + df['standard_deviation']
    df['lower_band'] = df['pivot'] - df['standard_deviation']
    ans = {
        'pivot': df['pivot'].tolist(),
        'upper_band': df['upper_band'].tolist(),
        'lower_band': df['lower_band'].tolist()
    }
    return ans
