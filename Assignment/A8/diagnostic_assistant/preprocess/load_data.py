import pandas as pd
import os


def get_dataset():
    df = pd.read_csv(os.path.join(
        os.path.dirname(__file__), '../../data/dataset.csv'))
    return df


def get_symptom_severity():
    # df = pd.read_csv('../../data/Symptom-severity.csv')
    df = pd.read_csv(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '../../data/Symptom-severity.csv'))
    return df


def get_symptom_description():
    # df = pd.read_csv('../../data/symptom_Description.csv')
    df = pd.read_csv(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '../../data/symptom_Description.csv'))
    return df


def get_precautions():
    # df = pd.read_csv('../../data/symptom_precaution.csv')
    df = pd.read_csv(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '../../data/symptom_precaution.csv'))
    return df


def get_diabetes_data():
    # df = pd.read_csv('../../data/detail/diabetes.csv')
    df = pd.read_csv(os.path.join(
        os.path.dirname(os.path.abspath(__file__)), '../../data/detail/diabetes.csv'))
    return df
