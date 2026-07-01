#Tutorial BroCode sobre PyQt - Radio Buttons

import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QRadioButton,
                             QButtonGroup)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Radio Buttons")
        self.setGeometry(750, 300, 500, 500)

        self.radioButton1 = QRadioButton("Visa", self)
        self.radioButton2 = QRadioButton("MasterCard", self)
        self.radioButton3 = QRadioButton("Gift Card", self)
        self.radioButton4 = QRadioButton("In-Store", self)
        self.radioButton5 = QRadioButton("Online", self)

        #Agrupando os radioButtons para separa-los
        self.rButtonGroup1 = QButtonGroup(self)
        self.rButtonGroup2 = QButtonGroup(self)

        self.initUi()

    def initUi(self):
        self.radioButton1.setGeometry(0, 0, 300, 50)
        self.radioButton2.setGeometry(0, 50, 300, 50)
        self.radioButton3.setGeometry(0, 100, 300, 50)
        self.radioButton4.setGeometry(0, 200, 300, 50)
        self.radioButton5.setGeometry(0, 250, 300, 50)

        self.setStyleSheet("QRadioButton {"
                           "font-size: 30px;"
                           "font-family: Arial;"
                           "padding: 10px;"
                           "}")
        
        self.rButtonGroup1.addButton(self.radioButton1)
        self.rButtonGroup1.addButton(self.radioButton2)
        self.rButtonGroup1.addButton(self.radioButton3)

        self.rButtonGroup2.addButton(self.radioButton4)
        self.rButtonGroup2.addButton(self.radioButton5)

        self.radioButton1.toggled.connect(self.radioButtonChanged)
        self.radioButton2.toggled.connect(self.radioButtonChanged)
        self.radioButton3.toggled.connect(self.radioButtonChanged)
        self.radioButton4.toggled.connect(self.radioButtonChanged)
        self.radioButton5.toggled.connect(self.radioButtonChanged)

    def radioButtonChanged(self):
        radioButton = self.sender() #retorna o widget que ativou o metodo

        if radioButton.isChecked():
            print(f"{radioButton.text()} is selected ")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()