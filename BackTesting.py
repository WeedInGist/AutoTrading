import pyupbit
import time
import datetime


f = open("key.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
# upbit = pyupbit.Upbit(access, secret)
# 업비트 api 사용을 위한 코드


# fiat 값에 따라서 특정 마켓의 코인 리스트를 반환함
def tickers_list(fiat="KRW"):
    tickers = pyupbit.get_tickers(fiat=fiat)
    while tickers is None:
        tickers = pyupbit.get_tickers(fiat=fiat)
        time.sleep(0.05)
        print(datetime.datetime.now())
        print("연결 실패로 다시 코인 리스트 뽑는 중입니다.")
    return tickers


# 구매한 코인의 가격이 지금 몇 퍼만큼 변동이 있는지 계산해줌
def how_diff_percentage(ticker_bought, ticker_bought_price):
    current_price = pyupbit.get_current_price(ticker_bought)
    while current_price is None:
        current_price = pyupbit.get_current_price(ticker_bought)
        time.sleep(0.05)
        print(datetime.datetime.now())
        print("연결 실패로 구매한 코인의 현재 가격을 다시 불러오고 있습니다..")
    per = 100*current_price / ticker_bought_price - 100
    return per


# count 날만큼 그 날 가장 많이 올랐던 코인을 알려줌: 최고점을 비교함
def find_out_highest_coin(fiat, count):
    ticker_list = tickers_list(fiat)

    high_tickers = []
    high_pers = []
    high_days = []
    print(datetime.datetime.now())
    for i in range(count):
        high_per = 0
        high_ticker = None
        high_day = None
        for ticker in ticker_list:
            time.sleep(0.15)
            judgement = pyupbit.get_ohlcv(ticker=ticker, interval="day", count=count)
            # print(ticker)
            if high_per <= (judgement.iloc[i]['high'] / judgement.iloc[i]['open']) * 100 - 100:
                high_per = (judgement.iloc[i]['high'] / judgement.iloc[i]['open']) * 100 - 100
                high_ticker = ticker
                high_day = judgement.index[i]
            # print((judgement.iloc[i]['high']/judgement.iloc[i]['open'])*100 - 100)
            # print(judgement.index[i])
        high_tickers.append(high_ticker)
        high_pers.append(high_per)
        high_days.append(high_day)
    print(datetime.datetime.now())
    for i in range(count):
        print(high_tickers[i], high_pers[i], high_days[i])


