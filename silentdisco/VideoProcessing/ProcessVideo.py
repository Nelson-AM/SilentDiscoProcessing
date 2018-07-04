import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# To make sure any image-related function calls work.
from .ProcessImage import save_image

####################################
#####     VIDEO PROCESSING     #####
####################################


def read_video(vidin):
    """ Reads a video from filepath.
    
    Args:
        vidin:
    Returns:
        Video capture.
    """
    
    # If vidin is not a string, assume it's already a videocapture thing.
    if isinstance(vidin, str):
        vidin = os.path.expanduser(vidin)
        return cv2.VideoCapture(vidin)
    else:
        return vidin


def get_number_frames(vidin):
    """ Returns the number of frames in a video.
    
    Args:
        vidin
    Returns:
    
    """
    
    vidcap = read_video(vidin)
    return int(vidcap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT))


def extract_frame_time(vidin, time):
    """ Time in miliseconds.
    
    Args:
        vidin:
        time:
    Returns:
        image
    """
    
    vidcap = read_video(vidin)
    
    vidcap.set(cv2.cv.CV_CAP_PROP_POS_MSEC, time)
    success, image = vidcap.read()
    
    if success:
        # print time
        return image


def save_frame_time(vidin, time, outdir = None):
    """
    """
    
    image = extract_frame_time(vidin, time)
    
    timestr = str(time)
    
    if outdir:
        save_image(image, timestr, outdir)
    else:
        save_image(vidin, timestr, image)


def extract_frame_frame(vidin, frame):
    """
    """
    
    vidcap = read_video(vidin)
    
    vidcap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, frame)
    success, image = vidcap.read()
    
    if success:
        # print frame
        return image


def save_frame_frame(vidin, frame, outdir = None):
    """
    """
    
    image = extract_frame_frame(vidin, frame)
    
    framestr = str(frame)
    
    if outdir:
        save_image(image, framestr, outdir)
        # save_image(vidin, framestr, image, outdir)
    else:
        save_image(image, framestr)
        # save_image(vidin, framestr, image)


def show_video_HSV(vidin):
    """
    """
    
    vidcap = read_video(vidin)
    
    while(vidcap.isOpened()):
        _, frame = vidcap.read()
        
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
    
    vidcap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    print("Do something")