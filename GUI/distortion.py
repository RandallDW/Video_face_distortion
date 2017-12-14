import math
#import os
import numpy as np
from scipy import signal

"""
    spherize distortion
"""
def spherize(img):
    width = img.shape[1]
    height = img.shape[0]
    mid_x = width / 2
    mid_y = height / 2
    max_mid_xy = max(mid_x, mid_y)
    temp = np.zeros((height, width, 3), np.uint8)

    for w in range(0, width):
        for h in range(0, height):
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
    n = 100
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
                img_out[i, j, k] = img[(i+offset_y) % rows, (j + offset_x) % cols, k]
    return img_out

    
def rainbow(img):
    img_1 = img.copy()
    img_2 = img.copy()
    img_3 = img.copy()
    img_4 = img.copy()

    img_out = img.copy()

    Offset = 7

    row, col, channel = img.shape
    
    img_1[:, 0 : col-1-Offset, :] = img[:, Offset:col-1, :] 
    img_2[:, Offset:col-1, :]     = img[:, 0 : col-1-Offset, :] 
    img_3[0:row-1-Offset, :, :]   = img[Offset:row-1, :, :] 
    img_4[Offset:row-1, :, :]     = img[0:row-1-Offset, :, :]

    img_out = (img_1 + img_2 + img_3 + img_4)  
    return img_out  

