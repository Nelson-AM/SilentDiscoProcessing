import os, csv, cv2
import numpy as np
from matplotlib import pyplot as plt

# TODO: check for all functions that return values AND save images if this is necessary.



########################################
#####     GEN IMAGE PROCESSING     #####
########################################


def read_image(imin, colorspace = None):
    """ Reads an image from a filepath.
    
    Args:
        imin: full path to image (absolute or relative), if it's not a string the function assumes 
              it to be an image.
        colorspace: one of the following cv2.imread flags: cv2.IMREAD_COLOR, cv2.IMREAD_GRAYSCALE,
                    cv2.IMREAD_UNCHANGED (optional).
    Returns:
        An image array.
    """
    
    if isinstance(imin, str):
        imin = os.path.expanduser(imin)
        
        if colorspace:
            return cv2.imread(imin, colorspace)
        else:
            return cv2.imread(imin)
    else:
        return imin


def save_image(image, imname, imdir = None):
    """ Save image to file.
    
    Args:
        image: image to save (array of values)
        imname: name of image to append to imdir, if it contains no extension default to png.
        imdir: full path to target directory (absolute or relative path), if none is given, image is
               saved to the current working directory.
    """
    
    # Test if imname contains an extension, if not: default to png.
    if len(imname.rsplit('.')) == 1:
        imname = imname + ".png"
    
    if imdir:
        imname = imdir + imname
        cv2.imwrite(imname, image)
    else:
        cv2.imwrite(imname, image)


def save_images(images, imnames, imdir = None):
    """ Save multiple images to files (calls save_image)
    
    Args:
        images: list of image to save (array of values)
        imnames: list of image names to append to imdir, if it contains no extension default to png.
        imdir: full path to target directory (absolute or relative path), if none is given, image is
               saved to the current working directory.
    """
    
    if imdir:
        for imname, image in zip(imnames, images):
            save_image(image, imname, imdir)
    else:
        for imname, image in zip(imnames, images):
            save_image(image, imname)


def show_image(imin, imdir = None):
    """ Displays image using matplotlib.
    
    Args:
        imin: path to image (absolute or relative) or array of values to display.
    """
    
    if isinstance(imin, str):
        image = read_image(imin)
    else:
        image = imin
    
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


def separate_colors(imin, imdir = None):
    """ Takes a colour image and separates the colour layers.
    
    Args:
        imin: path to image (absolute or relative) or color image to separate.
        imdir: 
    
    Returns:
        saves individual color layers to file
        b, g, r: individual color layers of the original image.
    """

    if isinstance(imin, str):
        # Grayscale versus color image loading for debugging purposes.
        img = read_image(imin, cv2.CV_LOAD_IMAGE_COLOR)
    else:
        img = imin
    
    b, g, r = cv2.split(img)

    # Display image for debugging purposes.
    # show_image(img)

    imnames = ['b', 'g', 'r']
    images = [b, g, r]
    
    if imdir:
        save_images(images, imnames, imdir)
    else:
        save_images(images, imnames)
    
    return b, g, r


