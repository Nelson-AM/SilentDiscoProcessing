import os
import cv2 
import numpy as np
from matplotlib import pyplot as plt

class ProcessImage:
    """ Processes still images to extract coordinates of data points.
    
    Prerequisites:
    - Sample still images from video data.
    
    Plan:
    - Read image, separate colour layers, binarize images through (Otsu) thresholding.
    - 
    
    To-do:
DONE    - Look at edge cases for Otsu with Gaussian blur (empty vs. full).
DISC    - Check which other thresholding algorithms are implemented in OpenCV.
TODO    - Connected components analysis (take centroid).
TODO        - Set up limit for size (done).
        - Set up mask for area of interest (ignoring exhibition pieces).
TODO    - Translate image coordinates into real-world coordinates.
    """
    
    def __init__(self):
        self.data = []
    
    def read_image(self, imin, colourspace):
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
    
    def save_image(self, imin, imnames, images):
        """ Saves image to same path as original, with added string contained in imname.
        
        To-do:
        - Generalize so images are saved with the same extension as original.
        """
        
        imin = os.path.expanduser(imin)
        
        for imname, image in zip(imnames, images):
            cv2.imwrite(imin[:-4] + '_' + imname + '.png', image)
    
    def show_image(self, imin):
        """ Displays image using matplotlib.
        
        Assumes colour images are read using cv2, transforms the colourspace from BGR to RGB.
        """
        
        if len(imin.shape) == 3:
            imin = imin[:,:,::-1]
            plt.imshow(imin)
        else:
            plt.imshow(imin, cmap = 'gray', interpolation = 'bicubic')
        
        # Hide tick values on X and Y axes.
        plt.xticks([]), plt.yticks([])
        plt.show()
        
    def separate_colours(self, imin):
        """ Takes a colour image and separates the colour layers.
        """
        
        # Grayscale versus color image loading for debugging purposes.
        # img = self.read_image(imin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        img = self.read_image(imin, cv2.CV_LOAD_IMAGE_COLOR)
        b, g, r = cv2.split(img)
        
        # Display image for debugging purposes.
        # self.show_image(img)
        
        imnames = ['b', 'g', 'r']
        images = [b, g, r]
        
        self.save_image(imin, imnames, images)
        
        return b, g, r
    
    def simple_threshold(self, imin):
        """ Take an image and creates three binarized versions of it using simple thresholding.
        """
        
        img = cv2.imread(imin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
        ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
        ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
        ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
        ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
        
        imnames = ['simple_binary', 'simple_binary_inv', 'simple_trunc', 
                   'simple_tozero', 'simple_tozero_inv']
        images = [thresh1, thresh2, thresh3, 
                  thresh4, thresh5]
        
        self.save_image(imin, imnames, images)
    
    def adaptive_threshold(self, imin):
        """ Takes an image and creates three binarized versions of it using adaptive thresholding.
        """
        
        img = cv2.imread(imin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        img = cv2.medianBlur(img, 5)
        
        ret,th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, \
                                    cv2.THRESH_BINARY, 11, 12) # 50 - 100
        th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, \
                                    cv2.THRESH_BINARY, 11, 12) # 50 - 100
        
        imnames = ['adaptive_global', 'adaptive_mean', 'adaptive_gaussian']
        images = [th1, th2, th3]
        
        self.save_image(imin, imnames, images)
    
    def otsu_threshold(self, imin):
        """ Takes an image and creates binarised versions using Otsu thresholding.
        """
        
        img = self.read_image(imin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
        # Global thresholding
        ret1, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        # Otsu's thresholding
        ret2, th2 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        # Otsu's thresholding after Gaussian filtering
        blur = cv2.GaussianBlur(img, (5, 5), 0)
        ret3, th3 = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        imnames = ['noisy', 'global_v_127', 'otsu',
                  'gaussian_filtered', 'otsu_gaussian']
        images = [img, th1, th2, blur, th3]
        
        self.save_image(imin, imnames, images)
    
    def find_contours(self, imin):
        """ 
        """
        
        im = self.read_image(imin, cv2.IMREAD_COLOR)
        self.show_image(im)
        
        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        contours, hierarchy = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
                
        cv2.drawContours(im, contours, -1, (0, 0, 255), 2)
        
        self.show_image(im)
    
    def find_centres(self, imin):
        """
        """
        
        # ret,thresh = cv2.threshold(img,127,255,0)
        # 6 contours,hierarchy = cv2.findContours(thresh, 1, 2)
        # 7 
        # 8 cnt = contours[0]
        # 9 M = cv2.moments(cnt)
        # 10 print M
           
        im = self.read_image(imin, cv2.CV_LOAD_IMAGE_COLOR)
        imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        
        # self.save_image(imin, ['convertedCol'], [imgray])
        
        self.show_image(im)
        
        contours, _ = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_TC89_L1)
        
        cv2.drawContours(im, contours, -1, (0, 0, 255), 2)
        
        self.show_image(im)
        
        # contours, _ = cv2.findContours(img.copy(), cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_L1)
        
        print 'contours has length: '
        print len(contours)
        
        centres = []
        
        for i in range(len(contours)):
            
            if cv2.contourArea(contours[i]) < 20:
                continue
            
            moments = cv2.moments(contours[i])
            print "i is:"
            print i
            print "moments:"
            print moments
            centres.append((int(moments['m10']/moments['m00']), int(moments['m01']/moments['m00'])))
            cv2.circle(im, centres[-1], 3, (0, 255, 0), -1)
        
        print centres
        
        self.show_image(im)
        
        # cv2.imshow('image', img)
        # cv2.imwrite('output.png',img)
        # cv2.waitKey(0)

session = ProcessImage()

# session.separate_colours('~/Documents/PYTHON/SilentDiscoData/Screenshots/Example_004.png')
# session.otsu_threshold('~/Documents/PYTHON/SilentDiscoData/Screenshots/Example_004_g.png')
# session.otsu_threshold('~/Documents/PYTHON/SilentDiscoData/Screenshots/Example_004_r.png')
# session.find_contours('~/Documents/PYTHON/SilentDiscoData/Screenshots/Example_004_g_otsu_gaussian.png')
# session.find_contours('~/Documents/PYTHON/SilentDiscoData/Screenshots/Example_004_r_otsu_gaussian.png')

# WORKING
# session.find_centres('~/Documents/PYTHON/Example_004_r_crop.png')
# session.find_centres('~/Documents/PYTHON/Example_004_r_crop_2.png')

# session.find_centres('~/Documents/PYTHON/test_centres.png')
session.find_centres('~/Documents/PYTHON/SilentDiscoData/Screenshots/Example_004_r_crop.png')

# Stuff I might want to put into the class:
#
# def runsession(self, imagename):
#    """ Runs an image processing session.
#    """
#    
#    self.separate_colours(imagename)