#! /usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib
import matplotlib.pyplot as plt

import numpy as np
import pandas as pd
import pandas_datareader.data as pdd
import datetime as dt

font = {'family' : 'meiryo'}
matplotlib.rc('font', **font)

axs = []
ax = None
FIG_SIZE = (20,10)
ALPHA = 0.5

# http://api.bitcoincharts.com/v1/csv/

for csv in ['coincheck', 'bitflyer', 'kraken']:
    df = pd.read_csv(csv + 'JPY.csv')
#     df = df[df['jpy'] > 200000]
#     df = df[df['time'] >= 1500076800]
#     df = df[df['time'] <= 1500152400]
    df['date'] = pd.to_datetime(df['time'], unit='s')
    label = csv + '-JPY'
    df.rename(columns={'jpy': label}, inplace=True)
    if ax is None:
        ax = df.plot(x=['date'], y=label, figsize=FIG_SIZE, alpha=ALPHA)
    else:
        ax = df.plot(x=['date'], y=label, figsize=FIG_SIZE, alpha=ALPHA, ax=ax)

# plt.ylim(208000, 260000)
plt.show()
