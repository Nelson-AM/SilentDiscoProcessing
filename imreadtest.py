import cv2
import numpy as np

"""
To-do list for data point extraction.

- Separate image into respective RGB layers.
- For R and G:
    - Threshold and binarize images.
"""

img = cv2.imread("ScreenShot.png")
b, g, r = cv2.split(img)

print cv2.minMaxLoc(g)
print cv2.minMaxLoc(r)

# cv2.imwrite('ScreenShotG.png', g)
# cv2.imwrite('ScreenShotR.png', r)