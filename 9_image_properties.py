import cv2
import numpy as np

img = "lazy.png"

# Properties
color_img = cv2.imread(img, cv2.IMREAD_COLOR)
alpha_img = cv2.imread(img, cv2.IMREAD_UNCHANGED)
gray_img = cv2.imread(img, cv2.IMREAD_GRAYSCALE)

print('RGB Shape: ', color_img.shape)
print('ALPHA Shape: ', alpha_img.shape)    # In the output, instead of 3, there will be 4 channels - Alpha channel for transparency.
print('GRAY Shape: ', gray_img.shape)      # In the output, there will be no channels for grayscale.

cv2.imshow("RGB", color_img)
cv2.imshow("ALPHA", alpha_img)
cv2.imshow("GRAY", gray_img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Datatype - storage mechanism
print('Image Datatype: ', color_img.dtype)

# Size - multiplication of rows, cols, channels (not zero)
print("Image Size: ", color_img.size)
