#!/usr/bin/env python3
'''task 3'''
import pandas as pd
import numpy as np


from_file = __import__('2-from_file').from_file

df = from_file('coinbaseUSD_1-min_data_2014-12-01_to_2019-01-09.csv', ',')

df.rename(columns={'Timestamp': 'Datetime'}, inplace=True)

s
df['Datetime'] = pd.to_datetime(df['Datetime'], unit='s')


result_df = df[['Datetime', 'Close']]

print(result_df.tail())

