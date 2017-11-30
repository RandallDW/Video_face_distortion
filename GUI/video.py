import sys
import cv2
import numpy as np
from PyQt5.QtCore import *                                                      
from PyQt5.QtGui import *                                                       
from PyQt5.QtWidgets import *   
from GUI import *
from distortion import *
class Video():
    def __init__(self,capture):
        self.capture = capture
        self.currentFrame=np.array([])

        upper_dir = os.path.abspath('..')
        cascPath =  upper_dir + "/haarcascades" + "/haarcascade_frontalface_default.xml"  
        self.faceCascade = cv2.CascadeClassifier(cascPath)  
        self.distortion = 0
 
    def captureNextFrame(self):
        """                           
        capture frame and reverse RBG BGR and return opencv image                                      
        """
        ret, frame = self.capture.read()
        if ret == True:
            if self.distortion is 1:
                faces = self.faceCascade.detectMultiScale(
                    frame,
                    scaleFactor=1.1,
                    minNeighbors=5,
                    minSize=(30, 30),
                    
                )
                for (x, y, w, h) in faces:
                    roi = frame[y:y+h,x:x+w]
                    img_returned = spherize(roi)
                    frame[y:y+h, x:x+w] = img_returned
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
