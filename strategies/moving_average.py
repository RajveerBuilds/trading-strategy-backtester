import pandas as pd

def generate_signals(data, short_window=20, long_window=50):

    signals = pd.DataFrame(index=data.index)

    signals["short_ma"] = data["Close"].rolling(short_window).mean()
    signals["long_ma"] = data["Close"].rolling(long_window).mean()

    signals["signal"] = 0

    signals.loc[signals["short_ma"] > signals["long_ma"], "signal"] = 1

    signals["positions"] = signals["signal"].diff()

    return signals