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

####################################
#####     VIDEO PROCESSING     #####
####################################


def read_video(vidin):
    """
    """
    vidin = os.path.expanduser(vidin)
    return cv2.VideoCapture(vidin)


def process_video_time(vidin, time, outdir):
    """
    """

    vidcap = read_video(vidin)

    # Cue to 20 sec. position, not sure what 0 does here.
    # Something related to CV_CAP_PROP_POS_MSEC probably?
    # vidcap.set(0, time)
    vidcap.set(cv2.cv.CV_CAP_PROP_POS_MSEC, time)
    success, image = vidcap.read()

    if success:

        print time

        # save frame as PNG
        imnames = [time]
        images = [image]

        save_image(vidin, imnames, images)

    # self.show_image(image)


####################################
#####     IMAGE PROCESSING     #####
####################################

def read_image(imin, colourspace):
    """ Takes filename and colourspace to read image.
    
    Colourspace takes the cv2.imread flags, being:
    - cv2.IMREAD_COLOR
        Loads a color image. Any transparency of image will be neglected.
        It is the default flag.
    - cv2.IMREAD_GRAYSCALE
        Loads image in grayscale mode
    - cv2.IMREAD_UNCHANGED
        Loads image as such including alpha channel
    """

    imin = os.path.expanduser(imin)
    return cv2.imread(imin, colourspace)

def save_image(imin, imnames, images, imdir = None):
    """ Saves image to the same directory as original with string appended to end of name.
    
    imin = original file path, ? NO FULL STOPS ?
    imnames = string to append to image
    images = image file
    imdir = alternative directory, ? FULL PATH ? (optional)
    """
    
    imin = os.path.expanduser(imin)
    
    if imdir:
        # print 'imdir is present'
        # print imdir
        
        imdir = os.path.expanduser(imdir)
        
        # Splitting image name at the last occurence of "." and at the last "/" for filename.
        splitname = imin.rsplit('.', 1)[0]
        splitname = splitname.rsplit('/', 1)[1]
        splitext = imin.rsplit('.', 1)[1]
        
        print splitname
        print splitext
        
        
        for imname, image in zip(imnames, images):
            print imdir + splitname +  '_' + imname + '.' + splitext
            cv2.imwrite(imdir + splitname + '_' + imname + '.' + splitext, image)
    
    else:
        # print 'imdir is empty'
        
        # Splitting image name at the last occurence of ".".
        splitname = imin.rsplit('.', 1)[0]
        splitext = imin.rsplit('.', 1)[1]
        
        for imname, image in zip(imnames, images):
            cv2.imwrite(splitname + '_' + imname + '.' + splitext, image)
        
    # cv2.imwrite(imin[:-4] + '_' + imname + '.png', image)
    
def show_image(imin):
    """ Displays image using matplotlib.
    
    Assumes colour images are read using cv2, transforms the colourspace from BGR to RGB.
    """

    if len(imin.shape) == 3:
        imin = imin[:, :, ::-1]
        plt.imshow(imin)
    else:
        plt.imshow(imin, cmap='gray', interpolation='bicubic')

    # Hide tick values on X and Y axes.
    plt.xticks([]), plt.yticks([])
    plt.show()


def separate_colors(self, imin):
    """ Takes a colour image and separates the colour layers.
    """

    # Grayscale versus color image loading for debugging purposes.
    # img = self.read_image(imin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    img = read_image(imin, cv2.CV_LOAD_IMAGE_COLOR)
    b, g, r = cv2.split(img)

    # Display image for debugging purposes.
    # self.show_image(img)

    imnames = ['b', 'g', 'r']
    images = [b, g, r]

    save_image(imin, imnames, images)

    return b, g, r


def simple_threshold(imin):
    """ Take an image and creates three binarized versions of it using simple thresholding.
    """

    img = read_image(imin, cv2.CV_LOAD_IMAGE_GRAYSCALE)

    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    imnames = ['simple_binary', 'simple_binary_inv', 'simple_trunc',
               'simple_tozero', 'simple_tozero_inv']
    images = [thresh1, thresh2, thresh3,
              thresh4, thresh5]

    save_image(imin, imnames, images)


