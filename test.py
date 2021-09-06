import Up_or_Down
import Buy_or_Sell
import time
import logging
import pyupbit
import datetime
import threading

f = open("key.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
# 도서관에서 접속할 시 그 때마다 API관리 IP 주소 변경하는 것을 잊지 말 것
upbit = pyupbit.Upbit(access, secret)
# 9시에 10분동안 몇 퍼나 올랐는지 보여줌
def nine_o_clock():
    tickers_list = Up_or_Down.tickers_list("KRW")
    for ticker in tickers_list:
        time.sleep(0.05)
        data = pyupbit.get_ohlcv(ticker=ticker,count=1,interval="minute10",to="2021-09-06 09:10:00")
        per = data.iloc[0]['high']/data.iloc[0]['open']*100-100
        print(ticker, per)
nine_o_clock()


# 10분동안 15퍼 이상 오른 코인 중 그날 다시 원점으로 돌아온 코인이 있는가
def find_out_best_coin(fiat="BTC", count=1, rate=10):
    tickers_list = Up_or_Down.tickers_list(fiat)
    ticker_price={}
    for ticker in tickers_list:
        data = pyupbit.get_ohlcv(ticker=ticker, count=count, interval="minute10", to="2021-09-06 09:10:00")
        data1 = pyupbit.get_ohlcv(ticker=ticker, count=1, interval="day")
        (data.iloc[0]['open'])
        for i in range(count):
            if rate <= (data.iloc[i]['high'] / data.iloc[i]['open']) * 100 - 100:
                pass # highest_price =


# def Riding_On_Fastest_Horse():
# 날마다 가장 많이 오른 코인을 알려줌
def find_out_highest_coin(fiat, count):
    tickers_list = Up_or_Down.tickers_list(fiat)

    high_tickers = []
    high_pers = []
    high_days = []
    print(datetime.datetime.now())
    for i in range(count):
        high_per = 0
        high_ticker = None
        high_day = None
        for ticker in tickers_list:
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

# find_out_highest_coin("KRW",10)
# find_out_highest_coin("BTC",1)
# find_out_highest_coin("KRW",1)
# t1 = threading.Thread(target=Up_or_Down.going_up_list, args=(5,))
# t1.start()
# t2 = threading.Thread(target=Up_or_Down.going_up_list, args=(5,))
# t2.start()

#
def find_out_highest_coin_BTC(fiat, count):
    tickers_list = Up_or_Down.tickers_list(fiat)

    high_tickers = []
    high_pers = []
    high_days = []
    print(datetime.datetime.now())
    for ticker in tickers_list:
        time.sleep(0.05)
        judgement = pyupbit.get_ohlcv(ticker=ticker, interval="minute10", count=count)
        print(judgement.index[0])
        for i in range(count-1):
            if 10 <= (judgement.iloc[i]['high'] / judgement.iloc[i]['open']) * 100 - 100:
                # if judgement.iloc[i]['open']*1.>judgement.iloc[i+1]['close']:
                high_tickers.append({ticker: judgement.index[i]})
                high_day = judgement.index[i]
        # print((judgement.iloc[i]['high']/judgement.iloc[i]['open'])*100 - 100)
        # print(judgement.index[i])
    print(high_tickers)
# find_out_highest_coin_BTC("KRW", 93)
# judgement = pyupbit.get_ohlcv(ticker="BTC-ARK", interval="minute10", count=90, to='2021-08-10 09:00:00')
# print(judgement)

def get_pattern(fiat, count):
    time.sleep(0.05)
    tickers_list = Up_or_Down.tickers_list(fiat=fiat)
    for ticker in tickers_list:
        percent = []
        data = pyupbit.get_ohlcv(ticker=ticker, interval="minute10", count=count)
        for i in range(count):
            percent.append(100 * data.iloc[i]['close'] / data.iloc[i]['open'] - 100)
        # print(data.insert(0 , 'raise_per', percent))
        print(ticker)
        print(percent)


# get_pattern("BTC",10)
def te():
    time.sleep(0.05)
    tickers = pyupbit.get_tickers("BTC")
    for ticker in tickers:
        data = pyupbit.get_ohlcv(ticker)
        if data is None:
            print(ticker)
# te()
# data = pyupbit.get_ohlcv("BTC-LINK")
# print(data)
# print.data['raise_per']
# find_out_highest_coin_BTC("BTC", 100)
# find_out_highest_coin("BTC", 15)

# def find_out_highest_time(ticker, interval, date):
#
# data = pyupbit.get_ohlcv(ticker="BTC-BFC", interval="minute1", count=780)
# high_price = 0
# high_time = None
# for i in range(780):
#     if high_price <= data.iloc[i]['high']:
#         high_price = data.iloc[i]['high']
#         high_time = data.index[i]
# print(high_time)
#
#     sell_1 = False
#     sell_2 = False
#     while True:
#         balance_val = upbit.get_balance_t("BTC-VAL")*9970/10000
#         balance_prom = upbit.get_balance("BTC-PROM")*9970/10000
#         time.sleep(1)
#         price_val = pyupbit.get_current_price("BTC-VAL")
#         price_prom = pyupbit.get_current_price("BTC-PROM")
#         per_val = Up_or_Down.how_many_differences("BTC-VAL", 0.00013300)
#         per_prom = Up_or_Down.how_many_differences("BTC-PROM", 0.00052854)
#         if per_val >= 10:
#             upbit.sell_market_order("BTC-VAL", balance_val)
#             print(per_val)
#             logging.info("밸러디티 팔았습니다.")
#             print("밸러디티 팔았습니다.")
#             sell_1 = True
#         if per_prom >= 10:
#             upbit.sell_market_order("BTC-PROM", balance_prom)
#             logging.info("밸러디티 팔았습니다.")
#             print(per_prom)
#             print("밸러디티 팔았습니다.")
#             sell_2 = True
#         if sell_2 is True and sell_1 is True:
#             return