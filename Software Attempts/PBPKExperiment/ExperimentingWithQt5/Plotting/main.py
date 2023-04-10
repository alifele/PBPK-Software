import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets as QtW
from PyQt5 import QtCore
from pyqtgraph import PlotWidget, plot
from PyQt5.QtGui import QColor, QPalette
import pyqtgraph as pg
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


matplotlib.use("Qt5Agg")



class PlotCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setFixedSize(800,500)

        canvasWidget = PlotCanvas(self)


        tList = np.arange(0,10,0.1)
        yList = np.sin(tList)
        canvasWidget.axes.plot(tList, yList)

        toolbar = NavigationToolbar(canvasWidget, self)

        layout = QtW.QVBoxLayout()
        layout.addWidget(toolbar)
        layout.addWidget(canvasWidget)

        dummyWdiget = QtW.QWidget()
        dummyWdiget.setLayout(layout)

        self.setCentralWidget(dummyWdiget)







class Main:
    def __init__(self):

        app = QApplication(sys.argv)
        window = MainWindow()
        window.show()
        app.exec_()




if __name__ == "__main__":
    main = Main()



