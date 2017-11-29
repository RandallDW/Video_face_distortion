import math
from PIL import Image
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

