import math
import numpy as np
from PIL import Image
from scipy import signal

def gridline(img):
	n=100
	sobel_x = np.c_[
	    [-1,0,1],
	    [-2,0,2],
	    [-1,0,1]
	]

	sobel_y = np.c_[
	    [1,2,1],
	    [0,0,0],
	    [-1,-2,-1]
	]

	ims = []
	for d in range(3):
	    sx = signal.convolve2d(img[:,:,d], sobel_x, mode="same", boundary="symm")
	    sy = signal.convolve2d(img[:,:,d], sobel_y, mode="same", boundary="symm")
	    ims.append(np.sqrt(sx*sx + sy*sy))

	im_conv = np.stack(ims, axis=2).astype("uint8")

	return im_conv
