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

