# ObjectMovement


# Import necessary packages.
from collections import deque
import numpy as np
import argparse
import imutils
import cv2


# Construct argument parser and parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "Path to the optional video file.")
ap.add_argument("-b", "--buffer", type = int, default = 32, help = "Max buffer size.")
args = vars(ap.parse_args())


# Define lower and upper boundaries of the "green" ball in the HSV color space.
greenLower = (29, 86, 6)
greenUpper = (64, 255, 255)

# redLower = (0, 0, 0)
# redUpper = (255, 255, 255)
# blueLower = (0, 0, 0)
# blueUpper = (255, 255, 255)


# Initialize the list of tracked points, the frame counter, and the coordinate deltas.
pts = deque(maxlen = args["buffer"])
counter = 0
(dX, dY) = (0, 0)
direction = ""


# If a video path was not supplied, grab the reference to the webcam...
if not args.get("video", False):
    camera = cv2.VideoCapture(0)
# ... otherwise, grab a reference to the video file.
else:
    camera = cv2.VideoCapture(args["video"])


# Loop!
while True:
    # Grab the current frame.
    (grabbed, frame) = camera.read()
    
    
    # If we are viewing a video and we did not grab a frame, then we have reached the end of the video.
    if args.get("video") and not grabbed:
        break
    
    
    # Resize the frame, blur it, and convert it to HSV color space.
    frame = imutils.resize(frame, width = 600)
    blurred = cv2.GaussianBlur(frame, (11, 11), 0)
    hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
    
    
    # Construct a mask for the color "green", then perform a series of dilations and erosions to remove any small blobs left in the mask.
    mask = cv2.inRange(hsv, greenLower, greenUpper)
    mask = cv2.erode(mask, None, iterations = 2)
    mask = cv2.dilate(mask, None, iterations = 2)
    
    
    # Find contours in the mask and initialize the current (x, y) center of the ball.
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]
    center = None
    
    
    # Only proceed if at least one contour was found.
    if len(cnts) > 0:
        # Find the largest contour in the mask, then use it to compute the minimum enclosing circle and the centroid.
        c = max(cnts, key = cv2.contourArea)
        ((x, y), radius) = cv2.minEnclosingCircle(c)
        M = cv2.moments(c)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
        
        
        # Only proceed if the radius meets a minimum size.
        if radius > 10:
            # Draw the circle and centroid on the frame, then update the list of tracked points.
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)
            pts.appendleft(center)
            
    
    # Loop over the set of tracked points.
    for i in np.arange(1, len(pts)):
        # If either of the tracked points are None, ignore them.
        if pts[i - 1] is None or pts[i] is None:
            continue
        
        
        # Check to see if enough points are accumulated in the buffer.
        if counter >= 10 and i == 1 and pts[-10] is not None:
            # Compute the difference between the x and y coordinates and re-initialize the direction text variables.
            dX = pts[-10][0] - pts[i][0]
            dY = pts[-10][1] - pts[i][1]
            (dirX, dirY) = ("", "")
            
            
            # Ensure there is significant movement in the x-direction.
            if np.abs(dX) > 20:
                dirX = "East" if np.sign(dX) == 1 else "West"
            if np.abs(dY) > 20:
                dirX = "North" if np.sign(dY) == 1 else "South"
            
            
            # Handle when both directions are non-empty...
            if dirX != "" and dirY != "":
                direction = "{}-{}".format(dirY, dirX)
            # ... otherwise only one direction is non-empty.
            else:
                direction = dirX if dirX != "" else dirY
            
            
        # Otherwise compute the thickness of the line and draw the connecting lines.
        thickness = int(np.sqrt(args["buffer"] / float(i + 1)) * 2.5)
        cv2.line(frame, pts[i - 1], pts[i], (0, 0, 255), thickness)
        
    # Show the movement deltas and the direction of movement on the frame.
    cv2.putText(frame, direction, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.65, (0, 0, 255), 3)
    cv2.putText(frame, "dx: {}, dy: {}".format(dX, dY), (10, frame.shape[0] - 10),
                dv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)
    
    
    # Show the frame to our screen and increment the frame counter.
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1) & 0xFF
    counter += 1
    
    
    # If the 'q' key is pressed, stop the loop.
    if key == ord("q"):
        break

# Cleanup the camera and close all windows.
camera.release()
cv2.destroyAllWindows()