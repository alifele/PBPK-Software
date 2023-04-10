import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt
from Ui import Ui_MainWindow
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QAbstractListModel, Qt
import qtmodern.styles
import qtmodern.windows
from PyQt5.QtGui import QPalette


tick = QColor("green")


class TodoModel(QAbstractListModel):
    def __init__(self, *args, todos=None, **kwargs):
        super(TodoModel, self).__init__(*args, **kwargs)
        self.todos = todos or []

    def data(self, index, role):
        if role == Qt.DisplayRole:
            status, text = self.todos[index.row()]
            return text

        if role == Qt.DecorationRole:
            status, _ = self.todos[index.row()]
            if status:
                return tick

    def rowCount(self, index):
        return len(self.todos)





class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.model = TodoModel(todos=[(False, "My first doto"), (False, "Hello")])
        self.todoListView.setModel(self.model)
        self.setFixedSize(337,378)

        self.addPushButton.pressed.connect(self.add)
        self.todoLineEdit.returnPressed.connect(self.add)
        self.deletePushButton.pressed.connect(self.delete)
        self.completePushButton.pressed.connect(self.complete)


    def delete(self):
        indexes = self.todoListView.selectedIndexes()
        if indexes:
            index = indexes[0]
            del self.model.todos[index.row()]
            self.model.layoutChanged.emit()
            self.todoListView.clearSelection()


    def complete(self):
        indexes = self.todoListView.selectedIndexes()
        if indexes:
            index = indexes[0]
            row = index.row()
            status, text = self.model.todos[row]
            self.model.todos[row] = (True, text)
            self.model.layoutChanged.emit()
            self.todoListView.clearSelection()

    def add(self):
        print("New item is added")

        text = self.todoLineEdit.text()
        text = text.strip()

        if text:
            self.model.todos.append((False, text))
            self.model.layoutChanged.emit()
            self.todoLineEdit.clear()







    def submitInformation(self):
        name = self.nameLineEdit.text()
        lastName = self.lastNameLineEdit.text()
        birthday = self.birthDayLineEdit.text()

        txt = name + " " + lastName + " is born on " + birthday


        self.informationTextBrowser.setText(txt)





class Main():
    def __init__(self):

        app = QApplication(sys.argv)
        qtmodern.styles.dark(app)

        window = MainWindow()
        window.show()

        app.exec_()


if __name__ == "__main__":
    main = Main()