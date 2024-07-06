import cv2
image_path = "C:/Users/Priyalakshmi/Pictures/Memes/rockpet.png"
image = cv2.imread(image_path)

# Changing colour space
# RGB --> Gray (Gray takes less time in detection and identification)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow('Original Image', image)
cv2.imshow('Gray Scale Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Multiple modes - now you can do it without the multiple lines code above.
'''To change the image color to gray add -- 0
   To change the image color to original -- 1'''
img = cv2.imread(image_path, 0)
cv2.imshow("Ori Img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Change gray to colour
gray = cv2.imread(image_path, 1)
cv2.imshow("Gray to Ori Img", gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
