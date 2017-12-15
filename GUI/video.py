import cv2
import sys  
import dlib
import os.path
import logging as log  
import datetime as dt  
import numpy as np

from time import sleep  
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *   
from GUI import *
from distortion import *
from distortion_parameter import *
from smooth import *
import numpy.ma as ma

class Video():
    def __init__(self,capture):
        self.capture = capture
        self.currentFrame=np.array([])

        upper_dir = os.path.abspath('..')
        cascPath =  upper_dir + "/haarcascades" + "/haarcascade_frontalface_default.xml"  
        self.faceCascade = cv2.CascadeClassifier(cascPath)  
        self.fourcc = cv2.cv.CV_FOURCC('M','J','P','G')

        self.tracker = dlib.correlation_tracker()
        self.tracking = 0

        self.distortion = 0
        self.distort_method = SPHERIZE
 
    def captureNextFrame(self):
        """                           
        capture frame and reverse RBG BGR and return opencv image   
        """
        ret, frame = self.capture.read()
        if ret == True:
            if self.distortion == 1:
                if not self.tracking:
                    faces = self.faceCascade.detectMultiScale(frame, 1.3, 5)
                    maxArea = 0
                    x = 0
                    y = 0
                    w = 0
                    h = 0
                    for (_x, _y, _w, _h) in faces:
                        if  _w * _h > maxArea:
                            x = int(_x)
                            y = int(_y)
                            w = int(_w)
                            h = int(_h)
                            maxArea = w * h

                    if maxArea > 0 :

                        self.tracker.start_track(frame,
                                        dlib.rectangle( x,
                                                        y,
                                                        x + w,
                                                        y + h))
                        roi = frame[y:y+h, x:x+w]
#			old_roi = roi;
#			print(roi)
	#		print(h)
	#		print(w)
			test_h = np.mgrid[-h/2:h/2,0:3]
			test_h = test_h[0,:]
			test_w = np.mgrid[-w/2:w/2,0:3]
			test_w = test_w[0,:]
#			print(test_h)
			test = [test_h,test_w]
#			print(test)
		#	print(test.shape[1])
		#	print(test_h.shape[1])
                        try:
                            if self.distort_method is SPHERIZE:
                                img_returned = spherize(roi)
                            elif self.distort_method is GRIDLINE:
#                                print('gridline')
                                img_returned = gridline(roi)
                            elif self.distort_method is WAVE:
                                img_returned = wave(roi)
				
#                            frame[y:y+h, x:x+w] = img_returned
			    mask = build_face_mask(w,h)
			    idx = (mask==0)
#			    print(img_returned)
			    img_returned[idx] = roi[idx]
#			    print(img_returned)
			    frame[y:y+h, x:x+w] = img_returned
#			    trim = ma.masked_array(roi,idx)
#			    print(trim.shape[0])
			  #  frame[idx] = 0
			   # print(frame)
                            self.tracking = 1
                        except:
                            pass

                else:
                    trackingQuality = self.tracker.update(frame)
                    if trackingQuality >= 8.75:
                        tracked_position =  self.tracker.get_position()

                        t_x = int(tracked_position.left())
                        t_y = int(tracked_position.top())
                        t_w = int(tracked_position.width())
                        t_h = int(tracked_position.height())
                        roi = frame[t_y:t_y+t_h, t_x:t_x+t_w]
                        try:
                            if self.distort_method is SPHERIZE:
                                img_returned = spherize(roi)
                            elif self.distort_method is GRIDLINE:
 #                               print('gridline')
                                img_returned = gridline(roi)
                            elif self.distort_method is WAVE:
                                img_returned = wave(roi)
                           # frame[t_y:t_y+t_h, t_x:t_x+t_w] = img_returned
			    t_mask = build_face_mask(t_w,t_h)
			    t_idx = (t_mask==0)
			    img_returned[t_idx] = roi[t_idx]
			    frame[t_y:t_y+t_h, t_x:t_x+t_w] = img_returned
			 #   t_trim = ma.masked_array(roi,t_idx)
			#    print(t_trim)
			    #frame[t_idx] = 0
			   # print(t_idx)
                        except:
                            pass
                    else:
                        self.tracking = 0;
            self.currentFrame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    def convertFrame(self):
        """     converts frame to format suitable for QtGui            """
        try:
            height, width = self.currentFrame.shape[:2]
            img = QImage(self.currentFrame,
                              width,
                              height,
                              QImage.Format_RGB888)
            img = QPixmap.fromImage(img)
            self.previousFrame = self.currentFrame
            return img
        except:
            return None
