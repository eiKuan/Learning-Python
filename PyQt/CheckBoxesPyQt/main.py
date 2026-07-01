#Tutorial BroCode sobre PyQt - CheckBoxes

import sys

from PyQt5.QtWidgets import (QApplication, QMainWindow, QCheckBox)

from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("CheckBoxes ")
        self.setGeometry(750, 300, 500, 500)
        self.checkbox = QCheckBox("Do you like food?", self)

        self.initUi()

    def initUi(self):
        self.checkbox.setStyleSheet("font-size: 30px;" 
                                    "font-family: Arial;")
        self.checkbox.setGeometry(10, 0, 500, 100)
        self.checkbox.setChecked(False)

        self.checkbox.stateChanged.connect(self.checkboxChanged)

    def checkboxChanged(self, state):
        if state == Qt.Checked:
            print("You like food")
        else:
            print("You don't like food")
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()