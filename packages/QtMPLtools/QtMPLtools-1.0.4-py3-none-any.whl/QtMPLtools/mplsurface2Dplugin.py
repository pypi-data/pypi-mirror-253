# TODO: CAMPid 0970432108721340872130742130870874321
import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

from PyQt6 import (QtGui, QtDesigner)
from matplotlibwidgets import MPLsurface2D

DOM_XML = """
<ui language="c++"> displayname="2D Surface Plot">
    <widget class="MPLsurface2D" name="surface2dPlot">
        <property name="title">
            <string>2D Surf Plot</string>
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

class MPLsurface2DPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

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
        return MPLsurface2D(parent)

    def name(self):
        return MPLsurface2D.__name__

    def domXml(self):
        return DOM_XML

    def group(self):
        return 'Plots'

    def icon(self):
        imgLocation = os.path.join(CURRENT_DIR, 'figures/surface2D.ico')
        return QtGui.QIcon(imgLocation)

    def toolTip(self):
        return '2D Surface Plot'

    def whatsThis(self):
        return '2D Surface Plot'

    def isContainer(self):
        return False

    def includeFile(self):
        return 'QtMPLtools.matplotlibwidgets'
