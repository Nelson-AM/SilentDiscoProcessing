# OpticalFlow Lucas-Kanade method

import numpy as np
import cv2
import argparse

# Construct the argument parser and parse the arguments (command line tools).
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "path to the (optional) video file")
args = vars(ap.parse_args())

if not args.get("video", False):
    camera = cv2.VideoCapture(0)
# else, grab a reference to the video file.
else:
    camera = cv2.VideoCapture(args["video"])

# params for Shitomasi corner detection.
feature_params = dict(maxCorners = 100, qualityLevel = 0.3, minDistance = 7, blockSize = 7)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# Parameters for Lucas-Kanade optical flow.
lk_params = dict(winsize = (15, 15), maxLevel = 2,
                 criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Create some random colors.
colors = np.random.randint(0, 255, (100, 3))

# Take the first frame and find corners in it.
ret, old_frame = camera.read()
old_gray = cv2.cvtColor(old_frame, cv2.COLOR_BGR2GRAY)
p0 = cv2.goodFeaturesToTrack(old_gray, mask = None, **feature_params)

# Create a mask image for drawing purposes.
mask = np.zeros_like(old_frame)

while True:
    ret, frame = camera.read()
    frame_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Calculate optical flow.
    p1, st, err = cv2.calcOpticalFlowPyrLK(old_gray, frame_gray, p0) #, None, **lk_params)
    
    # Select good points.
    good_new = p1[st == 1]
    good_old = p0[st == 1]
    
    # Draw the tracks
    for i, (new, old) in enumerate(zip(good_new, good_old)):
        a, b = new.ravel()
        c, d = old.ravel()
        
        mask = cv2.line(mask, (a, b), (c, d), colors[i].tolist(), 2)
        frame = cv2.circle(frame, (a, b), 5, colors[i].tolist(), -1)
    
    img = cv2.add(frame, mask)
    
    cv2.imshow('frame', img)
    key = cv2.waitKey(1) & 0xFF
    
    # If the 'q' key is pressed, stop the loop.
    if key == ord("q"):
        break
    
    # Now update the previous frame and previous points.
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1, 1, 2)

cv2.destroyAllWindows()
camera.release()