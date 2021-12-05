import pandas as pd
import pickle
from sklearn.preprocessing import StandardScaler
from DataPreProcessing.Sampler import SepnSample


class Scaler:

    """

    Class_Name : Scaler
    Description: This Class is used to scale the dependent feature.
    Written By : Adityaraj Hemant Chaudhari
    Version    : 0.1
    Revisions  : None

    """

    def __init__(self):
        self.data = SepnSample()

    def stdsclr(self):

        """

        Method_Name : stdsclr
        Description : This method is used to perform scaling of data.
        output      : DataFrame
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            x, y = self.data.smpl()
            scl = StandardScaler()
            x = pd.DataFrame(scl.fit_transform(x), columns=x.columns)
            return x, y, scl
        except Exception as e:
            raise e

    def serializesclr(self):

        """
        Method_Name : serializesclr
        Description : This method is used to stor the scalar in serialized format in pickle file.
        output      : DataFrame
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None
        """

        try:
            a, b, s = self.stdsclr()
            pickle.dump(s, open('Scalar.pkl', 'wb'))
        except Exception as e:
            raise e





