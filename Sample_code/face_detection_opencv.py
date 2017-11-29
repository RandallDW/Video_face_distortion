# -*- coding: utf-8 -*-
import cv2  
import sys  
import logging as log  
import datetime as dt  
from time import sleep  
from distortion2 import *
from distortion import *
import os.path
upper_dir = os.path.abspath('..')

cascPath = upper_dir + "/haarcascades" + "/haarcascade_frontalface_default.xml"  
faceCascade = cv2.CascadeClassifier(cascPath)  
  
video_capture = cv2.VideoCapture('test1.avi')  
  
  
while True:  
    if not video_capture.isOpened():  
        print('Unable to load camera.')  
        sleep(5)  
        pass  
    print('able to load camera.')  
  
    ret, frame = video_capture.read()  
  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    faces = faceCascade.detectMultiScale(
	gray,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30, 30),
	#flags = cv2.CV_HAAR_SCALE_IMAGE
    )


    for (x, y, w, h) in faces:
        roi = frame[y:y+h,x:x+w]
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)  
        img_returned=spherize(roi)
        frame[y:y+h, x:x+w] = img_returned
  
    cv2.imshow('Video', frame)  
  
  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  
  
  
video_capture.release()  
  
cv2.destroyAllWindows()  
