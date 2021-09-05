import pybithumb
def bull_market():
    btc = pybithumb.get_ohlcv("BTC")

    close = btc['close']

    close_mean = close.rolling(5).mean()
    price = pybithumb.get_current_price("BTC")
    last_close_mean = close_mean[-2]

    if price > last_close_mean:
        return True
    else:
        return False

print(bull_market())