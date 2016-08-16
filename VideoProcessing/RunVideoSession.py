import argparse

from ProcessVideo import *
from ProcessImage import *

# Construct the argument parse and parse the arguments.
ap = argparse.ArgumentParser()
ap.add_argument("-v", "--video", help = "path to the video file")
ap.add_argument("-m", "--mask", help = "path to the mask file")
args = vars(ap.parse_args())

vidin = args["video"]
mask = args["mask"]

# TODO: softcode frame-total.

time = 1
frame_start = 1
frame_total = 100
frame_step = 1

# save_frame_frame(vidin, time)

for i in range(frame_start, frame_total, frame_step):
    frame = extract_frame_time(vidin, i)
    find_contours_multi(frame, mask)
    
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