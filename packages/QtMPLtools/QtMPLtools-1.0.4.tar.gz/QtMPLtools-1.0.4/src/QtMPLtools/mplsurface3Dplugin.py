# TODO: CAMPid 0970432108721340872130742130870874321
import os
CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

from PyQt6 import (QtGui, QtDesigner)
from matplotlibwidgets import MPLsurface3D

DOM_XML = """
<ui language="c++"> displayname="3D Surface Plot">
    <widget class="MPLsurface3D" name="surface3dPlot">
        <property name="title">
            <string>3D Surf Plot</string>
        </property>
        <property name="xlabel">
            <string>X</string>
        </property>
        <property name="ylabel">
            <string>Y</string>
        </property>
        <property name="zlabel">
            <string>Z</string>
        </property>
    </widget>
</ui>
"""

class MPLsurface3DPlugin(QtDesigner.QPyDesignerCustomWidgetPlugin):

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
        return MPLsurface3D(parent)

    def name(self):
        return MPLsurface3D.__name__

    def domXml(self):
        return DOM_XML

    def group(self):
        return 'Plots'

    def icon(self):
        imgLocation = os.path.join(CURRENT_DIR, 'figures/surface3D.ico')
        return QtGui.QIcon(imgLocation)

    def toolTip(self):
        return '3D Surface Plot'

    def whatsThis(self):
        return '3D Surface Plot'

    def isContainer(self):
        return False

    def includeFile(self):
        return 'QtMPLtools.matplotlibwidgets'
