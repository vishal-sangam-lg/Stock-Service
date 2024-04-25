# Relative Strength Index (RSI)
# Formula: 100 - (100 / (1 + RS)) where RS = avg gain / avg loss

WINDOW_LENGTH = 14


def get_rsi(close_prices):
    """Takes close_prices of a stock as input and return 14 days/weeks rsi"""
    gains = []
    losses = []
    rsi = []
    for i in range(0, len(close_prices)):
        difference = round(float(close_prices[i]) - float(close_prices[i - 1]), 2)
        if difference > 0:
            gains.append(difference)
            losses.append(0)
        elif difference < 0:
            gains.append(0)
            losses.append(abs(difference))
        else:
            gains.append(0)
            losses.append(0)
        if len(gains) > WINDOW_LENGTH and len(losses) > WINDOW_LENGTH:
            gains.pop(0)
            losses.pop(0)
            avg_gain = sum(gains) / len(gains)
            avg_loss = sum(losses) / len(losses)
            relative_strength = avg_gain / avg_loss
            current_rsi = 100.0 - (100.0 / (1 + relative_strength))
            rsi.append(current_rsi)
    # Adding 0s for first 14
    for i in range(0, 14):
        rsi.insert(0, 0)
    return rsi
