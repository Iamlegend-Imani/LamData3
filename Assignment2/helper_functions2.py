# import dataframes
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split as sk_train_test_split

# create CleanData class
class CleanData:

    # the init function
    def __init__(self):
        return

    # return the total null count in whole dataframe
    def null_count(self, df):
        return df.isnull().sum().sum()


# create class to warp Dataframes
class WarpData:

    # the init function
    def __init__(self):
        return

    # train test split a dataframe based upon a fraction
    def train_test_split(self, df, frac):
        train, test = sk_train_test_split(df, train_size=frac)
        return train, test

    # randomize the values of a dataframe
    def randomize(self, df, seed):
        df = df.sample(
            frac=1,
            axis=1,
            random_state=42).sample(
                frac=1,
                random_state=42).reset_index(drop=True)
        return df


# Create a Class to warp address series values
class WarpAddress:

    # split an address into city, state, zip into dataframe
    def addy_split(self, addy_series):
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


# # Convert State Abbreviations to State Names
# class WarpState:

#     # def function 
