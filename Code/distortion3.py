import cv2
import numpy as np
import math

def wave(img):
	rows, cols, color = img.shape
	img_out = np.zeros(img.shape, dtype=img.dtype)
	for k in range(color):
		for i in range(rows):
    			for j in range(cols):
        			offset_x = int(25.0 * math.sin(2 * 3.14 * i / 180))
        			offset_y = int(25.0 * math.sin(2 * 3.14 * j / 180))
            			img_out[i,j,k] = img[(i+offset_y)%rows,(j+offset_x)%cols,k]
	return img_out
