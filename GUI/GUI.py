import sys
import cv2
import numpy as np
from PyQt5.QtCore import *                                                      
from PyQt5.QtGui import *                                                       
from PyQt5.QtWidgets import *   
from mainWindow import *
from video import *
from distortion_parameter import *

class GUI(QMainWindow):
    def __init__(self, parent=None):
        QWidget.__init__(self,parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.is_distorted.stateChanged.connect(self.change_distortion_status)
        self.ui.start_video.clicked.connect(self.start_video)
        self.ui.end_video.clicked.connect(self.stop_video)

        self.ui.sphere.clicked.connect(self.sphere_distortion)
        self.ui.gridline.clicked.connect(self.gridline_distortion)
        self.ui.wave.clicked.connect(self.wave_distortion)

        self.video = None
        self._timer = QTimer(self)
        self._timer.timeout.connect(self.play)
        self._timer.start(27)
        self.update()
 
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
        if self.video is not None:
            if self.ui.is_distorted.isChecked():
                self.video.distortion = 1
            else:
                self.video.distortion = 0

    def start_video(self):
        if self.video is None:
            self.video_capture = cv2.VideoCapture(0)  
            self.video_capture.set(3, 20)
            self.video_capture.set(4, 20)
            self.video = Video(self.video_capture)

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



if __name__ == '__main__':
    app = QApplication(sys.argv) 
    run = GUI()
    run.show()
    sys.exit(app.exec_())
