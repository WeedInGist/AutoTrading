import pyupbit
import pandas
import time
import logging
import datetime

pandas.set_option('display.max_columns', 10)
pandas.set_option('display.max_row', 100)


def tickers_list(fiat="KRW"):
    tickers = pyupbit.get_tickers(fiat=fiat)
    while tickers is None:
        tickers = pyupbit.get_tickers(fiat=fiat)
        print("와이파이가 끊어져서 코인 리스트 뽑는 과정 재시도중")
    return tickers


def tickers_list_btc(fiat="BTC"):
    tickers = pyupbit.get_tickers(fiat=fiat)
    while tickers is None:
        tickers = pyupbit.get_tickers(fiat=fiat)
        print("와이파이가 끊어져서 코인 리스트 뽑는 과정 재시도중")
    return tickers


def how_many_differences(ticker_bought, ticker_bought_price):
    current_price = pyupbit.get_current_price(ticker_bought)
    while current_price is None:
        current_price = pyupbit.get_current_price(ticker_bought)
        print("코인 현재가 가져오는 중에 연결 끊어져서 재시도중1")
    per = 100*current_price/ticker_bought_price-100
    return per


def rel_per(ticker):
    data = pyupbit.get_ohlcv(ticker, interval="minute10")
    while data is None:
        data = pyupbit.get_ohlcv(ticker, interval="minute10")
    open_price = data.iloc[-1]['open']
    close_price = data.iloc[-1]['close']
    relative_per = 100*close_price/open_price - 100
    return relative_per


def is_going_up_or_down(ticker="KRW-ETH", rate=5.0):
    data = pyupbit.get_ohlcv(ticker, interval="minute10")
    while data is None:
        data = pyupbit.get_ohlcv(ticker, interval="minute10")
    open_price = data.iloc[-1]['open']
    close_price = data.iloc[-1]['close']
    per = 100 * close_price/open_price - 100
    if per >= rate:
        return True, per
    else:
        return False, per

# 10분간 5퍼 이상 10% 이하 상승한 코인 중에 가장 높은 코인을 리턴함


def going_up_list(rate=5):
    # now1 = datetime.datetime.now()
    print(datetime.datetime.now())
    up_list = {}
    highest_per = 0
    highest_ticker = None
    tickers = tickers_list()
    for ticker in tickers:
        time.sleep(0.15)
        up_or_down, per = is_going_up_or_down(ticker, rate)
        if up_or_down:
            if per > highest_per:
                highest_per = per
                highest_ticker = ticker
    up_list[highest_ticker] = highest_per
    # now2= datetime.datetime.now()
    print(datetime.datetime.now())
    return up_list

def going_up_list_btc(rate=5):
    # now1 = datetime.datetime.now()
    print(datetime.datetime.now())
    up_list = {}
    highest_per = 0
    highest_ticker = None
    tickers = tickers_list_btc()
    for ticker in tickers:
        time.sleep(0.05)
        up_or_down, per = is_going_up_or_down(ticker, rate)
        if up_or_down:
            if per > highest_per:
                highest_per = per
                highest_ticker = ticker
    up_list[highest_ticker] = highest_per
    # now2= datetime.datetime.now()
    print(datetime.datetime.now())
    return up_list


# print(going_up_list())
# is_going_up_or_down()
