import yfinance as yf
import pandas as pd

def load_data(symbol, start, end):

    data = yf.download(symbol, start=start, end=end, auto_adjust=True)

    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    return data[["Open","High","Low","Close","Volume"]]