from sklearn.model_selection import train_test_split
from DataPreProcessing.Scalar import Scaler


class Splitter:

    """

    Class_Name : Splitter
    Description: This Class is used to split the datainto training and testing sets.
    Written By : Adityaraj Hemant Chaudhari
    Version    : 0.1
    Revisions  : None

    """

    def __init__(self):
        self.data = Scaler()

    def splitdata(self):

        """

        Method_Name : splitdata
        Description : This method is used to split the data into train and test sets.
        output      : DataFrame
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            x, y, z = self.data.stdsclr()
            x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.33, random_state=100)
            return x_train, x_test, y_train, y_test
        except Exception as e:
            raise e


