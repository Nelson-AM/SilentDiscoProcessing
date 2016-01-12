"""
objectTrackingTutorial.cpp

Written by  Kyle Hounslow 2013

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
associated documentation files (the "Software"), to deal in the Software without restriction, 
including without limitation the rights to use, copy, modify, merge, publish, distribute, 
sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is 
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or 
substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT 
NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND 
NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, 
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, 
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import cv2

# Dummy variables, need to softcode.
# FRAME_HEIGHT = 250
# FRAME_WIDTH = 250

# default capture width and height
# const int FRAME_WIDTH = 640;
# const int FRAME_HEIGHT = 480;

# Max number of objects to be detected in frame.
MAX_NUM_OBJECTS = 50

# Minimum and maximum object area. Take frame height and width from images as they're read.
MIN_OBJECT_AREA = 20 * 20
MAX_OBJECT_AREA = FRAME_HEIGHT * FRAME_WIDTH / 1.5;

# names that will appear at the top of each window
windowName = "Original Image"
windowName1 = "HSV Image"
windowName2 = "Thresholded Image"
windowName3 = "After Morphological Operations"



# string intToString(int number){
#	std::stringstream ss;
#	ss << number;
#	return ss.str();
# }

def on_trackbar():
    # This function gets called whenever a trackbar position is changed.
    pass

trackbarWindowName = "Trackbars"

def createTrackbars():
    
    cv2.namedWindow(trackbarWindowName, 0)

    # initial min and max HSV filter values. These will be changed using trackbars.
    H_MIN = 0
    H_MAX = 256
    S_MIN = 0
    S_MAX = 256
    V_MIN = 0
    V_MAX = 256
    
	# Create trackbars and insert them into window.
    # 3 parameters are: the address of the variable that is changing when the trackbar is moved(eg.H_LOW), the max value the trackbar can move (eg. H_HIGH), and the function that is called whenever the trackbar is moved(eg. on_trackbar)
    cv2.createTrackbar("H_MIN", trackbarWindowName, H_MIN, H_MAX, on_trackbar);
    cv2.createTrackbar("H_MAX", trackbarWindowName, H_MAX, H_MAX, on_trackbar);
    cv2.createTrackbar("S_MIN", trackbarWindowName, S_MIN, S_MAX, on_trackbar);
    cv2.createTrackbar("S_MAX", trackbarWindowName, S_MAX, S_MAX, on_trackbar);
    cv2.createTrackbar("V_MIN", trackbarWindowName, V_MIN, V_MAX, on_trackbar);
    cv2.createTrackbar("V_MAX", trackbarWindowName, V_MAX, V_MAX, on_trackbar);

def drawObject(x, y, frame):
    
    cv2.circle(frame, (x, y), 20, (0, 255, 0), 2)
    
    if (y - 25) > 0:
        line(frame, (x, y), (x, y - 25), (0, 255, 0), 2)
    else:
        line(frame, (x, y), (x, 0), (0, 255, 0), 2)
    
    if (y + 25) < FRAME_HEIGHT:
        line(frame, (x, y), (x, y + 25), (0, 255, 0), 2)
    else:
        line(frame, (x, y), (x, FRAME_HEIGHT), (0, 255, 0), 2)
    
    if (x - 25) > 0:
        line(frame, (x, y), (x - 25, y), (0, 255, 0), 2)
    else:
        line(frame, (x, y), (0, y), (0, 255, 0), 2)
    
    if (x + 25) < FRAME_WIDTH:
        line(frame, (x, y), (x + 25, y), (0, 255, 0), 2)
    else:
        line(frame, (x, y), (FRAME_WIDTH, y), (0, 255, 0), 2)
    
    cv2.putText(frame, str(x) + ', ', str(y), (x, y + 30), 1, 1, (0, 255, 0), 2)

def morphOps(thresh):
    
    erodeElement = cv2.getStructuringElement(MORPH_RECT, (3, 3))
    dilateElement = cv2.getStructuringElement(MORPH_RECT, (8, 8))
    
    erode(thresh, thresh, erodeElement)
    erode(thresh, thresh, erodeElement)
    
    dilate(thresh, thresh, dilateElement)
    dilate(thresh, thresh, dilateElement)
    
def trackFilteredObject(x, y, threshold, cameraFeed):
    
    cv2.findContours(temp, contours, hierarchy, CV_RETR_CCOMP, CV_CHAIN_APPROX_SIMPLE)
    
    refArea = 0
    
    objectFound = False
    
    if hierarchy.size() > 0:
        numObjects = hierarchy.size()
        
        if numObjects > MAX_NUM_OBJECTS:
            for i in len(hierarchy):
                
                moment = cv2.moments(contours)
                area = moment.m00
                
                # If the area is less than 20px by 20px then it's probably just noise.
                # If the area is the same as the 3/2 of the image size, probably just a bad filter.
                # We only want the object with the largest area so we save a reference area each iteration and compare it to the area in the next iteration.
                if area > MIN_OBJECT_AREA and area < MAX_OBJECT_AREA and area > refArea:
                    x = moment.m10 / area
                    y = moment.m01 / area
                    objectFound = True
                    refArea = area
                else:
                    objectFound = False
            
            # Let user know we found an object.
            if objectFound:
				putText(cameraFeed,"Tracking Object",Point(0,50),2,1,Scalar(0,255,0),2);
				# draw object location on screen
				drawObject(x,y,cameraFeed)
            
        else:
            putText(cameraFeed,"TOO MUCH NOISE! ADJUST FILTER",Point(0,50),1,2,Scalar(0,0,255),2);

def RunSession():
    
    # Some boolean variables for different functionality within this program.
    trackObjects = False
    useMorphOps = False
    
    # Matrix to store each frame of the feed (or video file).
    # cameraFeed

    # Matrix storage for HSV image.
    # HSV

    # Matrix storage for binary threshold image.
    # threshold

    # x and y values for object location
    x = 0
    y = 0

    # Create slider bars for HSV filtering
    createTrackbars()

    # Video capture object to acquire webcam feed (or video file).
    capture = cv2.VideoCapture("~/Documents/PYTHON/SilentDiscoData/TX-BACK_UP_10s.mov")
    # VideoCapture capture
    
    # Open capture object at location 0.
    # capture.open(0)

    # Set height and width of capture frame.
    capture.set(CV_CAP_PROP_FRAME_WIDTH, FRAME_WIDTH)
    capture.set(CV_CAP_PROP_FRAME_HEIGHT, FRAME_HEIGHT)
    
    while(1):
        # Store image to matrix
        # capture.read(cameraFeed)
        
        # Convert frame from BGR to HSV colorspace
        HSV = cv2.cvtColor(cameraFeed, COLOR_BGR2HSV)
        
        # Filter HSV image between values and store filtered image to threshold matrix
        tohreshold = cv2.inRange(HSV, (H_MIN, S_MIN, V_MIN), (H_MAX, S_MAX, V_MAX))
        
        # Perform morphological operations on thresholded image to eliminate noise and emphasize the filtered object(s)
        if useMorphOps:
            morphOps(threshold)
        
        # Pass in thresholded frame to our object tracking function. This function will return the x and y coordinates of the filtered object.
        if trackObjects:
            trackFilteredObject(x, y, threshold, cameraFeed)
            
            # Show frames
            cv2.imshow(windowName2, threshold)
            cv2.imshow(windowName, cameraFeed)
            cv2.imshow(windowName1, HSV)
            
            # Delay 30ms so that screen can refresh. Image will not appear without the waitkey command.
        
        waitKey(30)
    
    
    return 0

RunSession()
# createTrackbars()