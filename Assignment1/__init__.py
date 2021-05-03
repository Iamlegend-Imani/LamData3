"""LambData - A collection of Data Science helper functions"""

import pandas as pd
import numpy as np
import random
from sklearn.model_selection import train_test_split

def null_count(df):
    """This functions returns the number of null values in a Dataframe"""
    NullSum = df.isnull().sum().sum()
    return NullSum
    

def train_test_split(df, frac):
"""Create a Train/Test split function for a dataframe and returns both the Training and Testing sets. 
Frac referes to the precent of data you would like to set aside for training."""
    train, test = train_test_split()
    return train, test

def randomize(df, seed):
"""Develop a randomization function that randomizes all of a dataframes cells then returns that randomized dataframe. 
This function should also take a random seed for reproducible randomization."""
    Randomy = print(random.random())
    return Randomy


"""The below functions, I am yet to work on

# def addy_split(addy_series)
# Split addresses into three columns (df['city'], df['state'], and df['zip']) - 
# you can use regexes to detect the format and pull out important pieces."""

# def abbr_2_st(state_series, abbr_2_st=True):
# """Return a new column with the full name from a State abbreviation column -> 
# An input of FL would return Florida. 
# This function should also take a boolean (abbr_2_state) and 
# when False takes full state names and return state abbreviations. -> 
# An input of Florida would return Fl."""

# def list_2_series(list_2_series, df):
# """Single function to take a list and dataframe then turn the list into a series and 
# add it to the inputted dataframe as a new column."""

# def rm_outlier(df):
# """A 1.5*Interquartile range outlier detection/removal function that gets rid of outlying rows and 
# returns that outlier cleaned dataframe."""

# def split_dates(date_series):
# """Function to split dates of format "MM/DD/YYYY" into multiple columns (df['month'], df['day'], df['year']) 
# and then return the same dataframe with those additional columns."""
