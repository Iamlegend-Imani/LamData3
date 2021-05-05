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
    NullSum = df.isnull().sum().sum()
    return NullSum
    

def train_test_split(dg):
    """Create a Train/Test split function for a dataframe and returns both the Training and Testing sets. 
    Frac referes to the precent of data you would like to set aside for training."""
    train, test = train_test_split(dg)
    return train, test
    # train, test = df.train_test_split(df,frac=0.2)
    # return (train, test)

def randomize(dg, seed):
    """Develop a randomization function that randomizes all of a dataframes cells then returns that randomized dataframe. 
    This function should also take a random seed for reproducible randomization."""
    Randomy = randomize(dg, seed==101)
    return Randomy

# def split_dates(date_series):
#     """Splits date into month, day and year"""
#     ds = pd.DataFrame()
#     ds['date'] = date_series
#     ds[["day","month","year"]] = ds['date'].str.split("/", expand=True)
#     ds.drop(columns = 'date',inplace=True)
#     return ds

def split_dates(date_series):
    """This function converts date column to a year, month, day column"""
    ds = pd.DataFrame()
    ds['year'] = pd.Series(ds[date_series].dt.year)
    ds['month'] = pd.Series(ds[date_series].dt.month)
    ds['day'] = pd.Series(ds[date_series].dt.day)
    return ds

if __name__ == "__main__":
    print(null_count(dg))
    print(randomize(dg, seed=101))
    print(train_test_split(dg, frac=0.1))
    