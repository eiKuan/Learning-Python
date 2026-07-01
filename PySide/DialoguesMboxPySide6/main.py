# PySide 6 Tutorial - NeuralNine, MessageBoxes & Dialogues

from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QMessageBox)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("MessageBoxes Application")

        button = QPushButton("Show Choices")
        button.clicked.connect(self.ask_choices)
        
   #     button.clicked.connect(self.ask_yes_no)

        self.setCentralWidget(button)

   # def ask_yes_no(self):
   #     if QMessageBox.question(self, "Question", "Do you like Python?") == QMessageBox.Yes:
   #         print("User Likes python")
   #     else:
   #         print("User do not like python")

    def ask_choices(self):
        msg = QMessageBox(self)

        msg.setWindowTitle("Choices")

        msg.setText("Select your favorite programming language")

        python = msg.addButton("Python", QMessageBox.AcceptRole)
        cpp = msg.addButton("C++", QMessageBox.AcceptRole)
        java = msg.addButton("Java", QMessageBox.AcceptRole)

        msg.exec()
        print("User's favorite programming language is: ", msg.clickedButton().text())

app = QApplication()

window = MainWindow()
window.show()

app.exec()
