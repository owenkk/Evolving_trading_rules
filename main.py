#!/usr/bin/python3
# coding: utf8

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

from utils.stock_functions import MAFilter

# all csv data
initial_data = pd.read_csv("./data/Training_data.csv",
                           names=['volume0', 'price0', 'volume1', 'price1', 'volume2', 'price2', 'volume3', 'price3',
                                  'volume4', 'price4'
                               , 'volume5', 'price5', 'volume6', 'price6', 'volume7', 'price7', 'volume8', 'price8',
                                  'volume9', 'price9'])

# all stock volume data
stock_trading_volume = pd.DataFrame(initial_data,
                                    columns=['volume0', 'volume1', 'volume2', 'volume3', 'volume4', 'volume5',
                                             'volume6', 'volume7', 'volume8', 'volume8'])
# all stock price data
stock_price = pd.DataFrame(initial_data,
                           columns=['price0', 'price1', 'price2', 'price3', 'price4', 'price5', 'price6', 'price7',
                                    'price8', 'price9'])

# first buy the number of stock
stock_num = 2

# hold stock data
sum_hold_stock = MAFilter.initial_buy_stock(stock_num,
                                            stock_price)  # [['price7', 27.065064414853307, 5000.0], ['price5', 12.291052114060964, 5000.0]]

# stock sum of value
sum_value = []

#
days = [2, 500]
day_list = []

i = days[0]
while i <= days[1]:

    # return the stock return rate
    stock_return_rate, stock_return_rate_sorted = MAFilter.stock_return_rate(i, stock_price)
    # max stock return rate
    max_rate = stock_return_rate_sorted[0]
    # min stock return rate
    min_rate = stock_return_rate_sorted[9]

    stock_min_rate_name = min_rate
    # if stock return rate<0 , will sell the stock out
    sell_money = MAFilter.sell_stock(sum_hold_stock, stock_return_rate, stock_price, i)

    if sell_money != 0:
        selt_money = MAFilter.trading_commissions(sell_money, fee=0.99)

        # buy a new stock
        buy_stock_list = MAFilter.buy_stock(max_rate, stock_price, i, selt_money)

        sum_hold_stock.append(buy_stock_list)

    new_sum_hold_stock = []
    for v in sum_hold_stock:
        stock_name = str(v[0])

        new_hold_stock = []
        new_hold_stock.append(stock_name)

        hold_stock_volume = v[1]
        new_hold_stock.append(hold_stock_volume)
        stock_value = hold_stock_volume * stock_price.iloc[i][stock_name]

        new_hold_stock.append(stock_value)

        new_sum_hold_stock.append(new_hold_stock)

    # current hold stock data
    print('new_sum_hold_stock')
    print(new_sum_hold_stock)

    print('----------------------------------')
    i += 1

    day_sum_value = 0
    for z in new_sum_hold_stock:
        day_sum_value = day_sum_value + z[2]

        # sum_value.append(z[3])

    sum_value.append(day_sum_value)
    day_list.append(days)


def draw_picture(record_list, day_list):
    iterations = list(np.arange(len(day_list)))
    plt.figure()
    plt.plot(iterations, record_list, 'b-')

    plt.title('best values record')
    plt.xlabel('Days')
    plt.ylabel('best value')
    plt.show()

# draw picture function
draw_picture(sum_value,day_list)

