import sys
import cv2
import numpy as np
from PyQt5.QtCore import *                                                      
from PyQt5.QtGui import *                                                       
from PyQt5.QtWidgets import *   
from mainWindow import *
from video import *
from distortion_parameter import *

class FileDialog(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.title = 'Browse a Video File'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()
 
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.show()
 
    def openFileNameDialog(self):    
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName

class GUI(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.ui = Ui_MainWidget()
        self.ui.setupUi(self)

        self.ui.is_distorted.stateChanged.connect(self.change_distortion_status)
        self.ui.start_video.clicked.connect(self.start_video)
        self.ui.end_video.clicked.connect(self.stop_video)
	self.ui.file_input_check.stateChanged.connect(self.fileIn)
	self.ui.file_browse.clicked.connect(self.fileBrow)

        self.ui.sphere.clicked.connect(self.sphere_distortion)
        self.ui.gridline.clicked.connect(self.gridline_distortion)
        self.ui.wave.clicked.connect(self.wave_distortion)
        self.ui.rainbow.clicked.connect(self.rainbow_distortion)

	self.input = 0
        self.video = None
        self.is_distortion = 0
	self.fileW = None
	self.filename = 0
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)
        self.update()
	

    def fileBrow(self):
	self.fileW = FileDialog()
	self.filename = self.fileW.openFileNameDialog()
	self.fileW.close()
	self.ui.lineEdit.setText(self.filename)

    def fileIn(self):
		if self.ui.file_input_check.isChecked():
			self.input = self.ui.lineEdit.text()
		else:
			self.input = 0
 
    def play(self):
        if self.video is not None:
            try:
                self.video.captureNextFrame()
                frame = self.video.convertFrame()
                if frame is not None:
                    self.ui.VideoFrame.setPixmap(frame)
                    self.ui.VideoFrame.setScaledContents(True)
            except TypeError:
                print ("No frame")

    def change_distortion_status(self):
        if self.ui.is_distorted.isChecked():
            self.is_distortion = 1
        else:
            self.is_distortion = 0

        if self.video is not None:
            if self.ui.is_distorted.isChecked():
                self.video.distortion = 1
            else:
                self.video.distortion = 0

    def start_video(self):
        if self.video is None:
	    try:
	        if self.ui.file_input_check.isChecked():
		    self.input = self.ui.lineEdit.text()
	        else:
		    self.input = 0
                self.video_capture = cv2.VideoCapture(self.input)  
                if not self.video_capture.isOpened():  
		    return
                self.video_capture.set(3, 20)
                self.video_capture.set(4, 20)
                self.video = Video(self.video_capture, self.is_distortion)
	    except:
		pass

    def stop_video(self):
        if self.video is not None:
            self.video_capture.release() 
            self.video = None
            self.ui.VideoFrame.clear()
            self.ui.is_distorted.setCheckState(False)

    def sphere_distortion(self):
        if self.video is not None:
            self.video.distort_method = SPHERIZE

    def gridline_distortion(self):
        if self.video is not None:
            self.video.distort_method = GRIDLINE

    def wave_distortion(self):
        if self.video is not None:
            self.video.distort_method = WAVE

    def rainbow_distortion(self):
        if self.video is not None:
            self.video.distort_method = RAINBOW



if __name__ == '__main__':
    app = QApplication(sys.argv) 
    run = GUI()
    run.show()
    sys.exit(app.exec_())
