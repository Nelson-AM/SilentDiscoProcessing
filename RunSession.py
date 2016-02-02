# RunSession

from ProcessImage import *
from ProcessVideo import *

videofile = "/Volumes/SAMSUNG/TX-BACK UP_21.mov"
centresfile = "/Volumes/SAMSUNG/centres10frames_masked_xy.csv"

# frame_50 = "/Volumes/SAMSUNG/TX-BACK UP_21_50.png"
# frame_2500 = "/Volumes/SAMSUNG/TX-BACK UP_21_2500.png"

mask = "/Volumes/SAMSUNG/TX_MASK.png"

# frame_start = 0
# frame_step = 100
# frame_total = (14780 * 25) + 1

frame_start = 50350
frame_step = 1
frame_total = 50352

for i in range(frame_start, frame_total, frame_step):
    current_frame = extract_frame_frame(videofile, i)
    
    centres_b, centres_g, centres_r = find_centres_multi(current_frame, mask)
    
    # print centres_b
    
    # Leave blue in for playing around, remove it for the big - proper - file.
    save_centres(centresfile, i, 'blue', centres_b)
    save_centres(centresfile, i, 'green', centres_g)
    save_centres(centresfile, i, 'red', centres_r)



# for i in range(frame_start, frame_total, frame_step):
#     process_video_frame('/Volumes/SAMSUNG/TX-BACK UP_21.mov', i, 'Frames')
    
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