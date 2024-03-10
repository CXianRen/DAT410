def get_possible_disease_with_symptoms(symptoms):
    # Fungal infection,itching, skin_rash, nodal_skin_eruptions, dischromic_patches
    # Chronic cholestasis,itching, vomiting, yellowish_skin, nausea, loss_of_appetite, abdominal_pain, yellowing_of_eyes
    return [("Fungal infection", 0.4), ("Chronic",0.4)]

def get_possible_symptoms_of_disease(disease):
    if disease == "Fungal infection":
        return ["itching", "skin_rash", "nodal_skin_eruptions", "dischromic_patches"]
    if disease == "Chronic":
        return ["itching", "vomiting", "yellowish_skin", "nausea", "loss_of_appetite", "abdominal_pain", "yellowing_of_eyes"]
    
def get_symptoms_from_text(text):
    sdict = ["itching", "vomiting", "yellowish_skin", "nausea", "loss of appetite", "abdominal pain", "yellowing of eyes"]
    symptoms = []
    for s in sdict:
        if s in text:
            symptoms.append(s)
    return symptoms

def get_duration_from_text(text):
    sdict = ["day", "week", "month", "year"]
    duration = []
    for s in sdict:
        if s in text:
            duration.append(s)
    return duration

def get_symptoms_severity_duration_from_text(history_text, new_text):
    symptoms = get_symptoms_from_text(new_text)
    severity = []
    duration = get_duration_from_text(new_text)

    return symptoms, severity, duration

def get_yes_or_not(text):
    if "yes" in text:
        return True
    if "no" in text:
        return False
    return None