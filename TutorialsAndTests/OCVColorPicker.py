# OCVColorPicker

#! /usr/bin/env python2

import cv2
import argparse
from operator import xor
import imutils
import numpy as np

colors = []

def on_mouse_click(event, x, y, flags, frame):
    if event == cv2.EVENT_LBUTTONUP:
        colors.append(frame[y,x].tolist())

def get_arguments():
    ap = argparse.ArgumentParser()
    ap.add_argument('-f', '--filter', required=True,
                    help='Range filter. RGB or HSV')
    ap.add_argument('-i', '--image', required=False,
                    help='Path to the image')
    ap.add_argument('-w', '--webcam', required=False,
                    help='Use webcam', action='store_true')
    args = vars(ap.parse_args())

    if not xor(bool(args['image']), bool(args['webcam'])):
        ap.error("Please specify only one image source")

    if not args['filter'].upper() in ['RGB', 'HSV']:
        ap.error("Please speciy a correct filter.")

    return args

def main():
    
    args = get_arguments()

    range_filter = args['filter'].upper()

    if args['image']:
        frame = cv2.imread(args['image'])
        
        frame = imutils.resize(frame, width = 1200)

        if range_filter == 'RGB':
            frame = image.copy()
        else:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # else:
        # capture = cv2.VideoCapture(0)

    while True:
        # if args['webcam'] or not args['image']:
        #    _, frame = capture.read()
        hsv = frame
        # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HLS_FULL)
        if colors:
            cv2.putText(hsv, str(colors[-1]), (10, 50), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2)
        cv2.imshow('frame', hsv)
        cv2.setMouseCallback('frame', on_mouse_click, hsv)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    # capture.release()
    cv2.destroyAllWindows()

    # avgb = int(sum(c[0] for c in colors) / len(colors))
    # avgg = int(sum(c[0] for c in colors) / len(colors))
    # avgr = int(sum(c[0] for c in colors) / len(colors))
    # print avgb, avgg, avgr
    
    minb = min(c[0] for c in colors)
    ming = min(c[1] for c in colors)
    minr = min(c[2] for c in colors)
    maxb = max(c[0] for c in colors)
    maxg = max(c[1] for c in colors)
    maxr = max(c[2] for c in colors)
    print minr, ming, minb, maxr, maxg, maxb

    lb = [minb,ming,minr]
    ub = [maxb,maxg,maxr]
    print lb, ub

if __name__ == "__main__":
    main()