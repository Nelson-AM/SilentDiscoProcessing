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

ap.add_argument("-s", "--step", type = int, default = 1, help = "Step size in number of frames.")
# Script currently processes the entire video, consider adding frame_total argument for partial video processing. However, this would also require a frame_start argument...

args = vars(ap.parse_args())

vidin = args["video"]
mask = args["mask"]

# TODO: check indexing for frame start, first frame or not?
frame_start = 0
frame_step = args["step"]

# TODO: switch to soft-coded when done debugging.
frame_total = 10
# frame_total = get_number_frames(vidin)
frame_end = frame_total + 1

# print "Frame start = " + str(frame_start)
# print "Frame step = " + str(frame_step)
# print "Frame total = " + str(frame_total)

for i in range(frame_start, frame_end, frame_step):
    
    
    # TODO: get each designated frame.
    # TODO: get contours from frame.
    # TODO: save contours to csv file (same folder as video file).
    frame = extract_frame_frame(vidin, i)
    
    if mask:
        find_contours_multi(frame, mask)
    else:
        find_contours_multi(frame)
    

# Process video frames within the range [frame_start, frame_total] with step size frame_step.
# Does this need to be a for loop or can a while loop be used as well?
#   While is more useful if processing the entire video because it uses fewer parameters.
#   For is easier to implement atm.

# save_frame_frame(vidin, time)

#for i in range(frame_start, frame_total, frame_step):
#    frame = extract_frame_time(vidin, i)
#    find_contours_multi(frame, mask)
    
# b, g, r = find_contours_multi(frame_2500, mask)

# centres_b, centers_g, centres_r = find_centres_multi(frame_2500, mask)


# frame_500250 = extract_frame_frame(videofile, 50250)

# centres_b, centres_g, centres_r = find_centres_multi(frame_500250, mask)

# time = 50
# save_centres(centres_blue, time, centres_b)




# g = find_centres_single(frame_50_g)
# b, g, r = find_centres_multi(frame_50)

# print "contours for g are: "
# print g

# b, g, r = find_contours_multi(frame_2500)

# print "Contours for B are: \n"
# print b
# print "Contours for G are: \n"
# print g
# print "Contours for R are: \n"
# print r


# time_start = 0
# time_step = 60000
# time_total = (14780 * 1000) + 1

# save_frame_time('/Volumes/SAMSUNG/TX-BACK UP_21.mov', 50)




# frame_start = 0
# frame_step = 1
# frame_total = (14780 * 25) + 1

# Frames 0-3229 saved.
# save_frame_frame('/Volumes/SAMSUNG/TX-BACK UP_21.mov', 2500)