import cv2

def find_centres_masked(imin, maskin):
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

    print('contours has length: ' + len(contours))

    centres = []
    
    for i in range(len(contours)):
        # To-do: soft-code these limits.
        if cv2.contourArea(contours[i]) < 5:
            continue
        if cv2.contourArea(contours[i]) > 250:
            continue

        moments = cv2.moments(contours[i])
        print("i is:" + i)
        print("moments: " + moments)
        centres.append(
            (int(moments['m10'] / moments['m00']), int(moments['m01'] / moments['m00'])))
        cv2.circle(im, centres[-1], 5, (0, 255, 0), -1)

    print(centres)

    save_image(imin, ['centroids_masked'], [im])
