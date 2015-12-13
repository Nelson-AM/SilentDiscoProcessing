import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('ScreenShotG.png', 0)
ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

titles = ['Original image', 'BINARY',
          'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]

for i in xrange(6):
    plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()

cv2.imwrite('simple_thresh_binary.png', thresh1)
cv2.imwrite('simple_thresh_binary_inv.png', thresh2)
cv2.imwrite('simple_thresh_trunc.png', thresh3)
cv2.imwrite('simple_thresh_tozero.png', thresh4)
cv2.imwrite('simple_thresh_tozero_inv.png', thresh5)
