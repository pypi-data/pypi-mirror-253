# TODO: CAMPid 0970432108721340872130742130870874321
import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

from PyQt6 import (QtGui, QtDesigner)
from matplotlibwidgets import MPLrect

DOM_XML = """
<ui language="c++"> displayname="Rect Plot">
    <widget class="MPLrect" name="rectPlot">
        <property name="title">
            <string>Rect Plot</string>
        </property>
        <property name="xlabel">
            <string>X</string>
        </property>
        <property name="ylabel">
            <string>Y</string>
        </property>
    </widget>
</ui>
"""

class MPLrectPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

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
        return MPLrect(parent)

    def name(self):
        return MPLrect.__name__

    def domXml(self):
        return DOM_XML

    def group(self):
        return 'Plots'

    def icon(self):
        imgLocation = os.path.join(CURRENT_DIR, 'figures/rect.ico')
        return QtGui.QIcon(imgLocation)

    def toolTip(self):
        return 'Rectangular Plot'

    def whatsThis(self):
        return 'Rectangular Plot'

    def isContainer(self):
        return False

    def includeFile(self):
        return 'QtMPLtools.matplotlibwidgets'
