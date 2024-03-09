#import spacy


class SymptomExtractor:
    def __init__(self):
        #self.nlp = spacy.load("en_core_web_sm")
        self.symptom_keywords = set(["headache", "fever", "cough", "fatigue", "nausea", "muscle ache", "chills"])

    def extract_symptoms(self, user_input):
        #doc = self.nlp(user_input)
        extracted_symptoms = []
        #extracted_symptoms = [ent.text for ent in doc.ents if ent.text.lower() in self.symptom_keywords]
        return extracted_symptoms
