# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\ricks\OneDrive\Development\Tools\cgdat\cgdat\..\qt\output_settings.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_OutputSettings(object):
    def setupUi(self, OutputSettings):
        OutputSettings.setObjectName("OutputSettings")
        OutputSettings.resize(618, 248)
        self.gridLayout = QtWidgets.QGridLayout(OutputSettings)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(OutputSettings)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(
            QtWidgets.QDialogButtonBox.Cancel | QtWidgets.QDialogButtonBox.Save
        )
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 1, 0, 1, 1)
        self.groupBox = QtWidgets.QGroupBox(OutputSettings)
        self.groupBox.setMinimumSize(QtCore.QSize(600, 200))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet("QGroupBox{padding-top:0px; margin-top:0px}")
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.iput_settings_label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.iput_settings_label.setFont(font)
        self.iput_settings_label.setObjectName("iput_settings_label")
        self.verticalLayout.addWidget(self.iput_settings_label)
        self.additional_input_file_settings_grid = QtWidgets.QGridLayout()
        self.additional_input_file_settings_grid.setObjectName(
            "additional_input_file_settings_grid"
        )
        self.label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.additional_input_file_settings_grid.addWidget(self.label, 0, 1, 1, 1)
        self.frame_rate_toggle = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_rate_toggle.sizePolicy().hasHeightForWidth()
        )
        self.frame_rate_toggle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_rate_toggle.setFont(font)
        self.frame_rate_toggle.setText("")
        self.frame_rate_toggle.setObjectName("frame_rate_toggle")
        self.additional_input_file_settings_grid.addWidget(
            self.frame_rate_toggle, 0, 0, 1, 1
        )
        self.frame_rate_value = QtWidgets.QDoubleSpinBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.frame_rate_value.sizePolicy().hasHeightForWidth()
        )
        self.frame_rate_value.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.frame_rate_value.setFont(font)
        self.frame_rate_value.setDecimals(0)
        self.frame_rate_value.setMinimum(100.0)
        self.frame_rate_value.setMaximum(1500.0)
        self.frame_rate_value.setSingleStep(1.0)
        self.frame_rate_value.setProperty("value", 1000.0)
        self.frame_rate_value.setObjectName("frame_rate_value")
        self.additional_input_file_settings_grid.addWidget(
            self.frame_rate_value, 0, 2, 1, 1
        )
        self.verticalLayout.addLayout(self.additional_input_file_settings_grid)
        self.output_settings_label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(11)
        self.output_settings_label.setFont(font)
        self.output_settings_label.setObjectName("output_settings_label")
        self.verticalLayout.addWidget(self.output_settings_label)
        self.additional_output_settings_grid = QtWidgets.QGridLayout()
        self.additional_output_settings_grid.setObjectName(
            "additional_output_settings_grid"
        )
        self.columns_toggle = QtWidgets.QCheckBox(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.columns_toggle.sizePolicy().hasHeightForWidth()
        )
        self.columns_toggle.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.columns_toggle.setFont(font)
        self.columns_toggle.setText("")
        self.columns_toggle.setObjectName("columns_toggle")
        self.additional_output_settings_grid.addWidget(self.columns_toggle, 0, 0, 1, 1)
        self.collumns_label = QtWidgets.QLabel(self.groupBox)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.collumns_label.setFont(font)
        self.collumns_label.setObjectName("collumns_label")
        self.additional_output_settings_grid.addWidget(self.collumns_label, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.additional_output_settings_grid)
        spacerItem = QtWidgets.QSpacerItem(
            20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding
        )
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)

        self.retranslateUi(OutputSettings)
        self.buttonBox.accepted.connect(OutputSettings.accept)
        self.buttonBox.rejected.connect(OutputSettings.reject)
        QtCore.QMetaObject.connectSlotsByName(OutputSettings)

    def retranslateUi(self, OutputSettings):
        _translate = QtCore.QCoreApplication.translate
        OutputSettings.setWindowTitle(_translate("OutputSettings", "Dialog"))
        self.iput_settings_label.setText(
            _translate(
                "OutputSettings",
                '<html><head/><body><p><span style=" text-decoration: underline;">Additional input file settings</span></p></body></html>',
            )
        )
        self.label.setText(_translate("OutputSettings", "Input measurement freq"))
        self.frame_rate_value.setSuffix(_translate("OutputSettings", " [Hz]"))
        self.output_settings_label.setText(
            _translate(
                "OutputSettings",
                '<html><head/><body><p><span style=" text-decoration: underline;">Change output variables</span></p></body></html>',
            )
        )
        self.columns_toggle.setToolTip(
            _translate(
                "OutputSettings",
                "By default the CGDAT tool only keeps the variables (csv columns) that are specified\n"
                ". Use this option to specify the collumns you want to include in the output file.",
            )
        )
        self.collumns_label.setText(_translate("OutputSettings", "Set output collumns"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    OutputSettings = QtWidgets.QDialog()
    ui = Ui_OutputSettings()
    ui.setupUi(OutputSettings)
    OutputSettings.show()
    sys.exit(app.exec_())

