#!/usr/bin/python3
# coding: utf8

import pandas as pd
import random


class MAFilter:

    @staticmethod
    def initial_buy_stock(stock_num, stock_price):
        money = 10000
        sum_hold_stock = []

        buy_order = random.sample(range(0, 10), 10)
        # print(buy_order)  # [1, 7, 2, 9, 6, 0, 4, 5, 8, 3]

        for i in buy_order[0:stock_num]:
            hold_stock = []
            hold_stock_volume = money / stock_num / stock_price.iloc[0][i]
            hold_stock.append('price' + str(i))
            hold_stock.append(hold_stock_volume)
            hold_stock.append(stock_price.iloc[0][i])
            stock_value = hold_stock_volume * stock_price.iloc[0][i]
            hold_stock.append(stock_value)
            sum_hold_stock.append(hold_stock)


        return sum_hold_stock

    @staticmethod
    def stock_return_rate(day, stock_price):
        day_price = stock_price.iloc[day]
        # print(day_price)

        stock_return_rate = []
        a = 0
        for i in day_price:
            last_day_price = stock_price.iloc[1][a]
            a += 1

            day_return_price = float(i) - float(last_day_price)
            day_return_rate = day_return_price / float(last_day_price) * 100
            stock_return_rate.append(day_return_rate)

        # print(stock_return_rate)  # [1.5939077304524902, -2.948941021179572, 1.2345679012345678, -0.34393809114359414, 0.18395080866015323, 0.30294074183538205, -1.0520512702715084, -1.0572826258482033, 2.931175483148958, -2.054947509492954]
        x = stock_return_rate
        b = sorted(enumerate(x), key=lambda x: x[1])
        c = [x[0] for x in b]
        # print(c)

        left_list = []
        right_list = []
        for i in c:
            # print(i)

            if stock_return_rate[i] >= 0:
                left_list.insert(0, i)
            else:
                right_list.insert(0, i)

        stock_return_rate_sorted = left_list + right_list
        # print(stock_return_rate_sorted)

        return stock_return_rate, stock_return_rate_sorted

    @staticmethod
    def return_min_rate_stock(sum_hold_stock, stock_return_rate):

        stock_num_list = []
        stock_volume_list = []
        stock_return_rate_list = []
        for i in sum_hold_stock:
            stock_name = i[0]
            stock_num = int(stock_name[-1])
            # print(stock_num)

            stock_volume = i[1]

            # if
            stock_num_list.append(stock_num)
            stock_volume_list.append(stock_volume)
            # stock_return_rate_list.append()

        if stock_return_rate[stock_num_list[0]] >= stock_return_rate[stock_num_list[1]]:
            stock_min_rate_name = stock_num_list[1]
            stock_min_volume = stock_volume_list[1]
            sum_hold_stock.remove(sum_hold_stock[1])
        else:
            stock_min_rate_name = stock_num_list[0]
            stock_min_volume = stock_volume_list[0]
            sum_hold_stock.remove(sum_hold_stock[0])

        return sum_hold_stock, stock_min_rate_name, stock_min_volume

    @staticmethod
    def sell_stock(sum_hold_stock, stock_return_rate,stock_price,day):

        sell_money = 0
        for a in sum_hold_stock:
            hold_stock_name = int(a[0][-1])
            if float(stock_return_rate[hold_stock_name]) < 0:
                day_stock_price = stock_price.iloc[day][hold_stock_name]
                day_stock_volume = a[1]
                sell_money = day_stock_price * day_stock_volume
                sell_money = a[3]

                sum_hold_stock.remove(a)

        return sell_money

    @staticmethod
    def buy_stock(max_rate, stock_price, day, sell_money):
        buy_money = sell_money * 0.99
        buy_stock_list = []
        buy_stock_name = 'price' + str(max_rate)
        buy_stock_price = stock_price[buy_stock_name][day]
        buy_stock_volume = buy_money / buy_stock_price

        buy_stock_list.append(buy_stock_name)
        buy_stock_list.append(buy_stock_volume)
        buy_stock_list.append(buy_stock_price)
        buy_stock_list.append(buy_money)

        return buy_stock_list

    @staticmethod
    def trading_commissions(money, fee=0.99):
        # fee = 0.99
        got_money = money * fee

        return got_money
