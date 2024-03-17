import os

import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
import numpy as np
from diagnostic_assistant.model.model import Model
from diagnostic_assistant.preprocess.data_clean import pre_process_data, pre_process_diabetes_data
from diagnostic_assistant.preprocess.load_data import get_dataset, get_symptom_severity, get_symptom_description, \
    get_precautions, get_diabetes_data
from diagnostic_assistant.utils.utils import get_best_match_symptoms
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import  MaxAbsScaler
from sklearn.ensemble import ExtraTreesClassifier

class DiagnosticAgent:

    def __init__(self):
        self.model = None
        self.detail_model = None
        self.processed_data = None

    def train(self):
        data = get_dataset()
        self.processed_data = pre_process_data(data)
        features = self.processed_data.iloc[:, 1:].values
        labels = self.processed_data['Disease'].values

        #decisionTree = DecisionTreeClassifier(criterion='gini', random_state=42, max_depth=13)
        randomForest = RandomForestClassifier()

        model = Model('random_forest_model', randomForest, features, labels)
        if not model.is_trained('random_forest_model'):
            model.fit()
            model.save()
        self.model = model

    def train_detail(self):
        diabetes_data = get_diabetes_data()
        diabetes_data = pre_process_diabetes_data(diabetes_data)
        features = diabetes_data.drop(columns=['outcome'])
        labels = diabetes_data['outcome']

        model_pipeline = Pipeline([
            ('scaler', MaxAbsScaler()),
            ('classifier', ExtraTreesClassifier(verbose=0))
        ])

        model = Model('extra_tree_classifier', model_pipeline, features, labels)
        if not model.is_trained('extra_tree_classifier'):
            model.fit()
            model.save()
        self.model = model

    def ask_matching_symptoms(self, symptoms):
        df_severity = get_symptom_severity()
        df_severity['Symptom'] = df_severity['Symptom'].str.replace('_', ' ')
        all_symptoms = df_severity['Symptom'].unique()
        symptoms = [x.replace('_', ' ') for x in symptoms]
        return get_best_match_symptoms(symptoms, all_symptoms)

    def ask_disease(self, symptoms):
        if self.model is None:
            self.train()

        df_severity = get_symptom_severity()
        df_severity['Symptom'] = df_severity['Symptom'].str.replace('_', ' ')

        all_symptoms = df_severity['Symptom'].unique()

        symptoms = [x.replace('_',' ') for x in symptoms]
        symptoms = get_best_match_symptoms(symptoms, all_symptoms)

        features = [0] * 17

        a = np.array(df_severity["Symptom"])
        b = np.array(df_severity["weight"])
        for j in range(len(symptoms)):
            for k in range(len(a)):
                if symptoms[j] == a[k]:
                    features[j] = b[k]

        self.disease = self.model.predict(input=[features])
        print(self.disease)
        return self.disease

    def ask_other_symptoms(self, disease):
        df = self.processed_data
        row = df.loc[df['Disease'] == disease[0]].drop(columns=['Disease']).values.tolist()
        return row

    def ask_description(self, disease):
        df_desc = get_symptom_description()
        disp = df_desc[df_desc['Disease'] == disease[0]]
        return disp.values[0][1]

    def ask_precautions(self, disease):
        df_precautions = get_precautions()
        c = np.where(df_precautions['Disease'] == disease[0])[0][0]
        precuation_list = []
        for i in range(1, len(df_precautions.iloc[c])):
            precuation_list.append(df_precautions.iloc[c, i])

        return ",".join(precuation_list)

    def ask_accuracy(self):
        return self.model.evaluate()

    def ask_detail_disease(self, parameters):
        if self.detail_model is None:
            self.train_detail()

        return self.model.predict(input=[parameters])