import cv2
import numpy as np
import os.path

from PIL import Image
from distortion import *


cap = cv2.VideoCapture(0)  
cap.set(3,20)
cap.set(4,20)
cv2.namedWindow("Frame")

while True:  
    if not cap.isOpened():  
        print('Unable to load camera.')  
        sleep(5)  
        pass  
    print('able to load camera.')  
  
    ret, frame = cap.read()  
    cv2_im = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    frame = Image.fromarray(cv2_im)
  
    img_distorted  =  spherize(frame)
 
    image = cv2.cvtColor(np.array(img_distorted), cv2.COLOR_RGB2BGR)
    cv2.imshow('Video', image)  
  
  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  
  
  
cap.release()  
  
cv2.destroyAllWindows()  