def adaptive_threshold(imin):
    """ Takes an image and creates three binarized versions of it using adaptive thresholding.
    """

    img = read_image(imin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    img = cv2.medianBlur(img, 5)

    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 11, 12)  # 50 - 100
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 11, 12)  # 50 - 100

    imnames = ['adaptive_global', 'adaptive_mean', 'adaptive_gaussian']
    images = [th1, th2, th3]

    save_image(imin, imnames, images)


def otsu_threshold(imin):
    """ Takes an image and creates binarised versions using Otsu thresholding.
    """

    img = read_image(imin, cv2.CV_LOAD_IMAGE_GRAYSCALE)

    # Global thresholding
    ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    # Otsu's thresholding
    ret2, th2 = cv2.threshold(
        img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    # Otsu's thresholding after Gaussian filtering
    blur = cv2.GaussianBlur(img, (5, 5), 0)
    ret3, th3 = cv2.threshold(
        blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    imnames = ['noisy', 'global_v_127', 'otsu',
               'gaussian_filtered', 'otsu_gaussian']
    images = [img, th1, th2, blur, th3]

    save_image(imin, imnames, images)


def find_contours(imin, maskin = None):
    """
    """
    
    im = read_image(imin, cv2.IMREAD_COLOR)
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    if maskin:
        mask = read_image(maskin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        imgray = cv2.bitwise_and(imgray, imgray, mask = mask)

    contours, _ = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contoursim = cv2.drawContours(im, contours, -1, (0, 0, 255), 2)

    return (contours, contoursim)


def find_centres(imin, maskin = None):
    """
    """
    
    contours, contoursim = find_contours(imin)
    im = read_image(imin, cv2.IMREAD_COLOR)
    
    if maskin:
        mask = read_image(maskin, cv2.IMREAD_GRAYSCALE)
        im = cv2.bitwise_and(imgray, imgray, mask = mask)
    
    # imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    print 'contours has length: '
    print len(contours)

    centres = []

    for i in range(len(contours)):
        # To-do: soft-code these limits.
        if cv2.contourArea(contours[i]) < 5:
            continue
        if cv2.contourArea(contours[i]) > 250:
            continue

        moments = cv2.moments(contours[i])
        print "i is:"
        print i
        print "moments:"
        print moments

        centres.append(
            (int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00'])))
        cv2.circle(im, centres[-1], 5, (0, 255, 0), -1)

    print centres
    
    if maskin:
        save_image(imin, ['centroids_masked'], [im])
    else:
        save_image(imin, ['centroids'], [im])


""" def find_centres_masked(imin, maskin):
    """
    """

    # Entire comment block == duplicate from find_contours_masked.
    # im = self.read_image(imin, cv2.CV_LOAD_IMAGE_COLOR)
    # imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    # mask = self.read_image(maskin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    #
    # apply mask
    # maskedim = cv2.bitwise_and(imgray, imgray, mask = mask)

    contours, contoursim = find_contours_masked(imin, maskin)
    im = read_image(imin, cv2.IMREAD_COLOR)
    mask = read_image(maskin, cv2.IMREAD_GRAYSCALE)

    print 'contours has length: '
    print len(contours)

    centres = []
    
    for i in range(len(contours)):
        # To-do: soft-code these limits.
        if cv2.contourArea(contours[i]) < 5:
            continue
        if cv2.contourArea(contours[i]) > 250:
            continue

        moments = cv2.moments(contours[i])
        print "i is:"
        print i
        print "moments:"
        print moments
        centres.append(
            (int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00'])))
        cv2.circle(im, centres[-1], 5, (0, 255, 0), -1)

    print centres

    save_image(imin, ['centroids_masked'], [im])
"""

testimage = "~/Documents/PYTHON/SilentDiscoData/Frames/TX-BACK UP_21_0.png"
otsu_threshold(testimage)
# imaged = read_image(testimage, cv2.IMREAD_COLOR)
# show_image(imaged)
# save_image(testimage, ['test'], [imaged])
# save_image(testimage, ['test'], [imaged], testdir)