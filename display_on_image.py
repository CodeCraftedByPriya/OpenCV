import cv2
image_path = "C:/Users/Priyalakshmi/Pictures/Memes/rockpet.png"
image = cv2.imread(image_path)


# Displaying Text
                ''' Here the syntax is, cv2.putText(output or the image file, Text to be displayed, (the coordinates to display the text), cv2.FONT_any style, font size, (the color scale), font thickness)'''
image = cv2.putText(image, 'SVT', (100, 400), cv2.FONT_HERSHEY_SIMPLEX, 4, (0, 0, 255), 5)
cv2.imshow('Text Over Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Drawing a line
                ''' Here the syntax is, cv2.line(output or the image file, (strt point coordinates), (end point coordinates), (colour scale), line thickness)'''
image = cv2.line(image, (450, 800), (900, 400), (0, 0, 512), 5)
cv2.imshow('Line Over Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Drawing a circle
                ''' Here the syntax is, cv2.circle(output or the image file, (the corrdinate of the center of the circle), radius, (colour scale), circle line thickness)'''
image = cv2.circle(image, (630,200), 80, (0, 0, 512), 5)
cv2.imshow('circle Over Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Drawing a Rectangle
                ''' Here the syntax is, cv2.rectangle(output or the image file, (strt point coordinates-left top corner), (end point coordinates-right bottom corner), (colour scale), line thickness)'''
image = cv2.rectangle(image, (150, 200), (800, 400), (0, 0, 512), 5)
cv2.imshow('Rectangle Over Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()


# Drawing an Ellipse
                ''' Here the syntax is, cv2.ellipse(output or the image file, (strt point coordinates), (axis - where this will be drawn), srt angle, end angle, (colour scale), thickness-even negative value)'''
image = cv2.ellipse(image, (150, 200), (120, 100), 30, 0, 360, (0, 0, 255), 7)
cv2.imshow('Ellipse Over Image', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
