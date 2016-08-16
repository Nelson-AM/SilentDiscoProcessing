"""
ProcessFile. Processes a video file to get centroids of headphone lights.

Processes a video file and goes through the following steps:
- Extracts frames at a given sampling rate
    - Frames are saved separately
- Image frames are processed
    - Colour layers are separated
    - Otsu thresholding is performed
    - Image moments and centroids are determined

GENERAL TO-DO:
- Integrate video and image processing
    - Save extracted frames to drive
    - Keep frame in memory, get centroids &c.
- Save centroids information
    - Flat array containing the following columns:
        - Timestamp (same as image ID)
        - X and Y coordinates
        - Centroid color
    - One entry per centroid makes the entire thing easier, as not all frames will contain the 
      same amount of centroids.
"""

import os
import cv2
import numpy as np
from matplotlib import pyplot as plt


from ProcessImage import *
from ProcessVideo import *

testframe = "~/Documents/PYTHON/SilentDiscoData/Frames/TX-BACK UP_21_0.png"
show_image(testframe)

