# TODO: CAMPid 0970432108721340872130742130870874321
import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

from PyQt6 import (QtGui, QtDesigner)
from matplotlibwidgets import MPLpolar

DOM_XML = """
<ui language="c++"> displayname="Polar Plot">
    <widget class="MPLpolar" name="polarPlot">
        <property name="title">
            <string>Polar Plot</string>
        </property>
    </widget>
</ui>
"""

class MPLpolarPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.initialized = False

    def initialize(self, core):
        if self.initialized:
            return

        self.initialized = True

    def isInitialized(self):
        return self.initialized

    def createWidget(self, parent):
        return MPLpolar(parent)

    def name(self):
        return MPLpolar.__name__

    def domXml(self):
        return DOM_XML

    def group(self):
        return 'Plots'

    def icon(self):
        imgLocation = os.path.join(CURRENT_DIR, 'figures/polar.ico')
        return QtGui.QIcon(imgLocation)

    def toolTip(self):
        return 'Polar Plot'

    def whatsThis(self):
        return 'Polar Plot'

    def isContainer(self):
        return False

    def includeFile(self):
        return 'QtMPLtools.matplotlibwidgets'
