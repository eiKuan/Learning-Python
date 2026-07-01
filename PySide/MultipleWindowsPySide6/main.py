# PySide 6 Tutorial - NeuralNine, Multiple Windows

from PySide6.QtWidgets import (QApplication, QMainWindow, QPushButton, QLabel)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Multiple Windows Application")

        button = QPushButton("Open Second Window")
        button.clicked.connect(self.open_window)
        
        self.setCentralWidget(button)

        self.count = 1
        self.windows = []

    def open_window(self):
        w = SecondaryWindow(self.count)
        self.count += 1

        self.windows.append(w)

        w.show()


class SecondaryWindow(QMainWindow):

    def __init__(self, n: int):
        super().__init__()
        self.setWindowTitle(f"Window Number {n}")

        label1 = QLabel(f"Number {n}")

        self.setCentralWidget(label1)


app = QApplication()

window = MainWindow()
window.show()

app.exec()
