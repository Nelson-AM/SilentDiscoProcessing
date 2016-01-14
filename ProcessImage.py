import os
import cv2
import numpy as np
from matplotlib import pyplot as plt





########################################
#####     GEN IMAGE PROCESSING     #####
########################################


def read_image(imin, colorspace = None):
    """ Takes filename and (optional) colourspace to read image.
    
    Colourspace takes the cv2.imread flags:
    - cv2.IMREAD_COLOR.
        Loads a color image. Any transparency of image will be neglected.
        It is the default flag.
    - cv2.IMREAD_GRAYSCALE
        Loads image in grayscale mode.
    - cv2.IMREAD_UNCHANGED
        Loads image as such including alpha channel.
    """
    
    imin = os.path.expanduser(imin)
    
    if colorspace:
        return cv2.imread(imin, colorspace)
    else:
        return cv2.imread(imin)


def save_image(imin, imname, image, imdir = None):
    """ Save image to same directory as original with string appended to end of name.
    
    imdir is relative to the imin path.
    """
    
    imin = os.path.expanduser(imin)
    print imin
    
    if imdir:
        splitname = imin.rsplit('.', 1)[0]
        imdir = splitname.rsplit('/', 1)[0] + '/' + imdir
        splitname = splitname.rsplit('/', 1)[1]
        splitext = imin.rsplit('.', 1)[1]
        if splitext == "mov":
            splitext = "png"
        
        print imdir + '/' + splitname + '_' + imname + '.' + splitext
        cv2.imwrite(imdir + '/' + splitname + '_' + imname + '.' + splitext, image)
        
    else:
        splitname = imin.rsplit('.', 1)[0]
        splitext = imin.rsplit('.', 1)[1]
        if splitext == "mov":
            splitext = "png"
        
        print splitname + '_' + imname + '.' + splitext
        cv2.imwrite(splitname + '_' + imname + '.' + splitext, image)
        
        
def save_images(imin, imnames, images, imdir = None):
    """ Calls save_image to easily save multiple images (names and files in list forms).
    """
    
    if imdir:
        for imname, image in zip(imnames, images):
            save_image(imin, imname, image, imdir)
    else:
        for imname, image in zip(imnames, images):
            save_image(imin, imname, image)


def show_image(image):
    """ Displays image using matplotlib.
    
    Reads color images using cv2, transforms the colorspace from BGR to RGB.
    """
    
    if isinstance(image, str):
        image = read_image(image)
    
    if len(image.shape) == 3:
        image = image[:, :, ::-1]
        plt.imshow(image)
    else:
        plt.imshow(image, cmap = 'gray', interpolation = 'bicubic')

    # Hide tick values on X and Y axes.
    plt.xticks([]), plt.yticks([])
    plt.show()





########################################
#####     BGR IMAGE PROCESSING     #####
########################################


def separate_colors(imin):
    """ Takes a colour image and separates the colour layers.
    """

    # Grayscale versus color image loading for debugging purposes.
    # img = self.read_image(imin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    img = read_image(imin, cv2.CV_LOAD_IMAGE_COLOR)
    show_image(img)
    b, g, r = cv2.split(img)

    # Display image for debugging purposes.
    # self.show_image(img)

    imnames = ['b', 'g', 'r']
    images = [b, g, r]

    save_images(imin, imnames, images)

    return b, g, r


def simple_threshold(imin):
    """ Take an image and creates three binarized versions of it using simple thresholding.
    """

    img = read_image(imin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    # b, g, r = separate_colors(imin)

    ret, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    ret, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
    ret, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
    ret, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
    ret, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)

    imnames = ['simple_binary', 'simple_binary_inv', 'simple_trunc',
               'simple_tozero', 'simple_tozero_inv']
    images = [thresh1, thresh2, thresh3,
              thresh4, thresh5]

    save_images(imin, imnames, images)


def adaptive_threshold(imin):
    """ Takes an image and creates three binarized versions of it using adaptive thresholding.
    """
    
    b, g, r = separate_colors(imin)
    
    # img = read_image(imin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
    # img = cv2.medianBlur(img, 5)
    
    ret, th1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
    th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                                cv2.THRESH_BINARY, 11, 12)  # 50 - 100
    th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                cv2.THRESH_BINARY, 11, 12)  # 50 - 100
                                
    imnames = ['adaptive_global', 'adaptive_mean', 'adaptive_gaussian']
    images = [th1, th2, th3]
    
    save_images(imin, imnames, images)


