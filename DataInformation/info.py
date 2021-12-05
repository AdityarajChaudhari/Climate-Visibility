import pandas as pd
from DataAccess.ingestion import AcquireData


class DataInfo:

    """

    Class Name : DataInfo
    Description: This class is used to figure out size and shape and overall info of data we loaded previously
    written by : Adityaraj Hemant Chaudhari
    version    : 0.1
    revisions  : None

    """

    def __init__(self):
        self.data = AcquireData()

    def shape(self):

        """

        Method_Name : shape
        Description : This method is used to get the shape of the dataset loaded previously
        Output      : 2-D array/DataFrame
        On failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            data = self.data.dataaccess()
            return data.shape
        except Exception as e:
            raise e

    def size(self):

        """

        Method_Name : size
        Description : This method is used to get the size of the dataset loaded previously
        Output      : 2-D array/DataFrame
        On failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            data = self.data.dataaccess()
            return data.size
        except Exception as e:
            raise e

    def info(self):

        """

        Method_Name : info
        Description : This method is used to get the info of the dataset loaded previously
        Output      : 2-D array/DataFrame
        On failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            data = self.data.dataaccess()
            return data.info()
        except Exception as e:
            raise e
