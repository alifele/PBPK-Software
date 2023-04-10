# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from plotcanvas import QPlotCanvas



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(781, 401)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.plotCanvas = QPlotCanvas(self.centralwidget)
        self.plotCanvas.setGeometry(QtCore.QRect(380, 20, 381, 301))
        self.plotCanvas.setObjectName("plotCanvas")
        self.plotTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.plotTypeLabel.setGeometry(QtCore.QRect(30, 40, 62, 17))
        self.plotTypeLabel.setObjectName("plotTypeLabel")
        self.plotTypeComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.plotTypeComboBox.setGeometry(QtCore.QRect(110, 40, 221, 25))
        self.plotTypeComboBox.setObjectName("plotTypeComboBox")
        self.plotPushButton = QtWidgets.QPushButton(self.centralwidget)
        self.plotPushButton.setGeometry(QtCore.QRect(40, 90, 131, 25))
        self.plotPushButton.setObjectName("plotPushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 781, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # MainWindow.setCentralWidget(self.plotCanvas)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.plotTypeLabel.setText(_translate("MainWindow", "TextLabel"))
        self.plotPushButton.setText(_translate("MainWindow", "PushButton"))

