import pyupbit
import logging

logging.basicConfig(filename="test.log", format='%(asctime)s:%(message)s', level=logging.INFO,
                    datefmt="%Y-%m-%d %H:%M:%S   ")
f = open("key.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

# 도서관에서 접속할 시 그 때마다 API관리 IP 주소 변경하는 것을 잊지 말 것
upbit = pyupbit.Upbit(access, secret)


def buy_ticker(ticker):
    balance = 0
    info = upbit.buy_market_order(ticker, balance)
    while info is None:
        logging.info("매수 주문 넣으려는데 연결이 끊어졌서 재시도중")
        info = upbit.buy_market_order(ticker, balance)
    logging.info("%s를 샀습니다.", ticker)
    return info


def sell_ticker(ticker):
    upbit.sell_market_order(ticker_bought, upbit.get_balance(ticker_bought))
    print(ticker_bought + " 팔았음 이윤은 " + str(per) + "%")
    logging.info("%s 팔았습니다.", ticker_bought)
    logging.info("이윤은 %s 입니다", per)
    flag = False
    deal_count += 1

#
# info = upbit.buy_limit_order("KRW-ETH", 100,100)
# balance = upbit.get_balance("KRW-ETH")
# info = upbit.buy_market_order("KRW-ETH", 6000)
# print(info['uuid'])
# uuid = '74ca09dd-eab3-4391-ba90-c7bca5638edb'
# print(upbit.get_individual_order(uuid))
# # upbit.cancel_order((inf))
# print(balance)
