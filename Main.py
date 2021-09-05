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

def main():
    sell_time = False
    buy_time = None
    flag = True
    ticker_bought = None
    ticker_bought_price = 0
    recent_bought_tickers = []
    deal_count = 0
    while True:
        now = datetime.datetime.now()
        time.sleep(0.05)
        if 8 <= now.hour <= 23:
            if flag is True:
                now1 = datetime.datetime.now()
                print("살 코인 찾는 중 " + str(now1))
                up_list = Up_or_Down.going_up_list(rate=5)
                ticker = list(up_list.keys())[0]
                per = up_list[ticker]
                if ticker in recent_bought_tickers:
                    time.sleep(0.05)
                    continue
                if ticker is not None:
                    print("코인 " + ticker + " 샀음 " + str(per))
                    balance = upbit.get_balance("KRW")
                    balance = balance/10005*9999
                    info = upbit.buy_market_order(ticker, balance)
                    # print(info)
                    buy_time = datetime.datetime.now()
                    logging.info("%s 때 들어갔습니다.", per)
                    logging.info("%s 샀습니다.", ticker)
                    recent_bought_tickers.append(ticker)
                    ticker_bought = ticker
                    ticker_bought_price = pyupbit.get_current_price(ticker_bought)
                    flag = False
                else:
                    print("살 코인이 없음")

            elif flag is False:
                print("코인 사서 관망 중")
                per = Up_or_Down.how_many_differences(ticker_bought, ticker_bought_price)
                sell_time = datetime.datetime.now()
                # if sell_time.hour*60 + sell_time.minute - buy_time.hour * 60 - buy_time.minute >= 120 and per >= 0:
                #     upbit.sell_market_order(ticker_bought, upbit.get_balance(ticker_bought))
                #     print(ticker_bought + " 팔았음 이윤은 " + str(per) + "%")
                #     logging.info("%s 팔았습니다.", ticker_bought)
                #     logging.info("이윤은 %s 입니다", str(per))
                #     flag = True
                    # deal_count += 1
                if per >= 15.0:
                    upbit.sell_market_order(ticker_bought, upbit.get_balance(ticker_bought))
                    print(ticker_bought + " 팔았음 이윤은 " + str(per) + "%")
                    logging.info("%s 팔았습니다.", ticker_bought)
                    logging.info("이윤은 %s 입니다", str(per))
                    flag = True
                    # deal_count += 1

                if per <= -5.0:
                    upbit.sell_market_order(ticker_bought, upbit.get_balance(ticker_bought))
                    print(ticker_bought + " 팔았음 이윤은 " + str(per) + "%")
                    logging.info("%s 팔았습니다.", ticker_bought)
                    logging.info("이윤은 %s 입니다", str(per))
                    flag = True
                    # deal_count += 1

main()
