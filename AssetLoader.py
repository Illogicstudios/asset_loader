import os
from functools import partial

import sys

from pymel.core import *
import maya.OpenMayaUI as omui

from PySide2 import QtCore
from PySide2 import QtGui
from PySide2 import QtWidgets

from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

from shiboken2 import wrapInstance

import utils

from Prefs import *

import maya.OpenMaya as OpenMaya

# ######################################################################################################################

_FILE_NAME_PREFS = "asset_loader"


# ######################################################################################################################

class AssetLoader(QtWidgets.QDialog):

    def __init__(self, prnt=wrapInstance(int(omui.MQtUtil.mainWindow()), QtWidgets.QWidget)):
        super(AssetLoader, self).__init__(prnt)


        # Common Preferences (common preferences on all tools)
        self.__common_prefs = Prefs()
        # Preferences for this tool
        self.__prefs = Prefs(_FILE_NAME_PREFS)

        # Model attributes

        # UI attributes
        self.__reinit_ui()

        # name the window
        self.setWindowTitle("Asset Loader")
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
        self.__ui_width = 800
        self.__ui_height = 500
        self.__ui_min_width = 550
        self.__ui_min_height = 300

    # Create the ui
    def __create_ui(self):
        # Reinit attributes of the UI
        self.__reinit_ui()
        self.setMinimumSize(self.__ui_min_width, self.__ui_min_height)
        self.resize(self.__ui_width, self.__ui_height)
        self.move(QtWidgets.QDesktopWidget().availableGeometry().center() - self.frameGeometry().center())

        asset_path = os.path.dirname(__file__) + "/assets"

        # Main Layout
        main_lyt = QVBoxLayout()
        main_lyt.setContentsMargins(8, 10, 8, 10)
        self.setLayout(main_lyt)

        # ML.1 : Top grid layout
        top_grid_layout = QGridLayout()
        top_grid_layout.setSpacing(8)
        top_grid_layout.setColumnStretch(0,2)
        top_grid_layout.setColumnStretch(1,1)
        main_lyt.addLayout(top_grid_layout)

        # ML.1.1 : Left title
        left_title = QLabel("Objects in Scene")
        left_title.setAlignment(Qt.AlignCenter)
        top_grid_layout.addWidget(left_title,0,0)
        # ML.1.2 : Right title
        right_title = QLabel("Variant - Version")
        right_title.setAlignment(Qt.AlignCenter)
        top_grid_layout.addWidget(right_title,0,1)

        # ML.1.3 : Table objects
        self.__ui_object_list = QListWidget()
        top_grid_layout.addWidget(self.__ui_object_list,1,0)
        # ML.1.4 : Content Right layout
        content_right_layout = QVBoxLayout()
        top_grid_layout.addLayout(content_right_layout,1,1)
        # ML.1.4.1 : Lists layout
        right_lists_layout = QHBoxLayout()
        content_right_layout.addLayout(right_lists_layout)
        # ML.1.4.1.1 : Variant List
        self.__ui_variant_list = QListWidget()
        right_lists_layout.addWidget(self.__ui_variant_list,3)
        # ML.1.4.1.2 : Version List
        self.__ui_version_list = QListWidget()
        right_lists_layout.addWidget(self.__ui_version_list,2)
        # ML.1.4.2 : Button set version
        self.__ui_submit_version_btn = QPushButton("Set version")
        content_right_layout.addWidget(self.__ui_submit_version_btn)
        # ML.1.5 : Buttons left layout
        btn_left_lyt = QHBoxLayout()
        top_grid_layout.addLayout(btn_left_lyt,2,0)
        # ML.1.5.1 : Select out of date objects
        self.__ui_select_ood_objects = QPushButton()
        self.__ui_select_ood_objects.setIcon(QIcon(asset_path+"/warning.png"))
        height_hint = self.__ui_select_ood_objects.sizeHint().height()
        self.__ui_select_ood_objects.setFixedSize(QSize(height_hint,height_hint))
        btn_left_lyt.addWidget(self.__ui_select_ood_objects)
        # ML.1.5.2 : Update to last
        self.__ui_update_to_last = QPushButton("Update to last")
        btn_left_lyt.addWidget(self.__ui_update_to_last)
        # ML.1.6 : Buttons right layout
        btn_right_lyt = QHBoxLayout()
        top_grid_layout.addLayout(btn_right_lyt,2,1)
        # ML.1.6.1 : To SD Button
        self.__ui_to_sd = QPushButton("to SD")
        btn_right_lyt.addWidget(self.__ui_to_sd)
        # ML.1.6.2 : To HD Button
        self.__ui_to_hd = QPushButton("to HD")
        btn_right_lyt.addWidget(self.__ui_to_hd)

        # ML.2 : Separator
        sep = QFrame()
        sep.setFixedHeight(1)
        sep.setFrameShape(QFrame.HLine)
        sep.setFrameShadow(QFrame.Sunken)
        main_lyt.addWidget(sep)

        # ML.3 : Button bottom
        bottom_btn_lyt = QHBoxLayout()
        bottom_btn_lyt.setAlignment(Qt.AlignCenter)
        main_lyt.addLayout(bottom_btn_lyt)
        # ML.3.1 : Convert to maya button
        self.__ui_to_maya_btn = QPushButton("Convert to Maya")
        self.__ui_to_maya_btn.setFixedWidth(180)
        bottom_btn_lyt.addWidget(self.__ui_to_maya_btn)
        # ML.3.2 : Add transforms
        self.__ui_add_transforms = QPushButton("Add Transforms")
        self.__ui_add_transforms.setFixedWidth(180)
        bottom_btn_lyt.addWidget(self.__ui_add_transforms)

    # Refresh the ui according to the model attribute
    def __refresh_ui(self):
        # TODO refresh the UI according to model attributes
        pass
