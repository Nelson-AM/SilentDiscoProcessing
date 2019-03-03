import os
import cv2
from matplotlib import pyplot as plt


def read_video(vidin):
    """
    """
    vidin = os.path.expanduser(vidin)
    return cv2.VideoCapture(vidin)


def save_image(imin, imnames, images, outdir):
    """ DUPLICATE FROM ProcessImage.py
    
    Saves image to same path as original, with added string contained
    in imname.

    To-do:
    - Generalize so images are saved with the same extension as original.
    """

    imin = os.path.expanduser(imin)
    outdir = os.path.expanduser(outdir)

    for imname, image in zip(imnames, images):
        cv2.imwrite(outdir + imin[17:-4] + '_' + str(imname / 1000) + '.png', image)


def show_image(imin):
    """ DUPLICATE FROM ProcessImage.py
    
    Displays image using matplotlib.

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


def process_video(vidin):

    cap = read_video(vidin)
    # cv2.VideoCapture("./out.mp4")

    while not cap.isOpened():
        cap = read_video(vidin)
        # cap = cv2.VideoCapture("./out.mp4")

        cv2.waitKey(1000)
        print("Wait for the header")

        pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)

        while True:
            flag, frame = cap.read()

            if flag:

                # The frame is ready and already captured
                show_image(frame)
                # cv2.imshow('video', frame)
                pos_frame = cap.get(cv2.CAP_PROP_POS_FRAMES)
                print(str(pos_frame) + " frames")

            else:

                # The next frame is not ready, so we try to read it again.
                cap.set(cv2.CAP_PROP_POS_FRAMES, pos_frame - 1)
                print("Frame is not ready")

                # It is better to wait a while for the next frame to be
                # ready.
                cv2.waitKey(1000)

                if cv2.waitKey(10) == 27:
                    break

                if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
                    # If the number of captured frames is equal to the
                    # total number of frames, we stop.
                    break


def process_video_time(vidin, time, outdir):

    vidcap = read_video(vidin)

    # Cue to 20 sec. position, not sure what 0 does here.
    # Something related to CV_CAP_PROP_POS_MSEC probably?
    # vidcap.set(0, time)
    vidcap.set(cv2.CAP_PROP_POS_MSEC, time)
    success, image = vidcap.read()

    if success:
        print(time)

        # save frame as PNG
        imnames = [time]
        images = [image]

        save_image(vidin, imnames, images, outdir)

    # cv2.imwrite("frame20sec.jpg", image)
    # self.show_image(image)
