#Tutorial BroCode sobre PyQt - Push Buttons

import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QPushButton, 
                             QLabel)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PushButtons")
        self.setGeometry(750, 300, 500, 500)
        self.label = QLabel("Hello", self)
        self.button = QPushButton("Click me", self)

        self.initUi()

    def initUi(self):
        self.button.setGeometry(150, 200, 200, 100)
        self.button.setStyleSheet("font-size: 30px;")
        self.button.clicked.connect(self.onClick) # signal (clicked) -> (Connect) event/action (slot)

        self.label.setGeometry(150, 300, 200, 100)
        self.label.setStyleSheet("font-size: 50px;")

    def onClick(self):
        self.label.setText("Goodbye")

        #print("Button Clicked!")
        #self.button.setText("Clicked")
        #self.button.setDisabled(True)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()