import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# class ProcessVideo:

class ProcessVideo:
    
    def __init__(self):
        self.data = []
    
    def read_video(self, vidin):
        """ 
        """
        vidin = os.path.expanduser(vidin)
        return cv2.VideoCapture(vidin)
    
    def save_image(self, imin, imnames, images):
        """ Saves image to same path as original, with added string contained 
        in imname.
        
        To-do:
        - Generalize so images are saved with the same extension as original.
        """
        
        imin = os.path.expanduser(imin)
        
        for imname, image in zip(imnames, images):
            cv2.imwrite(imin[:-4] + '_' + imname + '.png', image)
    
    def show_image(self, imin):
        """ Displays image using matplotlib.
        
        Assumes colour images are read using cv2, transforms the colourspace from BGR to RGB.
        """
        
        if len(imin.shape) == 3:
            imin = imin[:, :, ::-1]
            plt.imshow(imin)
        else:
            plt.imshow(imin, cmap = 'gray', interpolation = 'bicubic')
        
        # Hide tick values on X and Y axes.
        plt.xticks([]), plt.yticks([])
        plt.show()
    
    def process_video(self, vidin):
        
        cap = self.read_video(vidin)
        # cv2.VideoCapture("./out.mp4")
        
        while not cap.isOpened():
            cap = self.read_video(vidin)
            # cap = cv2.VideoCapture("./out.mp4")
            
            cv2.waitKey(1000)
            print "Wait for the header"
            
            pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
            
            while True:
                flag, frame = cap.read()
                
                if flag:
                    
                    # The frame is ready and already captured
                    self.show_image(frame)
                    # cv2.imshow('video', frame)
                    pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
                    print str(pos_frame) + " frames"
                    
                else:
                    
                    # The next frame is not ready, so we try to read it again.
                    cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame - 1)
                    print "Frame is not ready"
                    
                    # It is better to wait a while for the next frame to be ready.
                    cv2.waitKey(1000)
                    
                    if cv2.waitKey(10) == 27:
                        break
                    
                    if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
                        # If the number of captured frames is equal to the total number of frames, we stop.
                        break
    
    def ProcessVideoPerSec(self, vidin):
        
        vidcap = self.read_video(vidin)
        
        # Cue to 20 sec. position
        vidcap.set(0, 20000)
        success, image = vidcap.read()
        
        if success:
            # save frame as PNG
            imnames = ['20sec']
            images = [image]
            
            self.save_image(vidin, imnames, images)
            # cv2.imwrite("frame20sec.jpg", image)
            
            self.show_image(image)

session = ProcessVideo()

session.ProcessVideoPerSec('~/Documents/PYTHON/SilentDiscoData/TX-BACK_UP_21_120-130.mov')
# session.read_video('~/Documents/PYTHON/SilentDiscoData/TX-BACK_UP_10s.mov')


