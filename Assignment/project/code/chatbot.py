
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
  from ai_mock import get_possible_disease_with_symptoms, \
    get_possible_symptoms_of_disease, \
    get_symptoms_from_text, \
    get_duration_from_text, \
    get_symptoms_severity_duration_from_text


# def mock_get_user_input():
#     pass


def get_user_input():
    # read input from terminal
    user_input = input("Patient: ")
    return user_input




class mDoctorBot():
    def __init__(self):
        
        self.symptoms = []
        self.symptoms_severity = []
        self.symptoms_duration = []

        self.possible_disease = []
        
        self.history_text = []
        
        self.next_state = 0

    def state_0(self):
        # greeting
        self.state = 0
        print("Doctor: Good morning, how can I help you today?")
        self.next_state = 1

    def state_1(self):
        # get as much information as possible from the first input
        self.state = 1
        input_text = get_user_input()
        self.history_text.append(input_text)
        self.symptoms, self.symptoms_severity, self.symptoms_duration = \
          get_symptoms_severity_duration_from_text(self.history_text, input_text)
        if self.symptoms == []:
            self.next_state = 2
            return
        
        if self.symptoms_duration == []:
            print("Doctor: I see. How long have you been feeling this way?")
            self.next_state = 3
            return
        
        self.next_state = 5
     
    def state_2(self):
        self.state = 2
        print("Doctor: Sorry, I didn't catch that. Can you tell me about your symptoms?")
        print("Dotcor: Like fever, vomiting, etc.")
        self.next_state = 1
        
    def state_3(self):
        # get duration
        self.state = 3
        input_text = get_user_input()
        self.history_text.append(input_text)
        self.symptoms_duration = get_duration_from_text(input_text)
        print("[DEBUG] self.symptoms_duration: ", self.symptoms_duration)
        if self.symptoms_duration == []:
            self.next_state = 4
            return
        
        self.next_state = 5
        
    def state_4(self):
        self.state = 4
        print("Doctor: Sorry, I didn't catch that. Can you tell me about how long you've been feeling this way?")
        self.next_state = 3

    def state_5(self):
        # get possible disease and check if need to ask more
        self.state = 5
        
        self.possible_disease = get_possible_disease_with_symptoms(self.symptoms)
        print("[DEBUG] self.possible_disease: ", self.possible_disease)
        if self.possible_disease == []:
            print("Doctor: Have you been experiencing any other symptoms, like fever or vomiting?")
            self.next_state = 6
            return
        
        # check the possible disease:
        # if there are more than one possible disease
        if self.possible_disease[0][1] < 0.5:
            print("Doctor: Great, I have some ideas, but I need to ask you a few more questions to be sure.")
            self.next_state = 7
            return
        # todo
 
    def state_6(self):
        self.state = 6
        input_text = get_user_input()
        self.history_text.append(input_text)
        new_symptoms = get_symptoms_from_text(input_text)
        if new_symptoms == []:
            self.next_state = 7
            return
        
        self.next_state = 5

    def state_7(self):
        self.state = 7
        print("Doctor: Sorry, I didn't catch that. Can you tell me about any other symptoms you might be experiencing?")
        self.next_state = 6

    def run(self):
        while(self.next_state!=None):
          eval("self.state_"+str(self.next_state) + "()")


if __name__ == "__main__":
    bot = mDoctorBot()
    bot.run()
    print("Goodbye!")