import os

import cv2


def save_image(imin, imname, image, imdir = None):
    """ Save image to same directory as original with string appended to end of name.

    imin
        string of original image path
    imname
        name of image to save as (appends to file name)
    image
        image to save to file
    imdir
        savepath if applicable (relative to imin path)

    Arguments imin and imdir are somewhat redundant.
    A more logical
    """
    
    if isinstance(imin, str):
        imin = os.path.expanduser(imin)
        # print imin
    
    if imdir:
        splitname = imin.rsplit('.', 1)[0]
        imdir = splitname.rsplit('/', 1)[0] + '/' + imdir
        splitname = splitname.rsplit('/', 1)[1]
        splitext = imin.rsplit('.', 1)[1]
        if splitext == "mov" or splitext == "mp4":
            splitext = "png"

        print(imdir + '/' + splitname + '_' + imname + '.' + splitext)
        cv2.imwrite(imdir + '/' + splitname + '_' + imname + '.' + splitext, image)
        
    else:
        splitname = imin.rsplit('.', 1)[0]
        splitext = imin.rsplit('.', 1)[1]
        print(splitext)
        if splitext == "mov" or splitext == "mp4":
            splitext = "png"

        print(splitname + '_' + imname + '.' + splitext)
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