def otsu_base(imin, gauss = None):
    if gauss:
        blurim = cv2.GaussianBlur(imin, (5, 5), 0)
        _, otsuim = cv2.threshold(blurim, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    else:
        _, otsuim = cv2.threshold(imin, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    return otsuim


def otsu_threshold_test(imin, gauss = None):
    """ Perform Otsu thresholding.
    
    Args:
        imin
        gauss
    
    Returns:
        thresholded image
    """
    
    if isinstance(imin, str):
        img = read_image(imin)
    else:
        img = imin
    
    if len(img.shape) is 3:
        # FIXME: tuple call and then test function!
        otsuim = np.empty(img.shape)
        for i in range(img.shape[-1]):
            print i
            otsuim[:,:,i] = otsu_base(img[:,:,i], gauss)
    else:
        otsuim = otsu_base(img, gauss)
    
    return otsuim
    


def otsu_threshold(imin, gauss = None, imdir = None):
    """ Perform otsu thresholding
    
    Args:
        imin: path to image (absolute or relative) or array of values to threshold.
        gauss: optional
        imdir: optional path to save directory.
    
    Returns:
        otsuim: thresholded
        saves thresholded file
    """
    
    # TODO: assumes greyscale image (i.e. one color layer or a greyscaled image)
    # TODO: option for filename as argument?
    
    if isinstance(imin, str):
        img = read_image(imin)
    else:
        img = imin
    
    if gauss:
        blurim = cv2.GaussianBlur(img, (5, 5), 0)
        _, otsuim = cv2.threshold(blurim, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        imname = 'otsu_gauss'
        
    else:
        _, otsuim = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        imname = 'otsu'
    
    if imdir:
        save_image(otsuim, imname, imdir)
    else:
        save_image(otsuim, imname)
    
    return otsuim


def otsu_threshold_multi(imin, gauss = None, imdir = None):
    """ Takes an image and creates binarised versions using Otsu thresholding.
    
    Args:
        imin
    Returns:
        otsu_b, otsu_g, otsu_r: 
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
    
    # if imdir:
    #    save_images(images, imnames, imdir)
    # else:
    #    save_images(images, imnames)
    
    return otsu_b, otsu_g, otsu_r


def find_contours_single(imin, maskin = None):
    """ Finds contours on single channel image.
    
    Performs Otsu thresholding, then finds and draws contours.
    """
    
    im = otsu_threshold(imin, "gauss")
    contoursim = read_image(imin, cv2.IMREAD_COLOR)
    
    if maskin:
        mask = read_image(maskin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        im = cv2.bitwise_and(im, im, mask = mask)
    
    contours, _ = cv2.findContours(im, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(contoursim, contours, -1, (0, 0, 255), 2)
    
    return contours, contoursim


def find_contours_multi(imin, maskin = None):
    """ Finds contours of each colour layer, then returns them.  Applies mask if necessary.
    
    Args:
        imin:
        makskin:
    
    Returns:
        contours_b, contours_g, contours_r: dictionary of contours for the individual layers
        
    1. Call otsu_multi with gaussian filtering, returns colour layers.
    2. Find contours for each layer.
    """
    
    # TODO: allow function call with input image, not text string.
    #       save_image assumes imin is a string.
    
    b, g, r = otsu_threshold_multi(imin, "gauss")
    
    if maskin:
        # Read mask and apply to all three layers.
        # TODO: make sure read_image handles the colorspace argument properly.
        mask = read_image(maskin)
        mask = cv2.cvtColor(mask, cv2.cv.CV_BGR2GRAY)
        
        # TODO: see if this can be simplified (i.e. reduce number of near-duplicate lines).
        # IDEA: Instead of splitting the image into different variables, iterate over the image layers.
        b = cv2.bitwise_and(b, b, mask = mask)
        g = cv2.bitwise_and(g, g, mask = mask)
        r = cv2.bitwise_and(r, r, mask = mask)
    
    # TODO: see if this can be simplified (i.e. reduce number of near-duplicate lines).
    contours_b, _ = cv2.findContours(b, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_g, _ = cv2.findContours(g, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contours_r, _ = cv2.findContours(r, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    return contours_b, contours_g, contours_r


def save_contours_multi(imin, imname, maskin = None, savedir = None):
    """ Finds contours for each colour layer, then draws them onto the original color image.
    
    Args:
        imin:
        imname:
        makskin:
        savedir:
    
    Returns:
        saves image to file
        shows image on screen (show_image, matplotlib)
        contours_b, contours_g, contours_r: dictionary of contours for the individual layers
        
    1. Call find_contours_multi, returns contours for each colour layer.
    2. Draw contours onto original color image.
    3. Save image to file.
    """
    
    if not isinstance(imin, str):
        contoursim = read_image(imin)
    
    if maskin:
        contours_b, contours_g, contours_r = find_contours_multi(imin, maskin = maskin)
    else:
        contours_b, contours_g, contours_r = find_contours_multi(imin)
    
    # TODO: see if this can be simplified (i.e. reduce number of near-duplicate lines).
    cv2.drawContours(contoursim, contours_b, -1, (255, 0, 0), 2)
    cv2.drawContours(contoursim, contours_g, -1, (0, 255, 0), 2)
    cv2.drawContours(contoursim, contours_r, -1, (0, 0, 255), 2)
    
    if savedir:
        save_image(imin, imname, savedir)
    else:
        save_image(imin, imname)


def find_centres(contours):
    """
    """
    
    centres = []
    
    for i in range(len(contours)):
        if cv2.contourArea(contours[i]) < 5:
            continue
        if cv2.contourArea(contours[i]) > 250:
            continue
        
        moments = cv2.moments(contours[i])
        
        centres.append(
            (int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00'])))
    
    print centres
    return centres


def find_centres_multi(imin, maskin = None):
    """ Finds centres in each color layer.
    
    Args:
        imin
        maskin
    
    Returns:
        centres_b, centres_g, centres_r:
    """
    
    # FIXME: multiple values of maskin, need to use a different keyword.
    if maskin:
        contours_b, contours_g, contours_r = find_contours_multi(imin, maskin = maskin)
    else:
        contours_b, contours_g, contours_r = find_contours_multi(imin)
    
    # Preallocate for each color layer.
    centres_b = find_centres(contours_b)
    centres_g = find_centres(contours_g)
    centres_r = find_centres(contours_r)
    
    return centres_b, centres_g, centres_r


def save_centres_multi(imin, imname, maskin = None, savedir = None):
    """
    """
    
    # TODO: add "masked" string to image name if mask is applicable.
    if maskin:
        centres_b, centres_g, centres_r = find_centres_multi(imin, mask = maskin)
    else:
        centres_b, centres_g, centres_r = find_centres_multi(imin)
    
    centre_image = read_image(imin)
    
    for i in range(len(centres_b)):
        cv2.circle(centre_image, centres_b[i], 5, (0, 255, 255), -1)
    for i in range(len(centres_g)):
        cv2.circle(centre_image, centres_g[i], 5, (255, 0, 255), -1)
    for i in range(len(centres_r)):
        cv2.circle(centre_image, centres_r[i], 5, (255, 255, 0), -1)
    
    if savedir :
        save_image(imin, imname, savedir)
    else:
        save_image(imin, imname)
    
    

def find_centres_single(imin, maskin = None, imdir = None):
    """
    """
    
    # Assumes single channel image.
    # - Run separate_colors.
    # - Run find_centres for each layer.
    contours, contoursim = find_contours_single(imin)
    
    im = read_image(imin, cv2.IMREAD_COLOR)
    
    if maskin:
        mask = read_image(maskin, cv2.IMREAD_GRAYSCALE)
        im = cv2.bitwise_and(imgray, imgray, mask = mask)
        imname = 'centroids_masked'
    else:
        imname = 'centroids_unmasked'
    
    centres = find_centres(contours)
    
    return centres
    
    if imdir:
        save_image(im, imname, imdir)
    else:
        save_image(im, imname)


def save_centres(filename, timepoint, color, centres):
    """ Saves list of centres as >comma separated values<.
    
    Requires input:
    filename
        String of the full filepath.
    timepoint
        Identifier for either time or frame number.
    centres
        List of centres (x, y).
        Need to save the centres as two separate basic columns instead of the current array.
    """
    
    with open(filename, 'ab') as csvfile:
        spamwriter = csv.writer(csvfile, quoting = csv.QUOTE_ALL)
        
        centres_x = [x[0] for x in centres]
        centres_y = [x[1] for x in centres]
        
        for i in range(len(centres)):
            
            # centres_x = 
            # centres_y = 
            
            row = [timepoint] + [color] + [centres_x[i]] + [centres_y[i]]
            spamwriter.writerow(row)





########################################
#####     HSV IMAGE PROCESSING     #####
########################################





########################################
#####       DRAFT FUNCTIONS        #####
########################################

def show_centres(image, centres):
    
    for i in range(len(centres)):
        cv2.circle(image, centres[i], 5, (0, 255, 255), -1)
    
    show_image(image)


# testimage = "~/Documents/PYTHON/SilentDiscoData/Frames/TX-BACK UP_21_0.png"
# im = read_image(testimage)
# print len(im.shape)
# save_image(testimage, 'test', im, 'Processed2')
# save_image(testimage, 'test', im)