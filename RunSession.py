# RunSession

from ProcessImage import *
from ProcessVideo import *
from GraphModeling import *

""" 
ProcessImage is imported to process individual video frames, to find the image moments and their 
             centres.  Centres can be saved into a CSV file for further processing by GraphModeling.
             Shares some functions with ProcessVideo.

ProcessVideo is imported to process video files, extract frames from them and either save or return
             them for further processing.  Uses some functions from ProcessImage.

GraphModeling is imported to process CSV files containing information on the centres and build 
              graphs from this data.  Graphs are currently saved on a per-frame and per-threshold
              basis.
"""


########################################
#####        GRAPH MODELING        #####
########################################

# Specify the file locations. Home directory can be referred to using the tilde (~).
videofile = "/Volumes/SAMSUNG/TX-BACK UP_21.mov"
centresfile = "/Volumes/SAMSUNG/centres10frames_masked_xy.csv"

# Using a single threshold and single timepoint.  These can be looped over if necessary.
timestamp = 150354
threshold = 50

# create_graphs_color (note: plural) builds one graph for each timepoint in the input file.  The color argument is optional, if no color is given then it will automatically create graphs for red, green and blue.
create_graphs_color(centresfile, threshold, "red", graphdir = None)
create_graphs_color(centresfile, threshold, "green", graphdir = None)




"""
for timestamp in timestamps:
    for threshold in thresholds:
        
        create_graph_color (note: singular) builds a graph for the specified timepoint in the 
        input file.
        graph = create_graph_color(centresfile, timepoint, threshold, "red")
"""



"""
for i in range(frame_start, frame_total, frame_step):
    current_frame = extract_frame_frame(videofile, i)
    
    save_frame_frame(videofile, i)
    
    centres_b, centres_g, centres_r = find_centres_multi(current_frame, mask)
    
    # print centres_b
    
    # Leave blue in for playing around, remove it for the big - proper - file.
    save_centres(centresfile, i, 'blue', centres_b)
    save_centres(centresfile, i, 'green', centres_g)
    save_centres(centresfile, i, 'red', centres_r)
"""

