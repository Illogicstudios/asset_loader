import os
from functools import partial

import sys

from pymel.core import *
import maya.OpenMayaUI as omui

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

from PySide2.QtWidgets import *

from shiboken2 import wrapInstance

import utils

from Prefs import *

import maya.OpenMaya as OpenMaya

# ######################################################################################################################

# TODO Change the prefs name for this project
_FILE_NAME_PREFS = "maya_tool"

# ######################################################################################################################

# TODO change class name
class MayaTool(QtWidgets.QDialog):

    def __init__(self, prnt=wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)):
        # TODO change class name
        super(MayaTool, self).__init__(prnt)

        # Common Preferences (common preferences on all tools)
        self.__common_prefs = Prefs()
        # Preferences for this tool
        self.__prefs = Prefs(_FILE_NAME_PREFS)

        # Model attributes

        # UI attributes
        self.__reinit_ui()

        # name the window
        # TODO change window name
        self.setWindowTitle("Maya Tool")
        # make the window a "tool" in Maya's eyes so that it stays on top when you click off
        self.setWindowFlags(QtCore.Qt.Tool)
        # Makes the object get deleted from memory, not just hidden, when it is closed.
        self.setAttribute(QtCore.Qt.WA_DeleteOnClose)

        # Create the layout, linking it to actions and refresh the display
        self.__create_ui()
        self.__refresh_ui()
        self.__create_callback()

    # Create callbacks
    def __create_callback(self):
        pass
        # self.__selection_callback = \
        #     OpenMaya.MEventMessage.addEventCallback("SelectionChanged", self.on_selection_changed)

    # Remove callbacks
    def closeEvent(self, arg__1: QtGui.QCloseEvent) -> None:
        pass
        # OpenMaya.MMessage.removeCallback(self.__selection_callback)

    # initialize the ui
    def __reinit_ui(self):
        self.__ui_width = 500
        self.__ui_height = 300
        self.__ui_min_width = 300
        self.__ui_min_height = 200

    # Create the ui
    def __create_ui(self):
        # Reinit attributes of the UI
        self.__reinit_ui()
        self.setMinimumSize(self.__ui_min_width, self.__ui_min_height)
        self.resize(self.__ui_width, self.__ui_height)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

        # Some aesthetic value
        size_btn = QtCore.QSize(180, 30)

        # asset_path = os.path.dirname(__file__) + "/assets/asset.png"

        # Main Layout
        main_lyt = QtWidgets.QVBoxLayout()
        main_lyt.setContentsMargins(10, 15, 10, 15)
        main_lyt.setSpacing(12)
        self.setLayout(main_lyt)


    # Refresh the ui according to the model attribute
    def __refresh_ui(self):
        # TODO refresh the UI according to model attributes
        pass
