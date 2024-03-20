from difflib import get_close_matches
from itertools import chain
from diagnostic_assistant.preprocess.load_data import *
import numpy as np

def show_data(df):
    print(df.describe())
    print(df.head())

def get_best_match_symptoms(symptoms:list, all_symptoms):
    matched_symptoms = []
    for symptom  in symptoms:
        closest_match = get_close_matches(symptom, all_symptoms, n=1, cutoff=0.6)
        matched_symptoms.append(closest_match)

    return list(chain.from_iterable(matched_symptoms))


def map_init():
    df_symptoms = get_symptom_severity()
    symptoms = df_symptoms.iloc[:, 0].values
    # print(symptoms)

    # convert the symptoms to labels, and the labels to symptoms
    symptom_to_label = {symptom.strip(): i+1 for i, symptom in enumerate(symptoms)}
    label_to_symptom = {i+1: symptom.strip() for i, symptom in enumerate(symptoms)}

    df_disease = get_precautions()
    diseases = df_disease.iloc[:, 0].values
    # cluster the diseases
    diseases = list(set(diseases))
    diseases.sort()
    # convert the diseases to labels, and the labels to diseases
    disease_to_label = {disease.strip(): i+1 for i, disease in enumerate(diseases)}
    label_to_disease = {i+1: disease.strip() for i, disease in enumerate(diseases)}
    return symptom_to_label, label_to_symptom, disease_to_label, label_to_disease

symptom_to_label, label_to_symptom, disease_to_label, label_to_disease = map_init()

def convert_to_onehot(symptoms):
    onhot_symptoms = np.zeros(len(symptom_to_label))
    for symptom in symptoms:
        if symptom == 0:
            continue
        onhot_symptoms[symptom-1] = 1
        # print(symptom)
    return onhot_symptoms

def convert_dis_to_onehot(disease):
    onhot_disease = np.zeros(len(disease_to_label))
    onhot_disease[disease-1] = 1
    return onhot_disease

# convert onehot to symptoms
def convert_to_symptoms(onehot_symptoms):
    symptoms = []
    for i in range(len(onehot_symptoms)):
        if onehot_symptoms[i] == 1:
            symptoms.append(label_to_symptom[i+1])
    return symptoms

# convert onehot to disease
def convert_to_disease(onehot_disease):
    for i in range(len(onehot_disease)):
        if onehot_disease[i] == 1:
            return label_to_disease[i+1]
