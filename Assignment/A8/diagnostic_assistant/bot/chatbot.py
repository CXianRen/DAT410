
# the dialoge in most case will like this:
"""
# greeting start
(1) Doctor: Good morning, how can I help you today?
# Key information: symptoms
(2) Patient: Hi, I've been feeling dizzy and nauseous lately. I'm also experiencing some headaches.
# Key questions: duration
(3) Doctor: I see. How long have you been feeling this way?
# Key information: duration
(4) Patient: It's been about a week now. It comes and goes, but it's been pretty persistent.
# Key questions: other symptoms, based on the previous symptoms
(5) Doctor: Have you been experiencing any other symptoms, like fever or vomiting?
# Key information: other symptoms
(6) Patient: No fever, but I have vomited a couple of times.
# It is important to ask about the patient's medical history and any recent changes in their lifestyle or diet. 
# but in our system, and dataset, it is not available yet.
(7) Doctor: Alright, I'd like to do a few tests to get a better idea of what might be going on. We'll start with some blood tests and possibly a CT scan to rule out any serious issues.
# invalid response
(8) Patient: Okay, sounds good.
# Key information: what to do next
(9) Doctor: In the meantime, try to stay hydrated and get plenty of rest. We'll figure this out together.
# greeting
(10) Patient: Thank you, doctor.
# greeting
(11) Doctor: You're welcome. I'll have my nurse set up the tests for you. We'll go from there.
"""
Test = True

if Test:
  # import the mock functions
  import sys
  sys.path.append('.')
  from model.ai_mock import \
    get_possible_disease_with_symptoms, \
    get_possible_symptoms_of_disease, \
    get_symptoms_from_text, \
    get_duration_from_text, \
    get_symptoms_severity_duration_from_text, \
    get_yes_or_not

import os
import json
import random

class mDoctorBot():
    def __init__(self, pattern_path = \
            os.path.join(os.path.dirname(
                os.path.abspath(__file__)),
                "patterns.json")):
        self.symptoms = []
        self.symptoms_severity = []
        self.symptoms_duration = []
        self.possible_disease = []
        self.rejected_symptoms = []
        self.history_text = []
        self.input_text = None
        self.output_text = None
        self.next_state = 0
    
        with open(pattern_path, "r") as f:
            self.pattern_list = json.load(f)

    def __mprint(self, msg):
      self.history_text.append(msg)
      self.output_text = msg
      
    def state_0(self):
        # greeting
        self.state = 0
        self.__mprint(random.choice(self.pattern_list["state_0_1"]))
        self.next_state = 1

    def state_1(self):
        # get as much information as possible from the first input
        self.state = 1
        input_text = self.input_text
        self.history_text.append(input_text)
        self.symptoms, self.symptoms_severity, self.symptoms_duration = \
          get_symptoms_severity_duration_from_text(self.history_text, input_text)
        if self.symptoms == []:
            self.next_state = 2
            return
        
        if self.symptoms_duration == []:
            self.__mprint(random.choice(self.pattern_list["state_1_1"]))
            self.next_state = 3
            return
        
        self.next_state = 5
     
    def state_2(self):
        self.state = 2
        self.__mprint(random.choice(self.pattern_list["state_2_1"]))
        self.next_state = 1
        
    def state_3(self):
        # get duration
        self.state = 3
        input_text = self.input_text
        self.history_text.append(input_text)
        self.symptoms_duration = get_duration_from_text(input_text)
        print("\t\t\t\t[DEBUG] self.symptoms_duration: ", self.symptoms_duration)
        if self.symptoms_duration == []:
            self.next_state = 4
            return
        
        self.next_state = 5
        
    def state_4(self):
        self.state = 4
        self.__mprint(random.choice(self.pattern_list["state_4_1"]))
        self.next_state = 3

    def state_5(self):
        # get possible disease and check if need to ask more
        self.state = 5
        
        self.possible_disease = get_possible_disease_with_symptoms(self.symptoms)
        print("\t\t\t\t[DEBUG] self.possible_disease: ", self.possible_disease)
        if self.possible_disease == []:
            self.__mprint("Doctor: "+ random.choice(self.pattern_list["state_5_1"]))
            self.next_state = 6
            return
        
        # check the possible disease:
        # if there are more than one possible disease
        if self.possible_disease[0][1] < 0.5:
            self.__mprint("Doctor: " + random.choice(self.pattern_list["state_5_2"]))
            self.next_state = 8
            return
        
        self.next_state = None
        # check 

    def state_6(self):
        self.state = 6
        input_text = self.input_text
        self.history_text.append(input_text)
        new_symptoms = get_symptoms_from_text(input_text)
        if new_symptoms == []:
            self.next_state = 7
            return
        self.symptoms.append(new_symptoms)
        self.next_state = 5

    def state_7(self):
        self.state = 7
        self.__mprint(random.choice(self.pattern_list["state_7_1"]))
        self.next_state = 6

    def state_8(self):
        self.state = 8 
        if len(self.symptoms) + len(self.rejected_symptoms)> 5:
            # get the conclusion
          self.next_state = None

        symptoms_of_disease = get_possible_symptoms_of_disease(self.possible_disease[0][0])
        symptom_to_ask = None
        for s in symptoms_of_disease:
            if s not in self.symptoms and s not in self.rejected_symptoms:
                symptom_to_ask = s
                break
        
        print("\t\t\t\t[DEBUG] symptoms_of_disease: ", symptoms_of_disease)
        print("\t\t\t\t[DEBUG] self.symptoms: ", self.symptoms)
        print("\t\t\t\t[DEBUG] self.rejected_symptoms: ", self.rejected_symptoms)
        print("\t\t\t\t[DEBUG] symptom_to_ask: ", symptom_to_ask)
      
        if self.possible_disease[0][1]<0.5 and symptom_to_ask is not None:
        # ask more question to improve the score  if possible
            self.__mprint("%s %s" %(random.choice(self.pattern_list["state_8_1"]), symptom_to_ask))
            while True:
                input_text = self.input_text
                self.history_text.append(input_text)
                if get_yes_or_not(input_text):
                    self.symptoms.append(symptom_to_ask)
                    break
                else:
                    self.rejected_symptoms.append(symptom_to_ask)
                    break
            # check again  
            self.next_state = 8
            return
        self.next_state = 9

    def state_9(self):
        self.state = 9
        self.__mprint("%s %s" % ((random.choice(self.pattern_list["conclusion"]), self.possible_disease)))
        self.next_state = None

    # def run(self):
    #     while(self.next_state!=None):
    #       eval("self.state_"+str(self.next_state) + "()")

    def get_response(self, input):
        # clear history output
        self.output_text = None
        self.input_text = input
        while self.output_text is None and self.next_state is not None:
            eval("self.state_"+str(self.next_state) + "()")
        return self.output_text


if __name__ == "__main__":
    bot = mDoctorBot()
    # trigger the state_0
    print("Doctor: ", bot.get_response(""))
    while True:
        input_text = input("You: ")
        print("Doctor: ", bot.get_response(input_text))
        if bot.next_state == None:
            break