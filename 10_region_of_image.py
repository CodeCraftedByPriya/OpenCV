import numpy as np
import cv2

img_file = 'lazy.png'
img = cv2.imread(img_file)

# To see only the part of the image that you are interested in
cv2.selectROI("Part of image", img, showCrosshair = , fromCenter = )

