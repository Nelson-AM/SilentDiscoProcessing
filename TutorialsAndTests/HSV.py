import cv2
import os

def on_trackbar():
    # This function gets called whenever a trackbar position is changed.
    pass

trackbarWindowName = "Trackbars"

def createTrackbars(trackbarWindowName):
    
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

def runSession(vidin):
    
    vidin = os.path.expanduser(vidin)
    
    capture = cv2.VideoCapture(vidin)
    
    while(capture.isOpened()):
        ret, frame = capture.read()
        
        # capture.set(3, 640)
        # capture.set(4, 480)

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        cv2.namedWindow("", cv2.WINDOW_NORMAL)
        cv2.imshow('frame', gray)
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    capture.release()
    cv2.destroyAllWindows()
    
    # trackbarWindowName = "Trackbars"
    
    # createTrackbars(trackbarWindowName)

runSession("~/Documents/PYTHON/SilentDiscoData/TX-BACK_UP_10s.mov")