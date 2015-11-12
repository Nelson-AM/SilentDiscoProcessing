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
TODO    - Connected components analysis (take centroid). Set up hard filter for region of interest.
TODO    - Translate image coordinates into real-world coordinates.
    """
    
    def __init__(self):
        self.data = []
    
    def save_image(self, imin, imnames, images):
        
        for imname, image in zip(imnames, images):
            cv2.imwrite(imin[:-4] + '_' + imname + '.png', image)
    
    def show_image_col(self, imin):
        
        # Correct ordering of colour layers from BGR to RGB.
        imin2 = imin[:,:,::-1]
        
        plt.imshow(imin2)
        # Hide tick values on X and Y axes.
        plt.xticks([]), plt.yticks([])
        plt.show()
    
    def show_image_gs(self, imin):
        
        plt.imshow(imin, cmap = 'gray', interpolation = 'bicubic')
        # Hide tick values on X and Y axes.
        plt.xticks([]), plt.yticks([])
        plt.show()
        
    def separate_colours(self, imin):
        """ Takes a colour image and separates the colour layers.
        """
        
        img = cv2.imread(imin)
        b, g, r = cv2.split(img)
        
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
        
        img = cv2.imread(imin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
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
        
        

session = ProcessImage()

session.separate_colours('example_009.png')

# blaargh is courtesy of Maarten
# blaargh = ProcessImage()

# blaargh.separate_colours('example_001.png')

# blaargh.otsu_threshold('example_001_g.png')
# blaargh.otsu_threshold('example_001_r.png')
# blaargh.otsu_threshold('example_001_b.png')

# Stuff I might want to put into the class:
#
# def runsession(self, imagename):
#    """ Runs an image processing session.
#    """
#    
#    self.separate_colours(imagename)