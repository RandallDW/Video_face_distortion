import cv2  
import sys  
import logging as log  
import datetime as dt  
from time import sleep  
from distortion2 import *
from distortion import *
import os.path
import dlib

upper_dir = os.path.abspath('..')

cascPath = upper_dir + "/haarcascades" + "/haarcascade_frontalface_default.xml"  
faceCascade = cv2.CascadeClassifier(cascPath)
fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
video_capture = cv2.VideoCapture('test1.avi')  
out = cv2.VideoWriter('outpy.avi',fourcc, 20.0, (528,288))

tracker = dlib.correlation_tracker()
tracking = 0

while video_capture.isOpened():

    ret, frame = video_capture.read()
    if frame is None:
	break
    if not tracking:
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        maxArea = 0
        x = 0
        y = 0
        w = 0
        h = 0
        for (_x,_y,_w,_h) in faces:
            if  _w*_h > maxArea:
                x = int(_x)
                y = int(_y)
                w = int(_w)
                h = int(_h)
                maxArea = w*h

	if maxArea > 0 :

            tracker.start_track(frame,
                            dlib.rectangle( x,
                                            y,
                                            x+w,
                                            y+h))
	    roi = frame[y:y+h,x:x+w]
            img_returned=spherize(roi)
	    frame[y:y+h, x:x+w] = img_returned
            trackingFace = 1
    if tracking:
	trackingQuality = tracker.update( frame )
        if trackingQuality >= 8.75:
            tracked_position =  tracker.get_position()

            t_x = int(tracked_position.left())
            t_y = int(tracked_position.top())
            t_w = int(tracked_position.width())
            t_h = int(tracked_position.height())
            roi = frame[t_y:t_y+t_h, t_x:t_x+t_w]
	    img_returned=spherize(roi)
            frame[y:y+h, x:x+w] = img_returned

	else:
	    tracking = 0;
    out.write(frame)
    cv2.imshow('Video', frame)
    
    if cv2.waitKey(10) & 0xFF == ord('q'):  
        break  
  
  
video_capture.release()  
out.release()
cv2.destroyAllWindows() 




