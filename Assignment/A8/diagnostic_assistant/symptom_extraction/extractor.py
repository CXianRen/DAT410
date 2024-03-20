#import spacy

from diagnostic_assistant.utils.utils import symptom_to_label


class SymptomExtractor:
    def __init__(self):
        #self.nlp = spacy.load("en_core_web_sm")
        self.symptom_keywords = set(["headache", "fever", "cough", "fatigue", "nausea", "muscle ache", "chills"])

    def extract_symptoms(self, user_input):
        #doc = self.nlp(user_input)
        extracted_symptoms = []
        symptom_to_label_keys = symptom_to_label.keys()
        for word in user_input.split():
            # remove the characters that are not alphabets
            word = ''.join(e for e in word if e.isalnum())
            if word in self.symptom_keywords:
                extracted_symptoms.append(word)
            elif word in symptom_to_label_keys:
                extracted_symptoms.append(word)
        return extracted_symptoms


class DurationExtractor:
    def __init__(self):
        self.duration_keywords = set(["day","days", "week","weeks", "month","months", "year","years"])

    def extract_duration(self, user_input):
        #doc = self.nlp(user_input)
        extracted_duration = []
        prev_word = ""
        for word in user_input.split():
            if word in self.duration_keywords:
                extracted_duration.append(prev_word + " " + word)
            prev_word = word
        return extracted_duration
    
def get_yes_or_not(text):
    postive_response = ["yes", "sure", "ok", "yeah", "yup", "yep"]
    for p in postive_response:
        if p in text:
            return True
        
    negetive_response = ["no", "not", "nope", "nah", "nay"]
    for n in negetive_response:
        if n in text:
            return False
    return None