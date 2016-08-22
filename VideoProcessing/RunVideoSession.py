import argparse

from ProcessVideo import *
from ProcessImage import *

# Construct the argument parse and parse the arguments.
ap = argparse.ArgumentParser()

# TODO: switch to required = True when done debugging.
# ap.add_argument("-v", "--video", required = True, help = "Path to the video file.")
# ap.add_argument("-m", "--mask", required = True, help = "Path to the mask file.")
ap.add_argument("-v", "--video", help = "Path to the video file.")
ap.add_argument("-m", "--mask", help = "Path to the mask file.")

ap.add_argument("-s", "--step", type = int, default = 1, help = "Step size in number of frames. \
                Default is 1.")
# Script currently processes the entire video, consider adding frame_total argument for partial video processing. However, this would also require a frame_start argument...

args = vars(ap.parse_args())

vidin = args["video"]
mask = args["mask"]

# CHANGED: frame indexing starts at 1 (frames 0 and 1 are identical).
frame_start = 1
frame_step = args["step"]

frame_total = get_number_frames(vidin)

savedir = str(vidin.rsplit("/", 1)[0])

for i in range(frame_start, frame_end, frame_step):
    
    # TODO: get each designated frame.
    # TODO: get contours and save to image for mask creation.
    # TODO: get centres from contours data.
    # TODO: save centres to csv file (same folder as video file).
    frame = extract_frame_frame(vidin, i)
    
    if mask:
        imname = "frame_masked_" + str(i)
        find_contours_multi(frame, imname, maskin = mask, savedir = savedir)
    else:
        imname = "frame_" + str(i)
        find_contours_multi(frame, imname, savedir = savedir)

