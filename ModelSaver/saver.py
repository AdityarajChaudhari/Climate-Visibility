import pickle
from ModelTuner.tuner import Tuner


class ModelSaving:

    """

    Class_Name : ModelSaving
    Description: This Class is used to save the model in serialized format.
    Written By : Adityaraj Hemant Chaudhari
    Version    : 0.1
    Revisions  : None

    """

    def __init__(self):
        self.model = Tuner()
        self.path = "model.pkl"
        self.mode = "wb"

    def serializedmodel(self):

        """

        Method_Name : serializemodel
        Description : This method is used to save the model in the serialized format in the pickle file.
        output      : Pickle File
        on failure  : raise exception

        Written by  : Adityaraj Hemant Chaudhari
        Version     : 0.1
        Revisions   : None

        """

        try:
            svc = self.model.modeltuner()
            pickle.dump(svc, open(self.path, self.mode))
        except Exception as e:
            raise e

