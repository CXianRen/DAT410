from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import joblib

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

    def fit(self):
        self.model.fit(self.x_train, self.y_train)

    def save(self):
        joblib.dump(self.model, self.name+'.joblib')

    def predict(self, input):
        _model = joblib.load(self.name+'.joblib')
        if input:
            self.predictions = _model.predict(input)
        else:
            self.predictions = _model.predict(self.x_test[0])

        return self.predictions

    def evaluate(self):
        accuracy = accuracy_score(self.y_test, self.predictions)
        precision = precision_score(self.y_test, self.predictions)
        recall = recall_score(self.y_test, self.predictions)
        f1 = f1_score(self.y_test, self.predictions)

        print("Accuracy:", accuracy)
        print("Precision:", precision)
        print("Recall:", recall)
        print("F1-score:", f1)

        cm = confusion_matrix(self.y_test,self. predictions)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot()
        plt.title('Confusion Matrix')
        plt.show()

