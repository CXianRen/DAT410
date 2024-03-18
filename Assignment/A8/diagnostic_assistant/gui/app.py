import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QTextEdit, QLineEdit, QPushButton, QGroupBox
)
from PyQt5.QtGui import QFont
from diagnostic_assistant.base.agent import DiagnosticAgent
from diagnostic_assistant.bot.chatbot import mDoctorBot


class ChatBotGUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Diagnostic Assistant')
        self.chatbot = mDoctorBot()
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
            print("[DEBUG] matching_symptoms:", matching_symptoms) 
            disease = agent.ask_disease(symptoms)
            print("[DEBUG] disease:", disease)

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
