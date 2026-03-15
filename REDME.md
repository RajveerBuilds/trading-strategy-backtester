# Trading Strategy Backtester

A Python-based quantitative research tool for testing algorithmic trading strategies on historical market data.

This project simulates trading strategies, executes trades on historical data, and evaluates performance using key financial metrics. It also compares strategy performance against a simple buy-and-hold benchmark.

---

## Overview

Financial markets generate massive amounts of time-series data. Traders and quantitative researchers test strategies on past data to understand whether a trading idea has a statistical edge.

This project implements a modular backtesting framework that:

* Loads historical stock data
* Generates buy and sell signals using trading strategies
* Simulates portfolio trades over time
* Tracks portfolio value and returns
* Computes risk-adjusted performance metrics
* Compares strategy performance against the market

---

## Features

* Historical stock data download using Yahoo Finance
* Moving Average Crossover Strategy
* RSI Trading Strategy
* Realistic trade simulation with capital tracking
* Transaction cost modelling
* Performance evaluation metrics:

  * Total Return
  * Sharpe Ratio
  * Maximum Drawdown
* Visualization of portfolio performance
* Strategy vs Buy-and-Hold comparison

---

## Project Structure

```
trading-backtester
│
├── backtester
│   ├── engine.py        # trade simulation engine
│   └── metrics.py       # performance calculations
│
├── strategies
│   ├── moving_average.py
│   └── rsi_strategy.py
│
├── utils
│   └── data_loader.py   # downloads and prepares market data
│
└── main.py              # runs the backtest
```

---

## Strategies Implemented

### Moving Average Crossover

The strategy generates signals using two moving averages.

Buy when the short-term moving average crosses above the long-term moving average.

Sell when the short-term moving average crosses below the long-term moving average.

### RSI Strategy

Uses the Relative Strength Index (RSI) indicator.

Buy signal when RSI < 30 (oversold market).

Sell signal when RSI > 70 (overbought market).

---

## Performance Metrics

The system evaluates strategies using common quantitative finance metrics.

**Total Return**
Measures overall profitability of the strategy.

**Sharpe Ratio**
Measures risk-adjusted return by comparing average return to volatility.

**Maximum Drawdown**
Measures the largest peak-to-trough loss during the trading period.

---

## Example Output

Example results from running the moving average strategy on AAPL historical data:

Strategy Return: 127%
Sharpe Ratio: 0.84
Max Drawdown: -25%

The program also generates graphs showing:

* Portfolio value over time
* Strategy performance vs buy-and-hold market performance

---

## Technologies Used

Python
Pandas
NumPy
Matplotlib
yfinance

---

## How to Run

Install required libraries:

```
pip install pandas numpy matplotlib yfinance
```

Run the program:

```
python main.py
```

The program will download market data, run the strategy backtest, calculate performance metrics, and display graphs comparing the strategy to the market.

---

## Future Improvements

* Strategy parameter optimization
* Multi-asset portfolio backtesting
* Additional strategies (momentum, mean reversion)
* Interactive dashboards using Plotly or Streamlit
* Strategy grid search for parameter tuning

---

## Author

Rajveer Jaiswal