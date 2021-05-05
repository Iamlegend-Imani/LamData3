"""Lambdata - Collection of Data Science Helper Functions"""
import pandas as pd
import numpy as np
from sklearn.utils import shuffle

# Confirms whether or not a DataFrame contains missing values

def null_count(df):
    """This function will return the number of null values contained
    within a DataFrame"""
    return df.isnull().sum().sum()

# Randomizer
def randomize(df, seed):
    """What it does is in the comment"""
    randomized = shuffle(
                         df,
                         random_state=seed
                         )
    return randomized