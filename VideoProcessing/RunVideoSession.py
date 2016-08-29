import argparse

from ProcessVideo import *
from ProcessImage import *

# Construct the argument parse and parse the arguments.
ap = argparse.ArgumentParser()

ap.add_argument("-v", "--video", required = True, help = "Path to the video file.")
ap.add_argument("-m", "--mask", required = True, help = "Path to the mask file.")
# ap.add_argument("-v", "--video", help = "Path to the video file.")
# ap.add_argument("-m", "--mask", help = "Path to the mask file.")

ap.add_argument("-s", "--step", type = int, default = 1, 
                help = "Step size in number of frames. Default is 1.")
# Script currently processes the entire video, consider adding frame_total argument for partial video processing. However, this would also require a frame_start argument...

csvname = "/Volumes/SAMSUNG/MOSI/split_colors.csv"

args = vars(ap.parse_args())

video = args["video"]
mask = args["mask"]

# CHANGED: toogle when done testing script.
frame_start = 1
frame_step = args["step"]

# CHANGED: toggle when done testing script.
# frame_total = frame_start + 10
frame_total = get_number_frames(video)
frame_end = frame_total + 1

savedir = str(video.rsplit("/", 1)[0])

for i in range(frame_start, frame_end, frame_step):
    
    frame = extract_frame_frame(video, i)
    
    # TODO: get centres from contours data.
    if mask:
        imname = "centres_masked_" + str(i)
        cent_b, cent_g, cent_r = find_centres_multi(frame, maskin = mask)
        
    else:
        imname = "centres_" + str(i)
        cent_b, cent_g, cent_r = find_centres_multi(frame)
    
    # TODO: save centres to csv file (same folder as video file).
    save_centres(csvname, i, "blue", cent_b)
    save_centres(csvname, i, "green", cent_g)
    save_centres(csvname, i, "red", cent_r)

