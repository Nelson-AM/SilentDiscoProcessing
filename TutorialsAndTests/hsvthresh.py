import cv2
import numpy as np
import os

vid = "~/Documents/PYTHON/SilentDiscoData/TX-BACK_UP_10s.mov"
vid = os.path.expanduser(vid)
cap = cv2.VideoCapture(vid)

def nothing(x):
    pass

# Creating a window for later use
cv2.namedWindow('result')

# Starting with 100's to prevent error while masking
h_min, s_min, v_min = 0, 0, 0
h_max, s_max, v_max = 256, 256, 256

# Creating track bar
cv2.createTrackbar('h_min', 'result', 0, 256, nothing)
cv2.createTrackbar('h_max', 'result', 256, 256, nothing)
cv2.createTrackbar('s_min', 'result', 0, 256, nothing)
cv2.createTrackbar('s_max', 'result', 256, 256, nothing)
cv2.createTrackbar('v_min', 'result', 0, 256, nothing)
cv2.createTrackbar('v_max', 'result', 256, 256, nothing)

while(1):

    _, frame = cap.read()

    frame = cv2.resize(frame, (0, 0), fx = 0.5, fy = 0.5, interpolation = cv2.INTER_CUBIC)
    
    #converting to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # get info from track bar and appy to result
    h_min = cv2.getTrackbarPos('h_min', 'result')
    h_max = cv2.getTrackbarPos('h_max', 'result')
    s_min = cv2.getTrackbarPos('s_min', 'result')
    s_max = cv2.getTrackbarPos('s_max', 'result')
    v_min = cv2.getTrackbarPos('v_min', 'result')
    v_max = cv2.getTrackbarPos('v_max', 'result')

    # Normal masking algorithm
    # lower_blue = np.array([h,s,v])
    # upper_blue = np.array([180, 255, 255])

    mask = cv2.inRange(hsv, (h_min, s_min, v_min), (h_max, s_max, v_max))
    # mask = cv2.inRange(hsv, lower_blue, upper_blue)

    result = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(50) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()