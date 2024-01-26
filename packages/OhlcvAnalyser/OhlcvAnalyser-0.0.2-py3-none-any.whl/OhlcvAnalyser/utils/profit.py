def calc_profit(series):
    profit = (series["close"].iloc[-1] - series["close"].iloc[0]) / series[
        "close"
    ].iloc[0]
    return profit