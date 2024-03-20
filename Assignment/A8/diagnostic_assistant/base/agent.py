import os

import numpy as np
from diagnostic_assistant.model.FCModel import FCModel
from diagnostic_assistant.preprocess.load_data import get_symptom_severity, get_symptom_description, \
    get_precautions, get_dataset
from diagnostic_assistant.utils.utils import symptom_to_label, \
    label_to_symptom, disease_to_label, label_to_disease,\
    convert_dis_to_onehot, convert_to_onehot, convert_to_symptoms, convert_to_disease, \
    get_best_match_symptoms
    
class DiagnosticAgent:

    def __init__(self):
        self.model = FCModel()
        self.detail_model = None
        self.processed_data = None

    def ask_matching_symptoms(self, symptoms):
        all_symptoms = symptom_to_label.keys()
        return get_best_match_symptoms(symptoms, all_symptoms)

    def ask_disease(self, symptoms):
        all_symptoms = symptom_to_label.keys()
        symptoms = get_best_match_symptoms(symptoms, all_symptoms)
        
        x = [symptom_to_label[symptom] for symptom in symptoms]
        x = convert_to_onehot(x)

        return self.model.predict_topN(x)

    def ask_other_symptoms(self, disease):
        df = get_dataset()
        df = df[df['Disease'] == disease]
        symptom_set = []
        for idx, row in df.iterrows():
            for i in range(1, len(row)):
                if type(row[i]) is float:
                    continue
                else:
                    if row[i] not in symptom_set:
                        symptom_set.append(row[i])                    
        return symptom_set

    def ask_description(self, disease):
        df_desc = get_symptom_description()
        disp = df_desc[df_desc['Disease'] == disease]
        return disp.values[0][1]

    def ask_precautions(self, disease):
        df_precautions = get_precautions()
        precuation_list = []
        try:
            c = np.where(df_precautions['Disease'] == disease)[0][0]
            for i in range(1, len(df_precautions.iloc[c])):
                precuation_list.append(df_precautions.iloc[c, i])
        except:
            pass

        return ",".join(precuation_list)

    def ask_accuracy(self):
        return self.model.evaluate()

    def ask_disease_confirmation(self, parameters):
        if self.detail_model is None:
            self.train_detail()

        disease_confirmed = self.detail_model.predict(input=[parameters])[0]== 1

        return disease_confirmed