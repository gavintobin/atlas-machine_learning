#!/usr/bin/env python3
'''task 3'''
import pandas as pd
import numpy as np


def from_data(array):
    '''python dicf'''
    num_columns = array.shape[1]


    column_labels = [chr(i) for i in range(ord('A'), ord('A') + num_columns)]


    df = pd.DataFrame(array, columns=column_labels)

    return df

