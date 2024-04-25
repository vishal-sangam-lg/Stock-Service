from ema import get_ema
import pandas as pd


def get_macd(close_prices):
    ema12 = get_ema(close_prices, 12)
    ema26 = get_ema(close_prices, 26)
    df = pd.DataFrame({'12EMA': ema12, '26EMA': ema26})
    df['macd'] = df['12EMA'] - df['26EMA']
    macd = df['macd'].tolist()
    signal = get_ema(macd, 9)
    df['signal'] = signal
    ans = {
        'macd': df['macd'].tolist(),
        'signal': df['signal'].tolist()
    }
    return ans
