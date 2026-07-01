#Task Planner Code First with Hala Tutorial

from PyQt5.QtWidgets import (QWidget, QApplication, QListWidgetItem, QMessageBox)

from PyQt5.uic import loadUi

from PyQt5 import QtCore

import sys

import sqlite3


class Window(QWidget):
    def __init__(self):
        super(Window, self).__init__()
        loadUi("main.ui", self)
        self.setWindowTitle("Daily Task Planner")
        self.calendarWidget.selectionChanged.connect(self.calendarDateChanged)
        self.calendarDateChanged()
        self.saveButton.clicked.connect(self.saveChanges)
        self.addButton.clicked.connect(self.addNewTask)


    def calendarDateChanged(self):
        print("The Calendar Date Was Changed")
        dateSelected = self.calendarWidget.selectedDate().toPyDate()
        print("Date selected: ", dateSelected)
        self.updateTaskList(dateSelected)

    def updateTaskList(self, date):

        self.taskListWidget.clear()

        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        query = "SELECT task, completed FROM tasks WHERE date = ?"

        row = (date,)

        results = cursor.execute(query, row).fetchall()

        for result in results:
            # add to the list widget
            item = QListWidgetItem(str(result[0]))
            item.setFlags(item.flags() | QtCore.Qt.ItemIsUserCheckable)
            item.setCheckState(QtCore.Qt.Unchecked)
            if result[1] == "YES":
                item.setCheckState(QtCore.Qt.Checked)
            else:
                item.setCheckState(QtCore.Qt.Unchecked)

            self.taskListWidget.addItem(item)

    def saveChanges(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()

        date = self.calendarWidget.selectedDate().toPyDate()

        for i in range(self.taskListWidget.count()):
            item = self.taskListWidget.item(i)
            task = item.text()
            if item.checkState() == QtCore.Qt.Checked:
                query = "UPDATE tasks SET completed = 'YES' WHERE task = ? AND date = ?"
            else:
                query = "UPDATE tasks SET completed = 'NO' WHERE task = ? AND date = ?"
            row = (task, date,)

            cursor.execute(query, row)
        db.commit()

        messageBox = QMessageBox()
        messageBox.setWindowTitle("Daily Task Planner")
        messageBox.setText("Changed saved.")

        messageBox.setStandardButtons(QMessageBox.Ok)

        messageBox.exec()

    def addNewTask(self):
        db = sqlite3.connect("data.db")
        cursor = db.cursor()


        newTask = str(self.textLineEdit.text())

        date = self.calendarWidget.selectedDate().toPyDate()

        query = "INSERT INTO tasks(task, completed, date) VALUES (?, ?, ?)"
        row = (newTask, "NO", date,)

        cursor.execute(query, row)
        db.commit()

        self.updateTaskList(date)

        self.textLineEdit.clear()

def main():
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()