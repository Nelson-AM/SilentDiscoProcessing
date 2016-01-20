# RunSession

from ProcessImage import *
from ProcessVideo import *

videofile = "/Volumes/SAMSUNG/TX-BACK UP_21.mov"
frame_50 = "/Volumes/SAMSUNG/TX-BACK UP_21_50.png"
frame_2500 = "/Volumes/SAMSUNG/TX-BACK UP_21_2500.png"

# frame = extract_frame_frame(videofile, 30500)

# b, g, r = find_contours_multi(frame)

frame_50_read = read_image(frame_50)
show_image(frame_50_read)




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