def otsu_threshold(imin, gauss = None):
    """
    """
    
    image = read_image(imin)
    
    if gauss:
        blurim = cv2.GaussianBlur(image, (5, 5), 0)
        _, otsuim = cv2.threshold(blurim, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        save_image(imin, 'otsu_gauss', otsuim)
        
    else:
        _, otsuim = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        save_image(imin, 'otsu', otsuim)
    
    return otsuim


def otsu_threshold_multi(imin, gauss = None):
    """ Takes an image and creates binarised versions using Otsu thresholding.
    """
    
    b, g, r = separate_colors(imin)
    
    if gauss:
        blur_b = cv2.GaussianBlur(b, (5, 5), 0)
        blur_g = cv2.GaussianBlur(g, (5, 5), 0)
        blur_r = cv2.GaussianBlur(r, (5, 5), 0)
        
        _, otsu_b = cv2.threshold(blur_b, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        _, otsu_g = cv2.threshold(blur_g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        _, otsu_r = cv2.threshold(blur_r, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        imnames = ['otsu_gauss_b', 'otsu_gauss_g', 'otsu_gauss_r']
        
    else:
        _, otsu_b = cv2.threshold(b, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        _, otsu_g = cv2.threshold(g, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        _, otsu_r = cv2.threshold(r, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        
        imnames = ['otsu_b', 'otsu_g', 'otsu_r']
    
    images = [otsu_b, otsu_g, otsu_r]
    save_images(imin, imnames, images)
    return otsu_b, otsu_g, otsu_r


def find_contours(imin, maskin = None):
    """ Finds contours on single channel image.
    
    Performs Otsu thresholding, then finds and draws contours.
    """
    
    # Check if Otsu results in single or multi channel image. Otherwise read original image separately as color to show colored contours.
    im = otsu_threshold(imin, "gauss")
    imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    
    if maskin:
        mask = read_image(maskin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        imgray = cv2.bitwise_and(imgray, imgray, mask = mask)
    
    contours, _ = cv2.findContours(imgray, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contoursim = cv2.drawContours(im, contours, -1, (0, 0, 255), 2)

    return contours, contoursim

def find_contours_multi(imin, maskin = None):
    """ 
    - Call otsu_multi, returns colour layers.
    - Find contours for each layer.
    """
    
    b, g, r = otsu_threshold_multi(imin, "gauss")
    
    image = read_image(imin)
    # Need to check, otsu thresholded images probably already have only one channel. In that case, also load the original color image for contours being colored.
    # b_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    # g_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    # r_gray = cv2.cvtColor(b, cv2.COLOR_BGR2GRAY)
    
    if maskin:
        mask = read_image(maskin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
        # apply mask to all three images.
        b = cv2.bitwise_and(b, b, mask = mask)
        g = cv2.bitwise_and(g, g, mask = mask)
        r = cv2.bitwise_and(r, r, mask = mask)
    
    contours_b, _ = cv2.findContours(b, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_g, _ = cv2.findContours(g, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_r, _ = cv2.findContours(r, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    print "contours_b"
    
    cv2.drawContours(image, contours_b, -1, (255, 0, 0), 2)
    cv2.drawContours(image, contours_g, -1, (0, 255, 0), 2)
    cv2.drawContours(image, contours_r, -1, (0, 0, 255), 2)
    
    show_image(image)
    
    # Think of how to draw the contours on an image. Draw them in a different color for each layer?
    
    return contours_b, contours_g, contours_r


def find_centres(imin, maskin = None):
    """
    """
    
    # Assumes single channel image.
    # - Run separate_colors.
    # - Run find_centres for each layer.
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
    return centres
    
    if maskin:
        save_image(imin, 'centroids_masked', im)
        # Save centres masked.
    else:
        save_image(imin, 'centroids', im)
        # Save centres unmasked.





########################################
#####     HSV IMAGE PROCESSING     #####
########################################



# testimage = "~/Documents/PYTHON/SilentDiscoData/Frames/TX-BACK UP_21_0.png"
# im = read_image(testimage)
# print len(im.shape)
# save_image(testimage, 'test', im, 'Processed2')
# save_image(testimage, 'test', im)