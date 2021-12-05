import pandas as pd
import numpy as np
from DataPreProcessing.FeatEngg import Preprocessor
from imblearn.under_sampling import RandomUnderSampler


class SepnSample:

    """

    Class_Name : SepnSample
    Description: This Class is used to seperate the dependent and independent features and perform Under Sampling.
    Written By : Adityaraj Hemant Chaudhari
    Version    : 0.1
    Revisions  : None

    """

    def __init__(self):
        self.data = Preprocessor()

    def sepdata(self):

        """

        Method_Name : sepdata
        Description : This method is used to separate the dependent and independent features.
        output      : DataFrame
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            data = self.data.dropfeat()
            data = data[~data.isin([np.nan, np.inf, -np.inf]).any(1)]
            x = data.drop('VISIBILITY', axis=1)
            y = data['VISIBILITY']
            return x, y
        except Exception as e:
            raise e

    def smpl(self):

        """
        Method_Name : smpl
        Description : This method is used to perform under sampling on the data.
        output      : DataFrame
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None
        """
        
        try:
            x, y = self.sepdata()
            rus = RandomUnderSampler()
            x, y = rus.fit_resample(x, y)
            return x, y
        except Exception as e:
            raise e

