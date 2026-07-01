#Tutorial BroCode sobre PyQt - Css

import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QHBoxLayout,
                             QWidget, QPushButton)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Css with PyQt")
        
        self.button1 = QPushButton("#1")
        self.button2 = QPushButton("#2")
        self.button3 = QPushButton("#3")



        self.initUi()

    def initUi(self):
        centralWidget = QWidget()
        self.setCentralWidget(centralWidget)

        hbox = QHBoxLayout()

        hbox.addWidget(self.button1)
        hbox.addWidget(self.button2)
        hbox.addWidget(self.button3)

        centralWidget.setLayout(hbox)

        self.button1.setObjectName("button1")
        self.button2.setObjectName("button2")
        self.button3.setObjectName("button3")

        self.setStyleSheet("""
            QPushButton{
                font-size: 40px;
                font-family: Arial;
                padding: 15px 75px;
                margin: 25px;
                border: 3px solid;
                border-radius:15px;
            }
                           
            QPushButton#button1{
                background-color: red;
            }
                           
            QPushButton#button2{
                background-color: green;
            }
                           
            QPushButton#button3{
                background-color: yellow;
            }
                           
            QPushButton#button1:hover{
                background-color: pink;
            }
                           
            QPushButton#button2:hover{
                background-color: pink;
            }
                           
            QPushButton#button3:hover{
                background-color: pink;
            }
                           
        """)

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()