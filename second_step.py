import Up_or_Down
import Buy_or_Sell
import time
import logging
import pyupbit
import datetime

f = open("key.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

# 도서관에서 접속할 시 그 때마다 API관리 IP 주소 변경하는 것을 잊지 말 것
upbit = pyupbit.Upbit(access, secret)

def eight_to_twelve():
    flag = False
    ticker_bought = None
    ticker_bought_price = 0
    recent_bought_tickers = []
    while True:
        balance = upbit.get_balance("KRW")
        if flag:
            logging.info("코인 사서 관망 중")
            print("코인 사서 관망 중")
            per = Up_or_Down.how_many_differences(ticker_bought, ticker_bought_price)
            relative_per = Up_or_Down.rel_per(ticker_bought)
            if per <= -10.0:
                upbit.sell_market_order(ticker_bought, upbit.get_balance(ticker_bought))
                print(ticker_bought + " 팔았음 이윤은 " + str(per) + "%")
                logging.info("%s 팔았습니다.", ticker_bought)
                logging.info("이윤은 %s %입니다", str(per))
                flag = False
            elif relative_per < -5.0 and per < 0.0:
                upbit.sell_market_order(ticker_bought, upbit.get_balance(ticker_bought))
                print(ticker_bought + " 팔았음 이윤은 " + str(per) + "%")
                logging.info("%s 팔았습니다.", ticker_bought)
                logging.info("이윤은 %s %입니다", str(per))
                flag = False
            elif per >= 20.0:
                # info = Buy_or_Sell.sell_ticker(ticker_bought)
                upbit.sell_market_order((ticker_bought), upbit.get_balance(ticker_bought))
                print(ticker_bought + " 팔았음 이윤은 " + str(per) + "%")
                logging.info("%s 팔았습니다.", ticker_bought)
                logging.info("이윤은 %s %입니다", str(per))
                flag = False
        else:
            logging.info("살 코인 찾는 중")
            now = datetime.datetime.now()
            print("살 코인 찾는 중 " + str(now))

            up_list = Up_or_Down.going_up_list()
            ticker = list(up_list.keys())[0]
            if ticker in recent_bought_tickers:
                time.sleep(1)
                continue
            if ticker is not None:
                time.sleep(1)
                # info = Buy_or_Sell.buy_ticker(ticker)
                print("코인 " + ticker + " 샀음")
                balance = balance/10005*9999

                info = upbit.buy_market_order(ticker, balance)
                print(info)
                logging.info("%s 샀습니다.", ticker)
                recent_bought_tickers.append(ticker)
                ticker_bought = ticker
                ticker_bought_price = pyupbit.get_current_price(ticker_bought)
                flag = True
            else:
                logging.info("살 코인이 없음")
                print("살 코인이 없음")
        time.sleep(1)

def twelve_to_eight():
    flag = False
    ticker_bought = None
    ticker_bought_price = 0
    recent_bought_tickers = []
    while True:
        balance = upbit.get_balance("KRW")
        if flag:
            logging.info("코인 사서 관망 중")
            print("코인 사서 관망 중")
            per = Up_or_Down.how_many_differences(ticker_bought, ticker_bought_price)
            relative_per = Up_or_Down.rel_per(ticker_bought)
            if per <= -5.0:
                # info = Buy_or_Sell.sell_ticker(ticker_bought)
                upbit.sell_market_order(ticker_bought, upbit.get_balance(ticker_bought))
                print(ticker_bought + " 팔았음 이윤은 " + str(per) + "%")
                logging.info("%s 팔았습니다.", ticker_bought)
                logging.info("이윤은 %s %입니다", str(per))
                flag = False
            elif relative_per < -5.0 and per < 0.0:
                upbit.sell_market_order(ticker_bought, upbit.get_balance(ticker_bought))
                print(ticker_bought + " 팔았음 이윤은 " + str(per) + "%")
                logging.info("%s 팔았습니다.", ticker_bought)
                logging.info("이윤은 %s %입니다", str(per))
                flag = False
            elif per >= 3.0:
                # info = Buy_or_Sell.sell_ticker(ticker_bought)
                upbit.sell_market_order((ticker_bought), upbit.get_balance(ticker_bought))
                print(ticker_bought + " 팔았음 이윤은 " + str(per) + "%")
                logging.info("%s 팔았습니다.", ticker_bought)
                logging.info("이윤은 %s %입니다", str(per))
                flag = False
        else:
            logging.info("살 코인 찾는 중")
            now = datetime.datetime.now()
            print("살 코인 찾는 중 " + str(now))

            up_list = Up_or_Down.going_up_list()
            ticker = list(up_list.keys())[0]
            if ticker in recent_bought_tickers:
                time.sleep(1)
                continue
            if ticker is not None:
                time.sleep(1)
                # info = Buy_or_Sell.buy_ticker(ticker)
                print("코인 " + ticker + " 샀음")
                balance = balance/10005*9999

                info = upbit.buy_market_order(ticker, balance)
                print(info)
                logging.info("%s 샀습니다.", ticker)
                recent_bought_tickers.append(ticker)
                ticker_bought = ticker
                ticker_bought_price = pyupbit.get_current_price(ticker_bought)
                flag = True
            else:
                logging.info("살 코인이 없음")
                print("살 코인이 없음")
        time.sleep(1)
# upbit.buy_market_order("KRW-ETH", 10000)
main()
