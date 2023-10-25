import numpy as np
import cv2
import os
import time


cap=cv2.VideoCapture(1)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,639)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)
count=0

#template = cv2.resize(cv2.imread('E:\FYP\Interface(fyp)\Spot(template).jpeg', 0), (0, 0), fx=0.6, fy=0.6)
template_directory="E:\FYP\Template Matching\Spot Dataset"
template_files = [os.path.join(template_directory, filename) for filename in os.listdir(template_directory) if filename.endswith(('.jpg', '.png', '.jpeg'))]

# Initialize an empty list to store template images
templates = []

# Load all template images
for template_file in template_files:
    template = cv2.resize(cv2.imread(template_file,cv2.IMREAD_GRAYSCALE), (0, 0), fx=0.9, fy=0.9)
    if template is not None:
        templates.append(template)
    else:
        print(f"Unable to read template image: {template_file}")
count=0;
while True:
    success,frame=cap.read()
    framer1 = cv2.resize(frame,(0, 0), fx = 0.9, fy = 0.9)
    framer= cv2.cvtColor(framer1, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("Press esc to Exit",framer)
    
    #Converting image into binary
    _, threshold = cv2.threshold(framer, 120, 255, cv2.THRESH_BINARY)
    _, threshold2 = cv2.threshold(template, 140, 255, cv2.THRESH_BINARY)
    
    invert = cv2.bitwise_not(threshold)
    invert2 = cv2.bitwise_not(threshold2)
    h, w = template.shape[::-1]
    #H, W=framer.shape
    #print(H ,W)

    methods = [cv2.TM_CCOEFF_NORMED,
            cv2.TM_CCORR_NORMED]

    for method in methods:
        result = cv2.matchTemplate(invert, template, method)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        print(max_val*100,min_val*100)
        m=round(max_val*100,0)
        loc2 = np.where(result >= 0.7)
        for pt in zip(*loc2[::-1]):
            cv2.rectangle(invert, pt, (pt[0] + w+3, pt[1] + h+2), 255, 0)
            cv2.putText(invert, "X", (pt[0] + w-8, (pt[1] + h) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.3, 255, 1)
            cv2.putText(invert,"Accuracy",(20, 50), 1, 1, (255, 255, 0))
            cv2.putText(invert,"%",(60, 70), 1, 1, (255, 255, 0))
            cv2.putText(invert,str(m),(20, 70), 1, 1, (255, 255, 0))
            cv2.putText(invert,"%",(60, 70), 1, 1, (255, 255, 0))
    hor=np.hstack((framer,invert))
    cv2.imshow('Matching',hor)
    count=0;
    #cv2.imwrite("E:\FYP\Template Matching\DefectDetectionSpot1\defect_detection%d.jpg" % count,hor)
    key=cv2.waitKey(1)
    if key == 27:
        break
    elif key==ord('f'):
        cv2.imwrite("E:\FYP\Template Matching\DefectDetectionSpot1\opencv_frame%d.jpg" % count,hor)
        count += 1

cap.release()
cv2.destroyAllWindows()

#cv2.destroyAllWindows()
