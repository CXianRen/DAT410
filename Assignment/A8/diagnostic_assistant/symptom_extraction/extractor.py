#import spacy

from diagnostic_assistant.utils.utils import symptom_to_label

import editdistance
import re
class SymptomExtractor:
    def __init__(self):
        self.symptom_keywords = set(symptom_to_label.keys())
        #self.nlp = spacy.load("en_core_web_sm")
        
    def extract_symptoms(self, user_input):
        print(user_input)
        extracted_symptoms = []
        for word in re.split(r'[,:| ]', user_input ):
            # remove the characters that are not alphabets
            word = ''.join(e for e in word if e.isalnum())
            for symptom in self.symptom_keywords:
                dist = editdistance.eval(word.lower(), symptom.lower())
                max_len = max(len(word), len(symptom))
                similarity = 1 - dist/max_len
                if similarity > 0.6:
                    extracted_symptoms.append(symptom) 
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