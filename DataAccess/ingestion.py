import pandas as pd


class AcquireData:

    """

    ClassName  : AcquireData
    Description: This class is used to acquire/access data that is stored in the text file
    Written by : Adityaraj Hemant Chaudhari
    Version    : 0.1
    Revisions  : 0

    """

    def __init__(self):
        self.path = r'../Data/jfk_weather_cleaned.csv'

    def dataaccess(self):

        """

        Method_Name : dataaccess
        Description : This method is used to acquire the data from the data source
        Output      : Pandas DataFrame
        On_Failure  : Raise Exceptions

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : 0

        """

        try:
            data = pd.read_csv(self.path)
            return data
        except Exception as e:
            raise e



