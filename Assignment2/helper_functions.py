"""LambData - A collection of Data Science helper functions"""

import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split
import math
import sys
sys.setrecursionlimit(5000)

lists = [0,20,None,100,50,30,None,0,20,50]
dg = pd.DataFrame(lists)
df = pd.DataFrame()

def null_count(df):
    """This functions returns the number of null values in a Dataframe"""
    return df.isnull().sum().sum()
    

def train_test_split(dg,frac):
    """Create a Train/Test split function for a dataframe and returns both the Training and Testing sets. 
    Frac referes to the precent of data you would like to set aside for training."""
    train, test = sk_train_test_split(df, train_size=frac)
    return train, test

def randomize(df, seed):
    """Develop a randomization function that randomizes all of a dataframes cells then returns that randomized dataframe. 
    This function should also take a random seed for reproducible randomization."""
    df = df.sample(
            frac=1,
            axis=1,
            random_state=42).sample(
                frac=1,
                random_state=42).reset_index(drop=True)
    return df

def addy_split(df, addy_series):
        # convert addresses into series
    addr = pd.Series(addy_series)

        # Split Address  on '\n'
    add1 = addr.str.split('\n')

        # Get city state and zip into column
    df_add = pd.DataFrame(add1)

    for i, val in enumerate(addr):
        if i < len(addr):
            df_add['city_st_zip'] = add1[i][1]
            i += 1

        # Split city_st_zip on ','
    city_st_zip = df_add['city_st_zip'].str.split(',')

        # Put city into column
    for i, val in enumerate(city_st_zip):
        if i < len(city_st_zip):
            df_add['city'] = city_st_zip[i][0]
            df_add['st_zip'] = city_st_zip[i][1]
            i += 1

        # Split st_zip on ' '
    st_zip = df_add['st_zip'].str.split(' ')

        # Put state and zip into columns
    for i, val in enumerate(st_zip):
        if i < len(st_zip):
            df_add['state'] = st_zip[i][1]
            df_add['zip'] = st_zip[i][2]
            i += 1

        # Drop unnessary columns
    drop_cols = [0, 'city_st_zip', 'st_zip']
    df_add.drop(
        columns=drop_cols,
        inplace=True
        )

    return df_add
