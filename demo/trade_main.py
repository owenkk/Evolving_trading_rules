#!/usr/bin/python3
# coding: utf8

import pandas as pd
import random
import matplotlib.pyplot as plt
import numpy as np

from utils.stock_functions import MAFilter

initial_data = pd.read_csv("../data/Training_data.csv",
                           names=['volume0', 'price0', 'volume1', 'price1', 'volume2', 'price2', 'volume3', 'price3',
                                  'volume4', 'price4'
                               , 'volume5', 'price5', 'volume6', 'price6', 'volume7', 'price7', 'volume8', 'price8',
                                  'volume9', 'price9'])
# print(initial_data)


stock_trading_volume = pd.DataFrame(initial_data,
                                    columns=['volume0', 'volume1', 'volume2', 'volume3', 'volume4', 'volume5',
                                             'volume6', 'volume7', 'volume8', 'volume8'])
# print(stock_trading_volume)
stock_price = pd.DataFrame(initial_data,
                           columns=['price0', 'price1', 'price2', 'price3', 'price4', 'price5', 'price6', 'price7',
                                    'price8', 'price9'])
# print(stock_price)
# print(stock_price['price1'])


day1_stock_price = stock_price.iloc[0]
# print(day1_stock_price)
# print(day1_stock_price[1])  # 318.76
# print(stock_price.iloc[0][0])


stock_num = 2

sum_hold_stock = MAFilter.initial_buy_stock(stock_num,
                                            stock_price)  # [['price7', 27.065064414853307, 5000.0], ['price5', 12.291052114060964, 5000.0]]
print('sum_hold_stock: ')
print(sum_hold_stock)

sum_value = []

days = [2, 50]
day_list = []

i = days[0]
while i <= days[1]:
    print('day')
    print(i)

    # 获取上一日最大的回报率
    stock_return_rate, stock_return_rate_sorted = MAFilter.stock_return_rate(i, stock_price)
    # print(stock_return_rate_sorted)
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
    # if stock_min_rate_name != max_rate:
    print('stock_price')
    print(stock_price)
    sell_money = MAFilter.sell_stock(sum_hold_stock, stock_return_rate, stock_price, i)

    if sell_money != 0:
        selt_money = MAFilter.trading_commissions(sell_money, fee=0.99)
        print('selt_money:')
        print(selt_money)
        # """

        # 购买最大率股票

        buy_stock_list = MAFilter.buy_stock(max_rate, stock_price, i, selt_money)

        sum_hold_stock.append(buy_stock_list)

    print('sum_hold_stock: ' + '666666')
    print(sum_hold_stock)

    new_sum_hold_stock = []
    for v in sum_hold_stock:
        print(v)
        print(v[0])
        # print(v[0][-1])
        a = str(v[0])
        stock_name = a
        print('stock_name000000')
        print(stock_name)
        hold_stock = []
        hold_stock.append(stock_name)

        hold_stock_volume = v[1]
        hold_stock.append(hold_stock_volume)
        # hold_stock.append(stock_price.iloc[0][i])
        stock_value = hold_stock_volume * stock_price.iloc[i][stock_name]


        hold_stock.append(stock_value)

        new_sum_hold_stock.append(hold_stock)


    print('new_sum_hold_stock')
    print(new_sum_hold_stock)

    # """

    print('----------------------------------')
    i += 1

    day_sum_value = 0
    for z in sum_hold_stock:
        day_sum_value = day_sum_value + z[3]

        # sum_value.append(z[3])

    sum_value.append(day_sum_value )
    day_list.append(days)


def draw_picture(record_list, day_list):
    iterations = list(np.arange(len(day_list)))
    # iterations = list(np.arange(len(range(10))))
    plt.figure()
    plt.plot(iterations, record_list, 'b-')
    # plt.plot(record_list, iterations, 'b-')
    # plt.plot(iterations, record_list)

    plt.title('best values record')
    plt.xlabel('Cycles')
    plt.ylabel('best value')
    plt.show()

# draw_picture(sum_value,day_list)
