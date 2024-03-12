from difflib import get_close_matches
from itertools import chain

def show_data(df):
    print(df.describe())
    print(df.head())


def get_best_match_symptoms(symptoms:list, all_symptoms):
    matched_symptoms = []
    for symptom  in symptoms:
        closest_match = get_close_matches(symptom, all_symptoms, n=1, cutoff=0.6)
        matched_symptoms.append(closest_match)

    return list(chain.from_iterable(matched_symptoms))