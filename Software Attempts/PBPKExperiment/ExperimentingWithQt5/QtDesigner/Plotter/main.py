import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets as QtW
from PyQt5 import QtCore
from pyqtgraph import PlotWidget, plot
from PyQt5.QtGui import QColor, QPalette
import pyqtgraph as pg
from Ui import Ui_MainWindow
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from plotcanvas import Plotter, QPlotCanvas

matplotlib.use("Qt5Agg")



class PlotCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(800,500)

        self.setupUi(self)
        self.setupComboBox()



    def setupComboBox(self):
        self.plotTypeComboBox.addItem("Sin Plot")
        self.plotTypeComboBox.addItem("Cos Plot")
        self.plotTypeComboBox.addItem("x^2 Plot")
        self.plotTypeComboBox.addItem("sqrt(x) Plot")

        self.plotTypeComboBox.currentTextChanged.connect(self.plotHandler)


    def plotHandler(self, str):
        if str == "Sin Plot":
            self.plotCanvas.plotSin()
            print("plotting sin plot")

        if str == "Cos Plot":
            self.plotCanvas.plotCos()
            print("plotin cos plot")

        if str == "x^2 Plot":
            self.plotCanvas.plotX2()
            









class Main:
    def __init__(self):

        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exec_()




if __name__ == "__main__":
    main = Main()



