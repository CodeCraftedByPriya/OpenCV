import numpy as np
import cv2

img_file = 'lazy.png'
img = cv2.imread(img_file)

# To see only the part of the image that you are interested in
#cv2.selectROI("Part of image", img, showCrosshair = , fromCenter = )

roi = cv2.selectROI(img)
print(roi)

# Cropping Selected region of ROI
roi_crop = img[int(roi[1]): int(roi[1] + roi[3]), int(roi[0]): int(roi[0]) + int(roi[2])]
# how many rows or cols - per grid
cv2.imshow("ROI CROPPED IMAGE", roi_crop)
cv2.imwrite("Cropped.png", roi_crop)
cv2.waitKey(0)
cv2.destroyAllWindows()
