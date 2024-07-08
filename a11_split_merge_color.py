import numpy as np
import cv2

img_file = 'Cropped.png'
img = cv2.imread(img_file)

print("RGB: ", img.shape)

# Split the images based on RGB
g, b, r = cv2.split(img)
cv2.imshow("Green scale:", g)
cv2.imshow("Blue scale:", b)
cv2.imshow("Red scale:", r)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Merge the images based on RGB
merge = cv2.merge((g, b, r))
cv2.imshow("Merged RGB image:", merge)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Changing the color of the image
'''We already learnt how to change colors with RGB and Gray Scale, but those are not the only colors:
Scales like LAB, LUV, HSI, etc
Which included saturation or intensity into account anf not just RGB'''

color = cv2.cvtColor(img, cv2.COLOR_RGB2Luv)
color2 = cv2.cvtColor(img, cv2.COLOR_RGB2Lab)
cv2.imshow("RGB to LUV Color Change: ", color)
cv2.imshow("RGB to LAB Color Change: ", color2)
cv2.waitKey(0)
cv2.destroyAllWindows()

