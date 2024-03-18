import os

from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import joblib
import numpy as np


class Model:
    def __init__(self, name, model, data, labels, train_spilt_size=0.8):
        self.name = name
        self.model = model
        self.data = data
        self.labels = labels
        self.x_train, self.x_test, self.y_train, self.y_test = train_test_split(self.data, self.labels,
                                                                                train_size=train_spilt_size,
                                                                                random_state=42)
        self.predictions = None
        self.trained_model_path =  os.path.dirname(os.path.abspath(__file__))+"/trained/"

    def fit(self):
        self.model.fit(self.x_train, self.y_train)

    def save(self):
        joblib.dump(self.model, self.trained_model_path + self.name + '.joblib')

    def predict(self, input):
        _model = joblib.load(self.trained_model_path + self.name + '.joblib')
        if input:
            self.predictions = _model.predict(input)
        else:
            self.predictions = _model.predict(self.x_test)

        return self.predictions

    def predict_proba(self, input):
        _model = joblib.load(self.trained_model_path + self.name + '.joblib')
        self.predictions = _model.predict_proba(input)
        top3_indices = self.predictions.argsort(axis=1)[:, -3:] 
        top3_probabilities = np.take_along_axis(self.predictions, top3_indices, axis=1)
        
        print("DEBUG: top3_indices:", top3_indices)
        print("DEBUG: top3_probabilities:", top3_probabilities)
        print("DEBUG: labels:", self.labels[top3_indices])
       
        return self.predictions
    
    def evaluate(self):
        y_pred = self.predict()
        accuracy = accuracy_score(self.y_test, y_pred)
        precision = precision_score(self.y_test, y_pred, average='macro')
        recall = recall_score(self.y_test, y_pred, average='macro')
        f1 = f1_score(self.y_test, y_pred, average='macro')

        stats = f"""Accuracy: {accuracy}
Precision: {precision}
Recall: {recall}
F1-score: {f1}
        """

        print("Accuracy:", accuracy)
        print("Precision:", precision)
        print("Recall:", recall)
        print("F1-score:", f1)

        #cm = confusion_matrix(self.y_test, y_pred)
        #disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        #disp.plot()
        #plt.title('Confusion Matrix')
        #plt.show()
        return stats

    def is_trained(self, name):
        return os.path.exists(self.trained_model_path + self.name + '.joblib')
