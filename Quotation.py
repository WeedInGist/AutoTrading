import pyupbit
import time
f = open("key.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access, secret)


def tickers_list(fiat="KRW"):
    tickers = pyupbit.get_tickers(fiat=fiat)
    while tickers is None:
        tickers = pyupbit.get_tickers(fiat=fiat)
        print("와이파이가 끊어져서 코인 리스트 뽑는 과정 재시도중")
    return tickers


# 인수로 넘어가는 값에 따라서 시장의 코인들을 전부 리스트로 반환


def how_many_differences(ticker_bought, ticker_bought_price):
    current_price = pyupbit.get_current_price(ticker_bought)
    while current_price is None:
        current_price = pyupbit.get_current_price(ticker_bought)
        print("코인 현재가 가져오는 중에 연결 끊어져서 재시도중1")
    per = 100 * current_price / ticker_bought_price - 100
    return per


# 내가 산 코인과 그 가격을 넣으면 현재 수익률을 알려줌


def more_than_zero_list(rate=0):
    potential_list = []
    tickers = tickers_list()
    for ticker in tickers:
        time.sleep(0.1)
        data = pyupbit.get_ohlcv(ticker, interval="minute10")
        while data is None:
            print("?")
            data = pyupbit.get_ohlcv(ticker, interval="minute10")
        open_price = data.iloc[-1]['open']
        current_price = data.iloc[-1]['close']
        per = 100 * current_price / open_price - 100
        print(per)
        if per > rate:
            print("doing")
            potential_list.append((per, ticker))
    return sorted(potential_list)
# print(tickers_list())


# rate 비율보다 높이 오른 코인들을 리스트로 반환
def get_my_coins_and_volume():
    information_list = upbit.get_balances()
    temp_list = []
    coins_list = []
    for information in information_list:
        if information['unit_currency'] == 'KRW':
            temp_list.append(information['currency'])
    for i in temp_list:
        coins_list.append("KRW-"+i)
    print(coins_list)
    se = coins_list[1:6]
    print(pyupbit.get_current_price(["KRW-BTC","KRW-GLM"]))
    print(pyupbit.get_current_price(se))
"""
    for i in range(1, len(information_list)):
        percent = how_many_differences(information_list[i]['unit_currency']+"-"+information_list[i]['currency'], float(information_list[i]['avg_buy_price']))
        coins_list.append((information_list[i]['currency'],
                           information_list[i]['balance'], information_list[i]['avg_buy_price']))
        time.sleep(0.15)
        print("KRW-"+information_list[i]['currency'])
#     return coins_list
"""

# print(get_my_coins_and_volume())
# print(how_many_differences('GLM', 654))
# print(pyupbit.get_current_price("KRW-POWR"))