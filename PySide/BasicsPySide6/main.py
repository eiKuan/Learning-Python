# PySide 6 Tutorial - NeuralNine

from PySide6.QtWidgets import (QApplication, QMainWindow, QLabel, QWidget, QHBoxLayout,
                               QVBoxLayout, QPushButton, QLineEdit, QTextEdit, QCheckBox, 
                               QSlider, QProgressBar, QComboBox, QListWidget, QRadioButton)
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Hello World Application")

        container = QWidget()
        self.setCentralWidget(container)

        layout = QVBoxLayout(container)

        label1 = QLabel('One')
        label1.setAlignment(Qt.AlignCenter)


        button = QPushButton("Click me")
        button.clicked.connect(lambda: print('Button clicked'))

        list_widgets = QListWidget()
        list_widgets.addItems(("One" , "Two", "Three"))

        list_widgets.itemClicked.connect(lambda item: print(f"Item clicked {item.text()}"))
        list_widgets.itemDoubleClicked.connect(lambda item: print(f"Item double clicked {item.text()}"))

        inner_container = QWidget()

        inner_layout = QHBoxLayout(inner_container)

        checkbox1 = QCheckBox("One")
        checkbox2 = QCheckBox("Two")
        checkbox3 = QCheckBox("Three")

        for c in (checkbox1, checkbox2, checkbox3):
            c.toggled.connect(self.checkbx_Changed)

        inner_layout.addWidget(checkbox1)
        inner_layout.addWidget(checkbox2)
        inner_layout.addWidget(checkbox3)

        layout.addWidget(list_widgets)
        layout.addWidget(button)
        layout.addWidget(label1)
        layout.addWidget(inner_container)

    def checkbx_Changed(self):
        c = self.sender()

        if c.isChecked():
            print("Checkbox was selected! Value: ", c.text())


app = QApplication()

window = MainWindow()
window.show()

app.exec()
