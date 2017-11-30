import cv2  
import sys  
import thread
import logging as log  
import datetime as dt  
import numpy as np
from time import sleep  
from distortion import *
import threading
import os.path
import dlib


global distort

def change_distortion_method():
    while 1:
        if cv2.waitKey(1) & 0xFF == ord('z'):
            print('z')

def video_face_distortion():
    print('2')
    upper_dir = os.path.abspath('..')

    cascPath = upper_dir + "/haarcascades" + "/haarcascade_frontalface_default.xml"  
    faceCascade = cv2.CascadeClassifier(cascPath)

    fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
    out = cv2.VideoWriter('outpy.avi', fourcc, 20.0, (320, 240))

    video_capture = cv2.VideoCapture(0)  
    video_capture.set(3, 100)
    video_capture.set(4, 200)

    tracker = dlib.correlation_tracker()
    tracking = 0






    while video_capture.isOpened():
        ret, frame = video_capture.read()
        if frame is None:
            out.release()
            break
        if not tracking:
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.3, 5)
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

                tracker.start_track(frame,
                                dlib.rectangle( x,
                                                y,
                                                x + w,
                                                y + h))
                roi = frame[y : y + h, x : x + w]
                try:
                    img_returned = spherize(roi)
                except:
                    continue
                frame[y : y + h, x : x + w] = img_returned
                tracking = 1

        else:
            trackingQuality = tracker.update( frame )
            if trackingQuality >= 8.75:
                tracked_position =  tracker.get_position()

                t_x = int(tracked_position.left())
                t_y = int(tracked_position.top())
                t_w = int(tracked_position.width())
                t_h = int(tracked_position.height())
                roi = frame[t_y : t_y + t_h, t_x : t_x + t_w]
                try:
                    img_returned = spherize(roi)
                except:
                    continue
                frame[t_y : t_y + t_h, t_x : t_x + t_w] = img_returned
                

            else:
                tracking = 0;

        cv2.imshow('Video', frame)
        out.write(frame)
#        if cv2.waitKey(1) & 0xFF == ord('z'):
#            out.release()
#            break  
        
      
      
    video_capture.release()  
      
    cv2.destroyAllWindows() 






    

if __name__ == '__main__':
    distort = 0
    thread.start_new_thread(change_distortion_method, ())
    thread.start_new_thread(video_face_distortion, ())
    while True:
        continue
'''
    upper_dir = os.path.abspath('..')

    cascPath = upper_dir + "/haarcascades" + "/haarcascade_frontalface_default.xml"  
    faceCascade = cv2.CascadeClassifier(cascPath)

    fourcc = cv2.cv.CV_FOURCC('M','J','P','G')
    out = cv2.VideoWriter('outpy.avi', fourcc, 20.0, (320, 240))

    video_capture = cv2.VideoCapture(0)  
    video_capture.set(3, 100)
    video_capture.set(4, 200)

    tracker = dlib.correlation_tracker()
    tracking = 0






    while video_capture.isOpened():
        print('b')
        ret, frame = video_capture.read()
        if frame is None:
            out.release()
            break
        if not tracking:
            
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.3, 5)
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

                tracker.start_track(frame,
                                dlib.rectangle( x,
                                                y,
                                                x + w,
                                                y + h))
                roi = frame[y : y + h, x : x + w]
                try:
                    img_returned = spherize(roi)
                except:
                    continue
                frame[y : y + h, x : x + w] = img_returned
                tracking = 1

        else:
            trackingQuality = tracker.update( frame )
            if trackingQuality >= 8.75:
                tracked_position =  tracker.get_position()

                t_x = int(tracked_position.left())
                t_y = int(tracked_position.top())
                t_w = int(tracked_position.width())
                t_h = int(tracked_position.height())
                roi = frame[t_y : t_y + t_h, t_x : t_x + t_w]
                try:
                    img_returned = spherize(roi)
                except:
                    continue
                frame[t_y : t_y + t_h, t_x : t_x + t_w] = img_returned
                

            else:
                tracking = 0;

        cv2.imshow('Video', frame)
        out.write(frame)
#        if cv2.waitKey(1) & 0xFF == ord('z'):
#            out.release()
#            break  
        
      
      
    video_capture.release()  
      
    cv2.destroyAllWindows() 



'''
