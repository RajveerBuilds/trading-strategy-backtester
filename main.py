from utils.data_loader import load_data
from backtester.engine import backtest
from backtester.metrics import total_return, sharpe_ratio, max_drawdown

# choose strategy
from strategies.moving_average import generate_signals
# from strategies.rsi_strategy import generate_signals

import matplotlib.pyplot as plt

data = load_data("AAPL","2018-01-01","2023-01-01")

signals = generate_signals(data)

portfolio = backtest(data, signals)

tr = total_return(portfolio)
sr = sharpe_ratio(portfolio["returns"])
dd = max_drawdown(portfolio)

print("Strategy Return:", round(tr*100,2), "%")
print("Sharpe Ratio:", round(sr,2))
print("Max Drawdown:", round(dd*100,2), "%")

# market comparison
market = data["Close"] / data["Close"].iloc[0] * 10000

plt.figure(figsize=(10,5))
plt.plot(portfolio["total"], label="Strategy")
plt.plot(market, label="Buy & Hold")

plt.title("Strategy vs Market")
plt.xlabel("Date")
plt.ylabel("Portfolio Value")
plt.legend()

plt.show()