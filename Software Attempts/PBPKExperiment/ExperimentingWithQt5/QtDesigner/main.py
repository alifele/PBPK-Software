import sys

from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QAction
from PyQt5.QtGui import QColor, QPalette
from PyQt5.QtCore import Qt
from Ui.myUi import Ui_MainWindow
import qtmodern.styles
import qtmodern.windows
from PyQt5.QtGui import QPalette

import Ui.resources_rc



class Actions:
    def __init__(self, parent):
        self.parent = parent
        print("Hello there ")
        self.parent.submitAction.triggered.connect(self.submit)


    def submit(self):
        print("Hello there ")





class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(650,350)



        self.submitAction.triggered.connect(self.submitInformation)




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