# Support Resistance with respect to central pivot

# Formula and implications
# R3 = R1 + (high - low)            ->  Extremely Bullish
# R2 = pivot + (high - low)         ->  Bullish
# R1 = (2 * pivot) - low            ->  Mildly Bullish
# pivot = (high + low + close) / 3  ->  Mean price level
# S1 = (2 * pivot) - high           ->  Mildly Bearish
# S2 = pivot - (high - low)         ->  Bearish
# S3 = S1 - (high - low)            -> Extremely Bearish

import pandas as pd


def get_support_resistance(high_prices, low_prices, close_prices):
    # Convert prices str to float
    for i in range(0, len(close_prices)):
        high_prices[i] = float(high_prices[i])
        low_prices[i] = float(low_prices[i])
        close_prices[i] = float(close_prices[i])

    df = pd.DataFrame({'high': high_prices, 'low': low_prices, 'close': close_prices})
    df['pivot'] = (df['high'] + df['low'] + df['close']) / 3
    df['R1'] = (2 * df['pivot']) - df['low']
    df['R2'] = df['pivot'] + (df['high'] - df['low'])
    df['R3'] = df['R1'] + (df['high']) - df['low']
    df['S1'] = (2 * df['pivot'] - df['high'])
    df['S2'] = df['pivot'] - (df['high'] - df['low'])
    df['S3'] = df['S1'] - (df['high'] - df['low'])
    ans = {
        'pivot': df['pivot'].tolist(),
        'R1': df['R1'].tolist(),
        'R2': df['R2'].tolist(),
        'R3': df['R3'].tolist(),
        'S1': df['S1'].tolist(),
        'S2': df['S2'].tolist(),
        'S3': df['S3'].tolist()
    }
    return ans
