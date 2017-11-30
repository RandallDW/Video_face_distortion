import math
import math
import numpy as np
from PIL import Image
from scipy import signal
import numpy as np
def spherize(img):
    width = img.shape[1]
    height = img.shape[0]
    mid_x = width / 2
    mid_y = height / 2
    max_mid_xy = max(mid_x, mid_y)
    temp = np.zeros((height,width,3),np.uint8)
    for w in xrange(width):
        for h in xrange(height):
            offset_x = w - mid_x
            offset_y = h - mid_y

            radian = math.atan2(offset_y, offset_x)
            radius = (offset_x ** 2 + offset_y ** 2) / max_mid_xy

            x = int(radius * math.cos(radian)) + mid_x
            y = int(radius * math.sin(radian)) + mid_y

            x = min(max(x, 0), width - 1)
            y = min(max(y, 0), height - 1)
            
            temp[w, h] = img[x, y]

    return temp

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
