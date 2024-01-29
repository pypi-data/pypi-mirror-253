from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as Canvas
from matplotlib.figure import Figure
from matplotlib import rcParams
import numpy as np

from qtpy.QtCore import Property

rcParams['font.size'] = 9

class MPLrect(Canvas):
    def __init__(self, parent, title='', xscale='linear', yscale='linear',
                 width=4.3, height=3.6, dpi=100):
        self._title  = 'Rect Plot'
        self._xlabel = 'X'
        self._ylabel = 'Y'

        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.figure.add_subplot(111)
        self.axes.set_title(self._title)
        self.axes.set_xlabel(self._xlabel)
        self.axes.set_ylabel(self._ylabel)
        if xscale is not None:
            self.axes.set_xscale(xscale)
        if yscale is not None:
            self.axes.set_yscale(yscale)

        super().__init__(self.figure)
        self.setParent(parent)

    def getTitle(self):
        return self._title
    def getXlabel(self):
        return self._xlabel
    def getYlabel(self):
        return self._ylabel

    def setTitle(self, new_title):
        self._title = new_title
        self.axes.set_title(self._title)
        self.draw()
    def setXlabel(self, new_xlabel):
        self._xlabel = new_xlabel
        self.axes.set_xlabel(self._xlabel)
        self.draw()
    def setYlabel(self, new_ylabel):
        self._ylabel = new_ylabel
        self.axes.set_ylabel(self._ylabel)
        self.draw()


    title  = Property(str, getTitle, setTitle)
    xlabel = Property(str, getXlabel, setXlabel)
    ylabel = Property(str, getYlabel, setYlabel)

class MPLpolar(Canvas):
    def __init__(self, parent, width=3, height=3.3, dpi=100):
        self._title = 'Polar Plot'
        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.figure.add_subplot(111, projection='polar')
        self.axes.set_title(self._title)

        super().__init__(self.figure)
        self.setParent(parent)

    def getTitle(self):
        return self._title

    def setTitle(self, new_title):
        self._title = new_title

        self.axes.set_title(self._title)
        self.draw()

    title = Property(str, getTitle, setTitle)

class MPLsurface2D(Canvas):
    def __init__(self, parent, width=4.3, height=3.6, dpi=100):
        self._title = '2D Surf Plot'
        self._xlabel = 'X'
        self._ylabel = 'Y'

        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.figure.add_subplot(111)

        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)
        X, Y = np.meshgrid(X, Y)
        Z = np.ones((X.shape[0],X.shape[1]))

        self.axes.set_title(self._title)
        self.axes.set_xlabel(self._xlabel)
        self.axes.set_ylabel(self._ylabel)

        self.axes.pcolormesh(X, Y, Z, vmin=0, vmax=2)

        super().__init__(self.figure)
        self.setParent(parent)

    def getTitle(self):
        return self._title
    def getXlabel(self):
        return self._xlabel
    def getYlabel(self):
        return self._ylabel

    def setTitle(self, new_title):
        self._title = new_title
        self.axes.set_title(self._title)
        self.draw()
    def setXlabel(self, new_xlabel):
        self._xlabel = new_xlabel
        self.axes.set_xlabel(self._xlabel)
        self.draw()
    def setYlabel(self, new_ylabel):
        self._ylabel = new_ylabel
        self.axes.set_ylabel(self._ylabel)
        self.draw()


    title  = Property(str, getTitle, setTitle)
    xlabel = Property(str, getXlabel, setXlabel)
    ylabel = Property(str, getYlabel, setYlabel)

class MPLsurface3D(Canvas):
    def __init__(self, parent, width=3.5, height=3, dpi=100):
        self._title = '3D Surf Plot'
        self._xlabel = 'X'
        self._ylabel = 'Y'
        self._zlabel = 'Z'

        self.figure = Figure(figsize=(width, height), dpi=dpi)
        self.axes = self.figure.add_subplot(111, projection='3d')

        X = np.arange(-5, 5, 0.25)
        Y = np.arange(-5, 5, 0.25)
        X, Y = np.meshgrid(X, Y)

        Z = np.empty((X.shape[0],X.shape[1]))
        Z[:] = np.nan

        self.axes.set_title(self._title)
        self.axes.set_xlabel(self._xlabel)
        self.axes.set_ylabel(self._ylabel)
        self.axes.set_zlabel(self._zlabel)

        self.axes.plot_surface(X, Y, Z)

        super().__init__(self.figure)
        self.setParent(parent)

    def getTitle(self):
        return self._title

    def getXlabel(self):
        return self._xlabel

    def getYlabel(self):
        return self._ylabel

    def getZlabel(self):
        return self._zlabel

    def setTitle(self, new_title):
        self._title = new_title
        self.axes.set_title(self._title)
        self.draw()

    def setXlabel(self, new_xlabel):
        self._xlabel = new_xlabel
        self.axes.set_xlabel(self._xlabel)
        self.draw()

    def setYlabel(self, new_ylabel):
        self._ylabel = new_ylabel
        self.axes.set_ylabel(self._ylabel)
        self.draw()

    def setZlabel(self, new_zlabel):
        self._zlabel = new_zlabel
        self.axes.set_zlabel(self._zlabel)
        self.draw()

    title = Property(str, getTitle, setTitle)
    xlabel = Property(str, getXlabel, setXlabel)
    ylabel = Property(str, getYlabel, setYlabel)
    zlabel = Property(str, getZlabel, setZlabel)
