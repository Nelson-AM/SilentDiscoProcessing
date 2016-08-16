# contours.py

import numpy as np
import cv2

# Read image, convert to grayscale, find contours.
im = cv2.imread('test.jpg')
imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cnt = contours[0]
print len(cnt)

for h, cnt in enumerate(contours):
    mask = np.zeros(imgray.shape, np.uint8)
    cv2.drawContours(mask, [cnt], 0, 255, -1)
    mean = cv2.mean(im, mask = mask)
