import sys

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtWidgets as QtW
from PyQt5 import QtCore
from pyqtgraph import PlotWidget, plot
from PyQt5.QtGui import QColor, QPalette
import pyqtgraph as pg
from UI import Ui_MainWindow
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg

import qtmodern.styles
import qtmodern.windows



matplotlib.use("Qt5Agg")


class PlotCanvas(FigureCanvasQTAgg):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = plt.figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(1106, 872)

        self.setupUi(self)




class Main:
    def __init__(self):
        app = QApplication(sys.argv)
        window = MainWindow()
        qtmodern.styles.dark(app)

        window.show()
        app.exec_()


if __name__ == "__main__":
    main = Main()



