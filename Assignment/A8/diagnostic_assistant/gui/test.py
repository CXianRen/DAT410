from diagnostic_assistant.base.agent import DiagnosticAgent


agent = DiagnosticAgent()

symptoms = ['itching']
matching_symptoms = agent.ask_matching_symptoms(symptoms)
print("[DEBUG] matching_symptoms:", matching_symptoms) 
disease = agent.ask_disease(symptoms)
print("[DEBUG] disease:", disease)

# description = agent.ask_description(disease)
# print("[DEBUG] description:", description)

# precautions = agent.ask_precautions(disease)
# print("[DEBUG] precautions:", precautions)

# print("[DEBUG] accuracy:", agent.ask_accuracy())