import pickle
import numpy as np

model = pickle.load(open('./ModelSaver/model.pkl', 'rb'))
scalar = pickle.load(open('./DataPreProcessing/Scalar.pkl', 'rb'))

s = scalar.transform([[71.0, 96.0, 0.0, 0.0, 30.02, 0.01, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]])
print(s)
a = (model.predict(s))
print(a)
print(type(a))