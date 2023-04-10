import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from PyQt5 import QtWidgets
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar


class Plotter(FigureCanvasQTAgg):
    def __init__(self):
        fig = plt.figure()
        self.axes = fig.add_subplot(111)
        super().__init__(fig)


class QPlotCanvas(QtWidgets.QWidget):
    def __init__(self, parent):
        super().__init__(parent)
        self.parent = parent
        self.plotter = Plotter()
        self.tList = np.arange(0,10,0.1)
        self.yList = np.sin(self.tList)
        self.plotSin()

        self.update()

    def plotSin(self):
        self.plotter.axes.cla()
        self.plotter.axes.plot(self.tList, np.sin(self.tList))
        self.plotter.draw()
        # self.update()

    def plotCos(self):
        self.plotter.axes.cla()
        self.plotter.axes.plot(self.tList, np.cos(self.tList))
        self.plotter.draw()
        # self.update()

    def plotX2(self):
        self.plotter.axes.cla()
        self.plotter.axes.plot(self.tList, self.tList**2)
        self.plotter.draw()

    def update(self):
        toolbar = NavigationToolbar(self.plotter, self)
        layout = QtWidgets.QVBoxLayout(self.parent)
        layout.addWidget(toolbar)
        layout.addWidget(self.plotter)
        self.setLayout(layout)


