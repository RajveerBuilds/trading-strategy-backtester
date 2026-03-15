import numpy as np

def total_return(portfolio, initial_capital=10000):

    final_value = portfolio["total"].iloc[-1]

    return (final_value - initial_capital) / initial_capital


def sharpe_ratio(returns):

    returns = returns.dropna()

    if returns.std() == 0:
        return 0

    return np.sqrt(252) * returns.mean() / returns.std()


def max_drawdown(portfolio):

    cumulative_max = portfolio["total"].cummax()

    drawdown = (portfolio["total"] - cumulative_max) / cumulative_max

    return drawdown.min()