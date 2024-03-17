import pandas as pd


def get_dataset():
    df = pd.read_csv('../../data/dataset.csv')
    return df


def get_symptom_severity():
    df = pd.read_csv('../../data/Symptom-severity.csv')
    return df


def get_symptom_description():
    df = pd.read_csv('../../data/symptom_Description.csv')
    return df


def get_precautions():
    df = pd.read_csv('../../data/symptom_precaution.csv')
    return df


def get_diabetes_data():
    df = pd.read_csv('../../data/detail/diabetes.csv')
    return df