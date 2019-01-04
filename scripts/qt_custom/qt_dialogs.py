# -*- coding: utf-8 -*-
"""
This file contains some dialog classes that are created for the CGDAT GUI. These classes inherit from the
QtWidgets.Qdialog Class.
"""


### Import needed pyqt modules modules ###
from PyQt5 import QtWidgets, QtCore, QtGui

### Import custom classes ###
from qt_ui import Ui_OutputSettings
from qt_ui import Ui_ProgressDialog
from qt_ui import Ui_ImportDialog
from qt_custom import MultiSelectMenu

### Import other classes ###
import os

#####################################################################
#### Script Media paths                                          ####
#####################################################################
DIRNAME = os.path.dirname(os.path.abspath(__file__))  # Get relative script path
TOGGLE_ICON_ON = os.path.abspath(os.path.join(DIRNAME, "../..", "media/toggle_on.png")).replace('\\','/')    # Toggle on icon
TOGGLE_ICON_DISABLED = os.path.abspath(os.path.join(DIRNAME, "../..", "media/toggle_off_disabled.png")).replace('\\','/')    # Toggle on icon
TOGGLE_ICON_OFF = os.path.abspath(os.path.join(DIRNAME, "../..", "media/toggle_off.png")).replace('\\','/')  # Toggle off icon

#####################################################################
#### Overload custom progressDialog class                        ####
#####################################################################
class progressDialog(QtWidgets.QDialog, Ui_ProgressDialog):
    """This class overloads the qt python class that was generated by yQt5.uic.pyuic converter for the
    progressDialog so it can be used as a dialog in our main GUI.

    Args:
        QtWidgets (QtWidgets.QDialog): Main dialog class
        Ui_ProgressDialog (object): Custom made dialog class
    """

    #################################################
    #### Class initializer                       ####
    #################################################
    def __init__(self,parent=None):
        """Object initiation.
            parent (object, optional): Defaults to None. The partent object the class needs to be applied to.
        """
        QtWidgets.QDialog.__init__(self, parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.setupUi(self)

    #################################################
    #### updateProgressConsole method            ####
    #################################################
    def updateProgressConsole(self, text, color = None):
        """A function used to append messages to the progress console.

        Args:
            text (str): The message we want to append.
        """

        ### Add normal text when no color was given ###
        if color == None:
            self.progress_console.append(text)
        else:
            color_txt = "<span style=\" color:" + color + ";\" >" + text + "</span>"
            self.progress_console.append(color_txt)

    #################################################
    #### updateProgressBar method                ####
    #################################################
    def updateProgressBar(self, percentage):
        """Function used to update the progress bar.

        Args:
            int (int): The percentage of the progress bar.
        """

        ### Set progress bar value ###
        self.progress_bar.setValue(percentage)

        ### If 100 % change dialog buttons ###
        if percentage == 100.0:
            self.buttonBox.removeButton(self.buttonBox.button(QtWidgets.QDialogButtonBox.Cancel))  # Remove cancel button
            self.buttonBox.addButton("Finish", QtWidgets.QDialogButtonBox.AcceptRole)

#####################################################################
#### Overload custom import Dialog class                         ####
#####################################################################
class importDialog(QtWidgets.QDialog, Ui_ImportDialog):
    """This class overloads the qt python class that was generated by yQt5.uic.pyuic converter for the
    importDialog so it can be used as a dialog in our main GUI.

    Args:
        QtWidgets (QtWidgets.QDialog): Main dialog class
        Ui_ImportDialog (object): Custom made dialog class
    """

    #################################################
    #### Class initializer                       ####
    #################################################
    def __init__(self,parent=None):
        QtWidgets.QDialog.__init__(self, parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.setupUi(self)

#####################################################################
#### Overload auto created output settings window class          ####
#####################################################################
class outputSettingsDialog(QtWidgets.QDialog, Ui_OutputSettings):
    """This class overloads the qt python class that was generated by yQt5.uic.pyuic converter for the
    output_settings_ui so it can be used as a dialog in our main GUI.

    Args:
        QtWidgets (QtWidgets.QDialog): Main dialog class
        Ui_OutputSettings (object): Custom made dialog class
    """

    #################################################
    #### Class initializer                       ####
    #################################################
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent, QtCore.Qt.WindowSystemMenuHint | QtCore.Qt.WindowTitleHint)
        self.setupUi(self)

        ### Create toggle buttons ###
        self.frame_rate_toggle.setStyleSheet("QCheckBox::indicator:checked {image: url('"+TOGGLE_ICON_ON+"');}\n QCheckBox::indicator:unchecked {image: url('"+TOGGLE_ICON_OFF+"');}\n QCheckBox::indicator:disabled {image: url('"+TOGGLE_ICON_DISABLED+"');}")
        self.columns_toggle.setStyleSheet("QCheckBox::indicator:checked {image: url('"+TOGGLE_ICON_ON+"');}\n QCheckBox::indicator:unchecked {image: url('"+TOGGLE_ICON_OFF+"');}\n QCheckBox::indicator:disabled {image: url('"+TOGGLE_ICON_DISABLED+"');}")

        ### Create multi checkbox column choicer ###
        self.column_choicer_drop_down_menu = MultiSelectMenu()
        font = QtGui.QFont()
        font.setPointSize(10)
        self.column_choicer_drop_down_menu.setFont(font)
        self.column_choicer_drop_down_menu.setObjectName("column_choiser")
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.column_choicer_drop_down_menu.sizePolicy().hasHeightForWidth())
        self.column_choicer_drop_down_menu.setSizePolicy(sizePolicy)

        # self.column_choicer_drop_down_menu.font(10)
        self.additional_output_settings_grid.addWidget(self.column_choicer_drop_down_menu, 0, 2, 1, 1)
        self.column_choicer_drop_down_menu.setText("Please import a data file to see the available columns")
        self.column_choicer_drop_down_menu.setEnabled(0)
        self.columns_toggle.setEnabled(0)

