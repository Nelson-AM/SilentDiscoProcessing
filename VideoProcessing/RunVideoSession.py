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

video = args["video"]
mask = args["mask"]

# CHANGED: frame indexing starts at 1 (frames 0 and 1 are identical).
frame_start = 1500
frame_step = args["step"]

# TODO: toggle when done testing script.
frame_total = frame_start + 10
# frame_total = get_number_frames(video)
frame_end = frame_total + 1

savedir = str(video.rsplit("/", 1)[0])

for i in range(frame_start, frame_end, frame_step):
    
    # TODO: get each designated frame.
    # TODO: get contours and save to image for mask creation.
    # TODO: get centres from contours data.
    # TODO: save centres to csv file (same folder as video file).
    frame = extract_frame_frame(video, i)
    
    if mask:
        imname = "centres_masked_" + str(i)
        find_centres_multi(frame, maskin = mask)
        
        # find_contours_multi(frame, imname, maskin = mask, savedir = savedir)
    else:
        imname = "centres_" + str(i)
        find_centres_multi(frame)
        
        # find_contours_multi(frame, imname, savedir = savedir)

