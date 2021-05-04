class CleanUpData():
    """Way to clean up data quickly"""
    def __init__(self, df):
        self.df = df


    def null_count(self, df):
        nulls = df.isnull().sum().sum()
        return nulls


    def train_test_split(self, df):
        train, test = train_test_split(df)
        return train, test


class HelperFunctions:
    def __init__(self):
        """
        Constructor class for HelperFunctions
        """
        return
        
    def null_count(self,df):
        """
        This method returns the number of null values in a Dataframe
        """
        return df.isnull().sum().sum()