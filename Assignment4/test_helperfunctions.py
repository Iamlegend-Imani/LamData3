""" File where testing references are stores """

import pandas as pd
import numpy as np
import pytest
from Assignment2.helper_functions import CleanData, WarpData, WarpAddress

# Reference Dataframe for CleanData, WarpData testing
df = pd.DataFrame(
    np.array(
        [
            [1, 2, 3, 4, 5],
            [4, np.nan, 6, 24, 26],
            [7, 8, 9, 123, np.nan]
        ]
    ),
    columns=['a', 'b', 'c', 'd', 'e'])

# Testing CleanData class


def test_type_int():
    '''Check that null_count returns integer'''
    null_count = CleanData().null_count(df)
    assert isinstance(null_count, np.int64)


def test_count_null():
    '''Check that null_count returns correct number of nulls'''
    null_count = CleanData().null_count(df)
    assert null_count == 2


# Testing WarpData class
def test_type_int():
    '''Check training and test sets length'''
    train, test = WarpData().train_test_split(df, 0.4)
    assert len(train) < len(df)
    assert len(test) < len(df)
    assert len(train) < len(test)


def test_randomize_len():
    '''Check len of randomize df'''
    df_rand = WarpData().randomize(df, 42)
    assert len(df_rand) == len(df)


# Address series for WarpAddress class testing
addresses = [
    '890 Jennifer Brooks\nNorth Janet, WY 24785',
    '8394 Kim Meadow\nDarrenville, AK 27389',
    '379 Cain Plaza\nJosephburgh, WY 06332',
    '5303 Tina Hill\nAudreychester, VA 97036'
]


# # Import State_Abbr CSV as df
# state_abb = pd.read_csv('State_Abbr.csv')

# state_abb

