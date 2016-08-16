# RGBTracking.py
# Source: http://www.pyimagesearch.com/2015/09/14/ball-tracking-with-opencv/

# Import necessary packages.
from collections import deque
import numpy as np
import argparse
import imutils
import cv2
import csv
import os


def otsu_threshold(imin, gauss = None):
    """
    """
    
    if gauss:
        blurim = cv2.GaussianBlur(imin, (5, 5), 0)
        _, otsuim = cv2.threshold(blurim, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    else:
        _, otsuim = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return otsuim
    

def find_contours_single(imin, maskin = None):
    """ Finds contours on single channel image.
    
    Performs Otsu thresholding, then finds and draws contours.
    """
    
    im = otsu_threshold(imin, "gauss")
    
    if maskin is not None:
        im = cv2.bitwise_and(im, im, mask = maskin)
    
    contours, _ = cv2.findContours(im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    return contours


def find_centres(contours):
    
    centres = []
    
    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) < 5:
            continue
        if cv2.contourArea(contours[i]) > 250:
            continue
        
        moments = cv2.moments(contours[i])
        
        centres.append(
            (int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00'])))
    
    print centres
    return centres


def find_centres_single(imin, maskin = None):
    """
    """
    
    if maskin is not None:
        contours = find_contours_single(imin, maskin)
    else:
        contours = find_contours_single(imin)
    centres = find_centres(contours)
    
    return centres


def show_centres(image, centres, color = None):
    
    if color is None:
        color = (0, 255, 255)
    elif color == 'blue':
        color = (255, 0, 0)
    elif color == 'green':
        color = (0, 255, 0)
    elif color == 'red':
        color = (0, 0, 255)
        
    for i in range(len(centres)):
        cv2.circle(image, centres[i], 5, color, -1)

def save_centres(filename, timepoint, color, centres):
    """ Saves list of centres as >comma separated values<.
    
    Requires input:
    filename
        String of the full filepath.
    timepoint
        Identifier for either time or frame number.
    centres
        List of centres (x, y).
        Need to save the centres as two separate basic columns instead of the current array.
    """
    
    with open(filename, 'ab') as csvfile:
        spamwriter = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
        
        centres_x = [x[0] for x in centres]
        centres_y = [x[1] for x in centres]
        
        for i in range(len(centres)):
            
            row = [timepoint] + [color] + [centres_x[i]] + [centres_y[i]]
            spamwriter.writerow(row)








# Construct the argument parser and parse the arguments (command line tools).
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "path to the (optional) video file")
ap.add_argument("-m", "--mask", help = "path to the (optional) mask file")
args = vars(ap.parse_args())

# If a video path was not supplied, grab the reference to the webcam...
if not args.get("video", False):
    camera = cv2.VideoCapture(0)
# else, grab a reference to the video file.
else:
    camera = cv2.VideoCapture(args["video"])

# Get the mask file.
if args.get("mask", True):
    maskone = cv2.imread(args["mask"], cv2.CV_LOAD_IMAGE_GRAYSCALE)
    # maskone = imutils.resize(maskone, width = 600)

filename = "/Volumes/SAMSUNG/ESCOM/allframes.csv"

# Loop over video file/feed.
while True:
    
    # Grab the current frame.
    (grabbed, frame) = camera.read()
    frameno = camera.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) 
    # If we are viewing a video and we did not grab a frame, then we have reached the end of the video.
    
    if frameno > 1:
        
        if args.get("video") and not grabbed:
            break
        
        if frameno % 10 == 0:
            
            # Function call to get contours and centres per color.
            b, g, r = cv2.split(frame)
            
            b = cv2.dilate(b, None, iterations = 2)
            b = cv2.erode(b, None, iterations = 2)
            g = cv2.dilate(g, None, iterations = 2)
            g = cv2.erode(g, None, iterations = 2)
            r = cv2.dilate(r, None, iterations = 2)
            r = cv2.erode(r, None, iterations = 2)
    
            # Perform Otsu thresholding
            cb = find_centres_single(b, maskone)
            cg = find_centres_single(g, maskone)
            cr = find_centres_single(r, maskone)
    
            # show_centres(frame, cb, 'blue')
            # show_centres(frame, cg, 'green')
            # show_centres(frame, cr, 'red')
    
            # Show the frame and mask to our screen.
            # frame = imutils.resize(frame, width = 600)
    
            # cv2.imshow("Frame", frame)
            key = cv2.waitKey(1) & 0xFF
            
            # If the 'q' key is pressed, stop the loop.
            if key == ord("q"):
                break
            
            save_centres(filename, frameno, 'blue', cb)
            save_centres(filename, frameno, 'red', cr)
            save_centres(filename, frameno, 'green', cg)


# Cleanup the camera and close any open windows.
camera.release()
cv2.destroyAllWindows()

