import cv2
image_path = "C:/Users/Priyalakshmi/Pictures/Memes/rockpet.png"
image = cv2.imread(image_path)

# Display the image
cv2.imshow("sample", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Saving the image (The new one without any noises or with new changes)
# a directory (a folder to save the new image) - here OpenCV - Simplilearn
filename = 'savenew_petrock.png'
cv2.imwrite(filename, image)
print("Successfully saved the image!")

# Accessing Image Properties
# (Rows, columns, channels-colour values)
print(image.shape)
