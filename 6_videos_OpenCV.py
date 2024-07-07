import cv2
abc = cv2.VideoCapture(0)

# Capture Videos using OpenCV
if (abc.isOpened() == False):
    print("Could not open the camera")

# Set Resolution
width = int(abc.get(3))
height = int(abc.get(4))

# video codded - encoding and decoding
video_cod = cv2.VideoWriter_fourcc(*'XVID')
video_output = cv2.VideoWriter("Captured_Video.MP4", video_cod, 30, (width, height))

while(True):
    ret_, frame = abc.read()
    if ret_ == True:
        video_output.write(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'): #Here this 'q' is the exit key.
            break
    else:
        break
abc.release()
video_output.release()
cv2.destroyAllWindows()
print("Video saved successfully!")
