# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'videosettings.ui'
#
# Created: Fri Jun 28 11:48:14 2013
#      by: PyQt6 UI code generator 5.0-snapshot-478d7f271b71
#
# WARNING! All changes made in this file will be lost!

from PyQt6 import QtCore, QtGui, QtWidgets

class Ui_VideoSettingsUi(object):
    def setupUi(self, VideoSettingsUi):
        VideoSettingsUi.setObjectName("VideoSettingsUi")
        VideoSettingsUi.resize(561, 369)
        self.gridLayout_4 = QtWidgets.QGridLayout(VideoSettingsUi)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.scrollArea = QtWidgets.QScrollArea(VideoSettingsUi)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 543, 250))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.groupBox = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 2)
        self.audioCodecBox = QtWidgets.QComboBox(self.groupBox)
        self.audioCodecBox.setObjectName("audioCodecBox")
        self.gridLayout.addWidget(self.audioCodecBox, 1, 0, 1, 2)
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 2)
        self.audioSampleRateBox = QtWidgets.QComboBox(self.groupBox)
        self.audioSampleRateBox.setObjectName("audioSampleRateBox")
        self.gridLayout.addWidget(self.audioSampleRateBox, 3, 0, 1, 2)
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 4, 0, 1, 1)
        self.audioQualitySlider = QtWidgets.QSlider(self.groupBox)
        self.audioQualitySlider.setMaximum(4)
        self.audioQualitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.audioQualitySlider.setObjectName("audioQualitySlider")
        self.gridLayout.addWidget(self.audioQualitySlider, 4, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox, 0, 0, 1, 1)
        self.groupBox_2 = QtWidgets.QGroupBox(self.scrollAreaWidgetContents)
        self.groupBox_2.setObjectName("groupBox_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_8 = QtWidgets.QLabel(self.groupBox_2)
        self.label_8.setObjectName("label_8")
        self.gridLayout_2.addWidget(self.label_8, 0, 0, 1, 2)
        self.videoResolutionBox = QtWidgets.QComboBox(self.groupBox_2)
        self.videoResolutionBox.setObjectName("videoResolutionBox")
        self.gridLayout_2.addWidget(self.videoResolutionBox, 1, 0, 1, 2)
        self.label_9 = QtWidgets.QLabel(self.groupBox_2)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 2)
        self.videoFramerateBox = QtWidgets.QComboBox(self.groupBox_2)
        self.videoFramerateBox.setObjectName("videoFramerateBox")
        self.gridLayout_2.addWidget(self.videoFramerateBox, 3, 0, 1, 2)
        self.label_6 = QtWidgets.QLabel(self.groupBox_2)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 4, 0, 1, 2)
        self.videoCodecBox = QtWidgets.QComboBox(self.groupBox_2)
        self.videoCodecBox.setObjectName("videoCodecBox")
        self.gridLayout_2.addWidget(self.videoCodecBox, 5, 0, 1, 2)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.gridLayout_2.addWidget(self.label_7, 6, 0, 1, 1)
        self.videoQualitySlider = QtWidgets.QSlider(self.groupBox_2)
        self.videoQualitySlider.setMaximum(4)
        self.videoQualitySlider.setOrientation(QtCore.Qt.Horizontal)
        self.videoQualitySlider.setObjectName("videoQualitySlider")
        self.gridLayout_2.addWidget(self.videoQualitySlider, 6, 1, 1, 1)
        self.gridLayout_3.addWidget(self.groupBox_2, 0, 1, 3, 1)
        self.label_4 = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label_4.setObjectName("label_4")
        self.gridLayout_3.addWidget(self.label_4, 1, 0, 1, 1)
        self.containerFormatBox = QtWidgets.QComboBox(self.scrollAreaWidgetContents)
        self.containerFormatBox.setObjectName("containerFormatBox")
        self.gridLayout_3.addWidget(self.containerFormatBox, 2, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout_4.addWidget(self.scrollArea, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 14, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_4.addItem(spacerItem, 1, 0, 1, 1)
        self.buttonBox = QtWidgets.QDialogButtonBox(VideoSettingsUi)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout_4.addWidget(self.buttonBox, 2, 0, 1, 1)

        self.retranslateUi(VideoSettingsUi)
        self.buttonBox.accepted.connect(VideoSettingsUi.accept)
        self.buttonBox.rejected.connect(VideoSettingsUi.reject)
        QtCore.QMetaObject.connectSlotsByName(VideoSettingsUi)

    def retranslateUi(self, VideoSettingsUi):
        _translate = QtCore.QCoreApplication.translate
        VideoSettingsUi.setWindowTitle(_translate("VideoSettingsUi", "Dialog"))
        self.groupBox.setTitle(_translate("VideoSettingsUi", "Audio"))
        self.label_2.setText(_translate("VideoSettingsUi", "Audio Codec:"))
        self.label_5.setText(_translate("VideoSettingsUi", "Sample Rate:"))
        self.label_3.setText(_translate("VideoSettingsUi", "Quality:"))
        self.groupBox_2.setTitle(_translate("VideoSettingsUi", "Video"))
        self.label_8.setText(_translate("VideoSettingsUi", "Resolution:"))
        self.label_9.setText(_translate("VideoSettingsUi", "Framerate:"))
        self.label_6.setText(_translate("VideoSettingsUi", "Video Codec:"))
        self.label_7.setText(_translate("VideoSettingsUi", "Quality:"))
        self.label_4.setText(_translate("VideoSettingsUi", "Container Format:"))

