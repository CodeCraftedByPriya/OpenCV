import cv2
image_path = "C:/Users/Priyalakshmi/Pictures/Memes/rockpet.png"
image = cv2.imread(image_path)

# (Rows, columns, channels-colour values)
print(image.shape)

# Resize the image
resize = cv2.resize(image, (500, 900))
cv2.imshow('Original Image', image)
cv2.imshow('Resized Image', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()

