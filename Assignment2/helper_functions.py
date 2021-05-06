"""Lambdata - Collection of Data Science Helper Functions"""
import pandas as pd
import numpy as np
from sklearn.utils import shuffle

# Confirms whether or not a DataFrame contains missing values

def null_count(df):
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 14a2f938fb8fd66aeac45935fafe6bbd701f8862
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
<<<<<<< HEAD
=======
=======
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
>>>>>>> 24c66a8d6fc242d787095221b23a2c877b1183e0
>>>>>>> 14a2f938fb8fd66aeac45935fafe6bbd701f8862
