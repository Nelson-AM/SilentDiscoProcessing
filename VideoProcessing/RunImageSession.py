import random

# RunImageSession.py

from ProcessImage import *

image_1 = '/Volumes/SAMSUNG/ESCOM/Frames/TX-BACK UP_21_1.png'
mask = '/Volumes/SAMSUNG/ESCOM/TX_MASK_detailed_2.png'

for i in range(10):
    rng = random.randint(1, 3229)
    
    image = '/Volumes/SAMSUNG/ESCOM/Frames/TX-BACK UP_21_' + str(rng) + '.png'
    print image

    find_contours_multi(image, mask)