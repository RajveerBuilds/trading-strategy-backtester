import pandas as pd

def backtest(data, signals, initial_capital=10000, transaction_cost=0.001):

    portfolio = pd.DataFrame(index=data.index)

    price = data["Close"]

    cash = initial_capital
    shares = 0

    shares_history = []
    cash_history = []

    for i in range(len(data)):

        signal = signals["positions"].iloc[i]
        current_price = price.iloc[i]

        # BUY
        if signal == 1 and shares == 0:

            shares = int(cash / current_price)

            trade_value = shares * current_price
            fee = trade_value * transaction_cost

            cash -= (trade_value + fee)

        # SELL
        elif signal == -1 and shares > 0:

            trade_value = shares * current_price
            fee = trade_value * transaction_cost

            cash += (trade_value - fee)

            shares = 0

        shares_history.append(shares)
        cash_history.append(cash)

    portfolio["shares"] = shares_history
    portfolio["cash"] = cash_history
    portfolio["price"] = price

    portfolio["holdings"] = portfolio["shares"] * portfolio["price"]

    portfolio["total"] = portfolio["cash"] + portfolio["holdings"]

    portfolio["returns"] = portfolio["total"].pct_change()

    return portfolio