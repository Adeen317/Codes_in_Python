#object detection
import cv2
import numpy as np

cap= cv2.VideoCapture(0)

while True:
    _,frame = cap.read()
    #belt
    belt = frame[300: 427, 237: 380]
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, threshold = cv2.threshold(gray_frame, 100, 255, cv2.THRESH_BINARY)

    #Detect
    contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        cv2.polylines(frame,[cnt],True,(255,0,0,0),2)
        (x, y, w, h) = cv2.boundingRect(cnt)
        area = cv2.contourArea(cnt)
        if area > 400:
            cv2.rectangle(gray_frame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        elif 100 < area < 400:
            cv2.rectangle(gray_frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv2.putText(gray_frame, str(area), (x, y), 1, 1, (0, 255, 0))

    
    cv2.imshow("Frame",frame)
    cv2.imshow("belt",belt)
    cv2.imshow("Frame gray",gray_frame)
    cv2.imshow("Threshold",threshold)
    
 
    key= waitKey(1)
    if key == 27:
        break

    cap.release()
    cv2.destroyAllWindows()
