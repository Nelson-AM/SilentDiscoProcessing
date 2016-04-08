# BallTracking.py
# Source: http://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

# Import necessary packages.
from collections import deque
import numpy as np
import argparse
import imutils
import cv2


# Construct the argument parser and parse the arguments (command line tools).
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "path to the (optional) video file")
ap.add_argument("-b", "--buffer", type = int, default = 64, help = "max buffer size")
args = vars(ap.parse_args())


# Define the lower and upper boundaries of the "green" ball in the HSV color space, then initalize the list of tracked points.
# NOTE: values detected using the range-detector script in the imutils package.  Function can get thresholds for both HSV and RGB color spaces.

# (48, 26, 10)
# (62, 255, 139)
# greenLower = (50, 76, 38)
# greenUpper = (58, 255, 172)

# NOTE: lower and upper bounds for red, based on frame #6000:
# redLower = (167, 0, 27)
# redUpper = (190, 255, 255)
# NOTE: lower and upper bounds for green, based on frame #6000:
greenLower = (50, 76, 38)
greenUpper = (58, 255, 172)

pts = deque(maxlen = args["buffer"])


# If a video path was not supplied, grab the reference to the webcam...
if not args.get("video", False):
    camera = cv2.VideoCapture(0)
# else, grab a reference to the video file.
else:
    camera = cv2.VideoCapture(args["video"])


# Loop over video file/feed.
while True:
    # Grab the current frame.
    (grabbed, frame) = camera.read()
    
    
    # If we are viewing a video and we did not grab a frame, then we have reached the end of the video.
    if args.get("video") and not grabbed:
        break
    
    
    # Resize the frame, blur it, and convert to HSV color space.
    # NOTE: resizing the frame leads to faster image processing because there is less frame data to process, however in the silent disco case this might lead to data loss.  Also we don't care /that/ much about speed of processing at this time.
    frame = imutils.resize(frame, width = 600)
    # blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    
    # Construct a mask for the color "green", then perform a series of dilations and erosions to remove any small blobs left in the mask.
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    # mask = cv2.inRange(hsv, redLower, redUpper)
    mask = cv2.dilate(mask, None, iterations = 2)
    mask = cv2.erode(mask, None, iterations = 2)
    
    
    cv2.imshow("mask", mask)
    
    # Find contours in the mask and initialize the current (x, y) center of the ball.
    # NOTE: the slice of [-2] is necessary to make findContours compatible with OpenCV 3.
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    
    
    # Only proceed if at least one contour was found.
    if len(cnts) > 0:
        # Find the largest contour in the mask, then use it to compute the minimum enclosing circle and centroid.
        # NOTE: needs adaptation because we're not interested in the minimum enclosing circle.
        # NOTE: and we want to find multiple contours, not just the biggest one.  Basically we want to do this for ALL contours.
        for i in range(len(cnts)):
            M = cv2.moments(cnts[i])
            if cv2.contourArea(cnts[i]) > 3 and cv2.contourArea(cnts[i]) < 150:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        
        
        # c = max(cnts, key = cv2.contourArea)
        # ((x, y), radius) = cv2.minEnclosingCircle(c)
        # M = cv2.moments(c)
        # center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        
        
            # Only proceed if the radius meets a minimum size.
            # if radius > 10:
            # if cv2.contourArea(cnts[i]) > 5 and cv2.contourArea(cnts[i]) < 250:
                # Draw the circle and centroid of the frame, then update the list of tracked points.
                # NOTE: how about instead I draw the contour and the centroid?
                # cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
                cv2.circle(frame, center, 5, (0, 255, 255), -1)
    
    # Update the points queue.
    pts.appendleft(center)
    
    
    # Loop over the set of tracked points.
    for i in xrange(1, len(pts)):
        # If either of the tracked points are None, ignore them.
        if pts[i - 1] is None or pts[i] is None:
            continue
        
        # NOTE:
        # if pnts[i] is close enough in value to pnts[i - 1]:
            # draw a line between pnts[i]
        # Otherwise compute the thickness of the line and draw the connecting lines.
        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
        # cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
    
    
    # Show the frame to our screen.
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    
    
    # If the 'q' key is pressed, stop the loop.
    if key == ord("q"):
        break


# Cleanup the camera and close any open windows.
camera.release()
cv2.destroyAllWindows()