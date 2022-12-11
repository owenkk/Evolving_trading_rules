#!/usr/bin/python3
# coding: utf8
# 导入相关模块
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# 读入股票数据
dataset = pd.read_csv('../data/Training_data.csv')

# 画图
plt.plot(dataset['Close'])

# 计算移动平均线
ma5 = dataset['Close'].rolling(window=5).mean()
ma10 = dataset['Close'].rolling(window=10).mean()

# 将移动平均线显示在图中
plt.plot(ma5, label='MA5')
plt.plot(ma10, label='MA10')
plt.legend()

# 初始化账户
cash = 0
stock = 0

# 根据移动平均线买卖股票
for i in range(len(dataset)):
    # 如果MA5大于MA10，买入股票
    if ma5[i] > ma10[i] and cash == 0:
        stock = 100
        cash = cash - dataset['Close'][i] * 100
    # 如果MA5小于MA10，卖出股票
    elif ma5[i] < ma10[i] and stock == 100:
        cash = cash + dataset['Close'][i] * 100
        stock = 0

# 输出最终的现金和股票的数量
print("最终的现金：", cash)
print("最终的股票：", stock)