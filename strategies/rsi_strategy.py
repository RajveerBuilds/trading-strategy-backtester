import pandas as pd

def generate_signals(data):

    delta = data["Close"].diff()

    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)

    avg_gain = gain.rolling(14).mean()
    avg_loss = loss.rolling(14).mean()

    rs = avg_gain / avg_loss

    rsi = 100 - (100 / (1 + rs))

    signals = pd.DataFrame(index=data.index)

    signals["positions"] = 0

    signals.loc[rsi < 30, "positions"] = 1
    signals.loc[rsi > 70, "positions"] = -1

    return signals