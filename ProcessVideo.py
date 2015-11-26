import os
import cv2
import numpy as np
from matplotlib import pyplot as plt

# class ProcessVideo:

def ProcessVideo(vid):
    
    cap = cv2.VideoCapture("./out.mp4")
    while not cap.isOpened():
        cap = cv2.VideoCapture("./out.mp4")
        cv2.waitKey(1000)
        print "Wait for the header"

        pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
        while True:
            flag, frame = cap.read()
            if flag:
            
                # The frame is ready and already captured
                cv2.imshow('video', frame)
                pos_frame = cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES)
                print str(pos_frame) + " frames"
            
            else:
            
                # The next frame is not ready, so we try to read it again
                cap.set(cv2.cv.CV_CAP_PROP_POS_FRAMES, pos_frame-1)
                print "frame is not ready"
            
                # It is better to wait for a while for the next frame to be ready
                cv2.waitKey(1000)

                if cv2.waitKey(10) == 27:
                    break
            
                if cap.get(cv2.cv.CV_CAP_PROP_POS_FRAMES) == cap.get(cv2.cv.CV_CAP_PROP_FRAME_COUNT):
                    # If the number of captured frames is equal to the total number of frames, we stop
                    break

def ProcessVideoPerSec(vid):

    vidcap = cv2.VideoCapture('d:/video/keep/Le Sang Des Betes.mp4')
    vidcap.set(cv2.CAP_PROP_POS_MSEC, 20000)      # just cue to 20 sec. position
    success,image = vidcap.read()
    if success:
        cv2.imwrite("frame20sec.jpg", image)     # save frame as JPEG file
        cv2.imshow("20sec",image)
        cv2.waitKey()
        
# c++ example
#include "opencv2/opencv.hpp"

def ProcessVideoFromC:
    """
    
    using namespace cv;
    
    int main(int, char**)
    {
        VideoCapture cap(0); // open the default camera
        if(!cap.isOpened())  // check if we succeeded
            return -1;
        
        Mat edges;
        namedWindow("edges",1);
        for(;;)
        {
            Mat frame;
            cap >> frame; // get a new frame from camera
            cvtColor(frame, edges, CV_BGR2GRAY);
            GaussianBlur(edges, edges, Size(7,7), 1.5, 1.5);
            Canny(edges, edges, 0, 30, 3);
            imshow("edges", edges);
            if(waitKey(30) >= 0) break;
        }
        // the camera will be deinitialized automatically in VideoCapture destructor
        return 0;
    }
    """