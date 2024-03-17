import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLineEdit, QPushButton, QGroupBox
)
from PyQt5.QtGui import QFont
from diagnostic_assistant.base.agent import DiagnosticAgent


class ChatBot:
    def get_response(self, input_text):
        return "Test"


class ChatBotGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Diagnostic Assistant')
        self.chatbot = ChatBot()
        self.initUI()

    def initUI(self):
        self.chat_display = QTextEdit()
        self.chat_display.setFont(QFont("Arial", 10))
        self.chat_display.setReadOnly(True)

        self.input_field = QLineEdit()
        self.input_field.setFont(QFont("Arial", 12))
        self.input_field.setMinimumHeight(50)
        self.send_button = QPushButton('Send')
        self.send_button.clicked.connect(self.send_message)

        input_layout = QHBoxLayout()
        input_layout.addWidget(self.input_field)
        input_layout.addWidget(self.send_button)

        self.graph_box = QGroupBox('Details')
        self.graph_box.setFont(QFont("Arial", 10))
        self.graph_label = QTextEdit()
        self.graph_label.setFont(QFont("Arial", 10))
        self.graph_label.setReadOnly(True)
        self.graph_box_layout = QVBoxLayout()
        self.graph_box_layout.addWidget(self.graph_label)
        self.graph_box.setLayout(self.graph_box_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.chat_display)
        main_layout.addLayout(input_layout)
        main_layout.addWidget(self.graph_box)

        self.setLayout(main_layout)
        self.setGeometry(100, 100, 800, 600)

    def send_message(self):
        user_input = self.input_field.text()
        self.input_field.clear()

        self.chat_display.append(f'You: {user_input}')

        diagnosis_start = True
        symptoms = user_input.split(",")
        if diagnosis_start:
            agent = DiagnosticAgent()

            matching_symptoms = agent.ask_matching_symptoms(symptoms)
            disease = agent.ask_disease(symptoms)

            # diabetes symptoms = fatigue, weight_loss, restlessness, lethargy, irregular_sugar_level, blurred_and_distorted_vision, obesity, excessive_hunger, increased_appetite, polyuria

            if len(matching_symptoms) == 0:
                self.chat_display.append(
                    f'Bot: Did you mean you have {" and ".join(symptoms)}.'
                    f' Sorry we have not found any symptoms like {" and ".join(symptoms)} in the database. '
                    f'Please provide more details')
                return

            detail_diseases = ['Diabetes', 'Heart attack']
            if disease in detail_diseases:
                self.chat_display.append(f'Bot: We might think that you are having {disease}. But, I would like to ask more question from you to confirm it. ?')
                parameters = None
                if disease == 'Diabetes':
                    question_lst = ['What is your Age.?', 'How many pregnancies you had.?', 'What is the Glucose value in the report.?', 'What is the BloodPressure.?', 'What is the SkinThickness parameter in the report.?',
                                    'What is the Insulin level.?',	'What is BMI valule.?',	'What is DiabetesPedigreeFunction value in the report.?']

                    # parameters = [0] * 8

                    diabetes_patient_params = [50, 6, 148, 72, 35, 0, 33.6, 0.627]
                    parameters = diabetes_patient_params  # Test data
                    for idx,q in enumerate(question_lst):
                        self.chat_display.append(f'Bot: {q}')

                        # TODO get input from user
                        #resp = self.input_field.text()
                        self.chat_display.append(f'You: {parameters[idx]}')
                        #parameters[idx] = resp


                    confirmed = agent.ask_disease_confirmation(parameters)

            if confirmed:
                self.chat_display.append(
                    f'Bot: Did you mean you have {" and ".join(matching_symptoms)}.'
                    f' If so, it is highly probable that you have {" or ".join(disease)}'
                )
            else:
                self.chat_display.append(
                    f'Bot: Did you mean you have {" and ".join(matching_symptoms)}.'
                    f' If so, you might have {" or ".join(disease)}'
                )


            description = agent.ask_description(disease)
            self.chat_display.append(f'Bot: Details of disease are, {description}')

            precautions = agent.ask_precautions(disease)
            self.chat_display.append(f'Bot: You can take precautions like {precautions}')

            self.graph_label.append(agent.ask_accuracy())


def main():
    app = QApplication(sys.argv)
    window = ChatBotGUI()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
