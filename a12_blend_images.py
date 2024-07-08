import cv2

# Two sources of the images for blending
img_file = 'Cropped.png'
src1 = cv2.imread(img_file, cv2.IMREAD_COLOR)
img_file2 = "Text.png"
src2 = cv2.imread(img_file2, cv2.IMREAD_COLOR)

# Resizing it to make it match
img1 = cv2.resize(src1, (750, 500))
img2 = cv2.resize(src2, (750, 500))

blend = cv2.addWeighted(img1, 0.5, img2, 0.5, 0.0)

# Syntax of the above ---> cv2.addWeighted(img1, alpha, img2, beta, gamma)
     '''img1: The first input image. (Here, img1 contributes 50%)
        img2: The second input image. (Here, img2 contributes 50%)
        0.5 (alpha): This is the weight of the first image, img1.
        0.5 (beta): This is the weight of the second image, img2.
        0.0 (gamma): This is a scalar added to each sum. Gamma can be used to adjust the brightness of the blended image.'''

cv2.imshow("Blended Images", blend)
cv2.waitKey(0)
cv2.destroyAllWindows()
