import cv2

cap = cv2.VideoCapture("Captured_Video.MP4")    # The name in the "" is the file name tht you wanht to play
while(True):
    ret_, frame = cap.read()
    cv2.imshow("abc", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Here this 'q' is the exit key.
        break
cap.release()
cv2.destroyAllWindows()
