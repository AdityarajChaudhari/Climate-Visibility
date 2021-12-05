import pandas as pd
import numpy as np
from datetime import datetime
from DataAccess.ingestion import AcquireData
pd.set_option('display.max_columns', None)


class Preprocessor:

    """

    Class_Name : PreProcessor
    Description: This Class is used to Perform Feature Engineering.
    Written By : Adityaraj Hemant Chaudhari
    Version    : 0.1
    Revisions  : None

    """

    def __init__(self):
        self.data = AcquireData()

    def getmonth(self):

        """

        Method_Name : getmonth
        Description : This method is used to get the month name from the date column
        output      : DataFrame
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            data = self.data.dataaccess()
            data['month'] = pd.DatetimeIndex(data['DATE']).month_name()
            return data
        except Exception as e:
            raise e

    def transform(self):

        """

        Method_Name : transform
        Description : This method is used to transform the dependent feature based on certain condition.
        output      : DataFrame
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            data = self.getmonth()
            bins = (0, 4, 8, 10)
            group_names = [3, 2, 1]   #1-High Visi 2-Medium Visi 3-Low/No Visi
            data['VISIBILITY'] = pd.cut(data['VISIBILITY'], bins=bins, labels=group_names)
            return data
        except Exception as e:
            raise e

    def logtrnsfrm(self):

        """

        Method_Name : logtrnsfrm
        Description : This is used to perform log transformation on some of the features to counter skewed distribution.
        output      : DataFrame
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            data = self.transform()

            def log(col_name):
                data[col_name] = np.log2(data[col_name])
            log('DRYBULBTEMPF')
            log('StationPressure')
            data['WindSpeed'] = data['WindSpeed'].replace(0,0.5)
            log('WindSpeed')
            return data
        except Exception as e:
            raise e

    def transformfeature(self):

        """

        Method_Name : transformfeature
        Description : This method is used to derive new value from the feature using some condition.
        output      : DataFrame
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            data = self.logtrnsfrm()
            data['Precip'] = np.where(data['Precip'] == 0, 0, 1) #0-No Precip 1-Precip Present
            return data
        except Exception as e:
            raise e

    def onehotencoder(self):

        """

        Method_Name : onehotencoder
        Description : This method is used to perform one hot encoding.
        output      : DataFrame
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            data = self.transformfeature()
            x = pd.get_dummies(data['month'], drop_first=True)
            data = pd.concat((data,x),axis=1)
            return data
        except Exception as e:
            raise e

    def dropfeat(self):

        """

        Method_Name : dropfeat
        Description : This method is used to drop features.
        output      : DataFrame
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            data = self.onehotencoder()
            data.drop(['WETBULBTEMPF', 'SeaLevelPressure', 'DewPointTempF','month','DATE'], axis=1, inplace=True)
            return data
        except Exception as e:
            raise e


p = Preprocessor()
p.dropfeat()
