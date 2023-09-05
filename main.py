import sys

from PyQt6.QtWidgets import QMainWindow, QTextEdit, QLineEdit, QPushButton, QApplication


class ChatBotGUI(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(700, 500)

        # Chat area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10, 10, 670, 400)
        self.chat_area.setReadOnly(True)

        # input area
        self.input_area = QLineEdit(self)
        self.input_area.setGeometry(10, 430, 550, 40)

        # button
        self.send_button = QPushButton("Send", self)
        self.send_button.setGeometry(580, 430, 100, 40)

        self.show()


app = QApplication(sys.argv)
chatbot_gui = ChatBotGUI()
sys.exit(app.exec())
