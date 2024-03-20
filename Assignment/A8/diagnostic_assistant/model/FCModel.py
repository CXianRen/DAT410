import os
import pickle
from sklearn.neural_network import MLPClassifier
import numpy as np

class FCModel():
    def __init__(self, model_path=
                 os.path.join(os.path.dirname(__file__),
                "./trained/finalized_model.sav")) -> None:
        self.model_path = model_path
        self.model= pickle.load(open(self.model_path, 'rb'))
    
    def predict_proba(self, X):
        return self.model.predict_proba(X)
    
    def predict_topN(self, X, N=10):
        predict = self.model.predict_proba([X])
        # get top3 diseases
        topN = np.argsort(predict[0])[-N:]
        # print("topN:",topN)
        # print("topN:",[convert_to_disease(conver_dis_to_onhot(label+1)) for label in topN])
        # print("topN:",predict[0][topN])
        return topN, predict[0][topN]
    