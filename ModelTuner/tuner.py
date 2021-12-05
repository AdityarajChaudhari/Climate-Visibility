from sklearn.model_selection import RandomizedSearchCV
from sklearn.svm import SVC
from ModelBuilding.model import ModelBuilder
from DataSplitter.split import Splitter


class Tuner:

    """

    Class_Name : Tuner
    Description: This Class is used to perform hyperparameter tuning on the Support Vector Machine Classifier.
    Written By : Adityaraj Hemant Chaudhari
    Version    : 0.1
    Revisions  : None

    """

    def __init__(self):
        self.model = ModelBuilder()
        self.data = Splitter()

    def modeltuner(self):

        """

        Method Name : modeltuner
        Description : This method is used to choose the best parameters for Support Vector Classifier and assigning it with set of values which can help our model to give better results.
        output      : generalized model
        On_failure  : Raise Exception

        Written By  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revision    : None

        """

        try:
            x_train, x_test, y_train, y_test = self.data.splitdata()
            svc = self.model.svcmodel()
            params = {
                'kernel': ['linear', 'rbf', 'sigmoid'],
                'degree': [i for i in range(1, 10, 1)],
                'gamma': ['scale', 'auto'],
                'decision_function_shape': ['ovr'],
                'C': [i for i in range(1, 20, 1)]
            }
            randomcv_svc = RandomizedSearchCV(svc, param_distributions=params, n_jobs=-1, cv=3, n_iter=100, verbose=True)
            randomcv_svc.fit(x_train, y_train)
            svc_best = randomcv_svc.best_params_
            svc_clf = SVC(decision_function_shape=svc_best['decision_function_shape'],
                          kernel=svc_best['kernel'],
                          degree=svc_best['degree'],
                          gamma=svc_best['gamma'],
                          C=svc_best['C'])
            svc_clf.fit(x_train, y_train)
            print("After HyperParameter Tuning :- ")
            print("Training Score :- ", round(svc_clf.score(x_train, y_train), 4))
            print("Testing Score :- ", round(svc_clf.score(x_test, y_test), 4))
            return svc_clf
        except Exception as e:
            raise e