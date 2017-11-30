# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(742, 530)
        self.video_frame = QtWidgets.QFrame(Form)
        self.video_frame.setGeometry(QtCore.QRect(10, 9, 501, 511))
        self.video_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_frame.setObjectName("video_frame")
        self.VideoFrame = QtWidgets.QLabel(self.video_frame)
        self.VideoFrame.setGeometry(QtCore.QRect(10, 15, 481, 481))
        self.VideoFrame.setText("")
        self.VideoFrame.setObjectName("VideoFrame")
        self.distortion_controller = QtWidgets.QFrame(Form)
        self.distortion_controller.setGeometry(QtCore.QRect(520, 10, 211, 141))
        self.distortion_controller.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.distortion_controller.setFrameShadow(QtWidgets.QFrame.Raised)
        self.distortion_controller.setObjectName("distortion_controller")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.distortion_controller)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridline = QtWidgets.QPushButton(self.distortion_controller)
        self.gridline.setObjectName("gridline")
        self.gridLayout_2.addWidget(self.gridline, 2, 0, 1, 1)
        self.sphere = QtWidgets.QPushButton(self.distortion_controller)
        self.sphere.setObjectName("sphere")
        self.gridLayout_2.addWidget(self.sphere, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.distortion_controller)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.wave = QtWidgets.QPushButton(self.distortion_controller)
        self.wave.setObjectName("wave")
        self.gridLayout_2.addWidget(self.wave, 3, 0, 1, 1)
        self.gridLayout_3.addLayout(self.gridLayout_2, 0, 0, 1, 1)
        self.video_controller = QtWidgets.QFrame(Form)
        self.video_controller.setGeometry(QtCore.QRect(520, 414, 211, 111))
        self.video_controller.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.video_controller.setFrameShadow(QtWidgets.QFrame.Raised)
        self.video_controller.setObjectName("video_controller")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.video_controller)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.start_video = QtWidgets.QPushButton(self.video_controller)
        self.start_video.setObjectName("start_video")
        self.verticalLayout.addWidget(self.start_video)
        self.end_video = QtWidgets.QPushButton(self.video_controller)
        self.end_video.setObjectName("end_video")
        self.verticalLayout.addWidget(self.end_video)
        self.is_distorted = QtWidgets.QCheckBox(self.video_controller)
        self.is_distorted.setObjectName("is_distorted")
        self.verticalLayout.addWidget(self.is_distorted, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.gridline.setText(_translate("Form", "Gridline"))
        self.sphere.setText(_translate("Form", "Sphere"))
        self.label.setText(_translate("Form", "Distortion Method"))
        self.wave.setText(_translate("Form", "Wave"))
        self.start_video.setText(_translate("Form", "Start"))
        self.end_video.setText(_translate("Form", "End"))
        self.is_distorted.setText(_translate("Form", "Distortion"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

