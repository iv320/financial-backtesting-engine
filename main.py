import yfinance as yf
import pandas as pd
import numpy as np

data = yf.download("AAPL", period="1y")

data["Returns"] = data["Close"].pct_change()
data["Strategy"] = np.where(data["Returns"] > 0, 1, -1)

data["Strategy_Returns"] = data["Returns"] * data["Strategy"]

pnl = data["Strategy_Returns"].sum()
sharpe = (data["Strategy_Returns"].mean() / data["Strategy_Returns"].std()) * np.sqrt(252)

print("P&L:", pnl)
print("Sharpe Ratio:", sharpe)
