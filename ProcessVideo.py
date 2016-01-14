import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# To make sure any image-related function calls work.
from ProcessImage import *

####################################
#####     VIDEO PROCESSING     #####
####################################


def read_video(vidin):
    """
    """
    
    vidin = os.path.expanduser(vidin)
    return cv2.VideoCapture(vidin)

def process_video_time(vidin, time, outdir):
    """
    """

    vidcap = read_video(vidin)

    # Cue to 20 sec. position, not sure what 0 does here.
    # Something related to CV_CAP_PROP_POS_MSEC probably?
    # vidcap.set(0, time)
    vidcap.set(cv2.cv.CV_CAP_PROP_POS_MSEC, time)
    success, image = vidcap.read()
    
    if success:
        print time
        save_image(vidin, time, image)


def process_video_frame(vidin, frame, outdir):
    """
    """
    
    vidcap = read_video(vidin)
    
    vidcap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, frame)
    success, image = vidcap.read()
    
    if success:
        print frame
        save_image(vidin, frame, image)


def show_video_HSV(vidin):
    """
    """
    
    vidcap = read_video(vidin)
    
    while(vidcap.isOpened()):
        ret, frame = vidcap.read()
        
        frame = cv2.resize(frame, 
                           (0, 0), 
                           fx = 0.5, 
                           fy = 0.5, 
                           interpolation = cv2.INTER_CUBIC)
        
        hsv_vid = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        cv2.namedWindow("", cv2.WINDOW_NORMAL)
        cv2.imshow("frame", hsv_vid)
        
        if cv2.waitKey(12) & 0xFF == ord('q'):
            break
    
    capture.release()
    cv2.destroyAllWindows()