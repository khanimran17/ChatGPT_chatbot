import sys
from backend import ChatBot
from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication
import threading

class ChatBotGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = ChatBot()

        self.setMinimumSize(700, 500)

        # Chat area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 670, 400)
        self.chat_area.setReadOnly(True)

        # input area
        self.input_area = QLineEdit(self)
        self.input_area.setGeometry(10, 430, 550, 40)
        self.input_area.returnPressed.connect(self.send_message())

        # button
        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(580, 430, 100, 40)
        self.send_button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_area.text().strip()
        self.chat_area.append(f"<p style='color:#33333'>Me: {user_input}</p>")
        self.input_area.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()

    def get_bot_response(self, user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#33333; background-color:#E9E9E9'>Bot: {response}</p>")


app = QApplication(sys.argv)
chatbot_gui = ChatBotGUI()
sys.exit(app.exec())
