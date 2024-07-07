import numpy as np
import cv2

# Basic Operations
# Access pixel values
'''RGB --> 0 to 255
    0 --> Not present
    255 --> Full R or G or B'''

img = cv2.imread('savenew_petrock.png')
px = img[100, 200]
print(f"The RGB combination: {px}")         # Gives the RGB of tht particular pixel

blue = img[100, 200, 0]
green = img[100, 200, 1]
red = img[100, 200, 2]
'''the 3rd parameter is the index position of the RGB. [B, G, R]
    0 ----> blue
    1 ----> green
    2 ----> red'''
print(f"Blue: {blue}\nGreen: {green}\nRed: {red}")

img[100, 200] = [100, 120, 150]              # changing the color combination of the selected pixel.
print("The new color combination: ",img[100, 200])
