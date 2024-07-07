import cv2

# Capture Video
# Using Webcam
abc = cv2.VideoCapture(0)
while(True):
    ret_, frame = abc.read()                                      # Reads each frame (25 per sec)
    cv2.imshow("abc", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):                         # Here this 'q' is the exit key.
        break
        abc.release()
cv2.destroyAllWindows()
