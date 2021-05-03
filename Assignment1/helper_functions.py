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
