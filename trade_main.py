#!/usr/bin/python3
# coding: utf8

import pandas as pd
import random

from utils.stock_functions import MAFilter

initial_data = pd.read_csv("./data/Training_data.csv",
                           names=['volume1', 'price1', 'volume2', 'price2', 'volume3', 'price3', 'volume4', 'price4',
                                  'volume5', 'price5'
                               , 'volume6', 'price6', 'volume7', 'price7', 'volume8', 'price8', 'volume9', 'price9',
                                  'volume10', 'price10'])
# print(initial_data)


stock_trading_volume = pd.DataFrame(initial_data,
                                    columns=['volume1', 'volume2', 'volume3', 'volume4', 'volume5', 'volume6',
                                             'volume7', 'volume8', 'volume9', 'volume10'])
# print(stock_trading_volume)
stock_price = pd.DataFrame(initial_data,
                           columns=['price1', 'price2', 'price3', 'price4', 'price5', 'price6', 'price7', 'price8',
                                    'price9', 'price10'])
# print(stock_price)


day1_stock_price = stock_price.iloc[0]
# print(day1_stock_price)
# print(day1_stock_price[1])  # 318.76
# print(stock_price.iloc[0][0])


stock_num = 2

sum_hold_stock = MAFilter.initial_buy_stock(stock_num,
                                            stock_price)  # [['price7', 27.065064414853307, 5000.0], ['price5', 12.291052114060964, 5000.0]]
print('sum_hold_stock: ')
print(sum_hold_stock)


days = [2, 5]

i = days[0]
while i <= days[1]:
    # print(i)

    # 获取上一日最大的回报率
    stock_return_rate, stock_return_rate_sorted = MAFilter.stock_return_rate(i, stock_price)
    print(stock_return_rate_sorted)
    max_rate = stock_return_rate_sorted[0]
    print("max_rate: ")
    print(max_rate)
    min_rate = stock_return_rate_sorted[9]
    print("min_rate: ")
    print(min_rate)
    print('stock_return_rate:')
    print(stock_return_rate)

    # ff
    stock_min_rate_name = min_rate
    # sum_hold_stock, stock_min_rate_name, stock_min_volume = MAFilter.return_min_rate_stock(sum_hold_stock, stock_return_rate)
    print('stock_min_rate_name:')
    print(stock_min_rate_name)
    # 如果当前最小回报不是上一日的第一，卖出换钱
    # sell_money = 0
    if stock_min_rate_name != max_rate:
        sell_money = MAFilter.sell_stock(sum_hold_stock, stock_price, i, stock_min_rate_name, stock_return_rate_sorted)
        selt_money = MAFilter.trading_commissions(sell_money, fee=0.99)
        print('selt_money:')
        print(selt_money)
        # """

        # 购买最大率股票
        buy_stock_list = MAFilter.buy_stock(max_rate, stock_price, i, selt_money)

        sum_hold_stock.append(buy_stock_list)

    print('sum_hold_stock: ' + '666666')
    print(sum_hold_stock)
    # """


    print('----------------------------------')
    i += 1



