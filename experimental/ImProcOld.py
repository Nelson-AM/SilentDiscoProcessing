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
    
    img = read_image(imin)
    
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

    # TODO: experimental function
    if maskin:
        mask = read_image(maskin, cv2.CV_LOAD_IMAGE_GRAYSCALE)
        
        if len(img.shape) is 3:
            for i in range(img.shape[-1]):
                maskim = cv2.bitwise_and(img[:, :, i], 
                                         img[:, :, i], 
                                         mask = mask)
                contoursim[:, :, i] = find_contours_base(maskim)
        else:
            maskim = cv2.bitwise_and(img, img, mask = mask)
            contoursim = find_contours_base(maskim)
    else:
        if len(img.shape) is 3:
            for i in range(img.shape[-1]):
                contoursim[:, :, i] = find_contours_base(imin[:, :, i])
        else:
            contoursim = find_contours_base(imin)
    
    return contours