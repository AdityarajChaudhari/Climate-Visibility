from DataSplitter.split import Splitter
from sklearn.svm import SVC


class ModelBuilder:

    """

    Class_Name : ModelBuilder
    Description: This Class is used to build the model.
    Written By : Adityaraj Hemant Chaudhari
    Version    : 0.1
    Revisions  : None

    """

    def __init__(self):
        self.data = Splitter()

    def svcmodel(self):

        """

        Method_Name : svcmodel
        Description : This method is used to train the support vector machine model for classification
        output      : model
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            x_train, x_test, y_train, y_test = self.data.splitdata()
            svc = SVC()
            svc.fit(x_train, y_train)
            return svc
        except Exception as e:
            raise e





