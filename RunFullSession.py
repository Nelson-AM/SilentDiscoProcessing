# RunSession

from ProcessImage import *
from ProcessVideo import *
from GraphModeling import *
from graph_tool.all import *
import cv2

from matplotlib import pyplot as plt
import numpy as np

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
# videofile = "/Volumes/SAMSUNG/TX-BACK UP_21.mov"
# centresfile = "/Volumes/SAMSUNG/centres10frames_masked_xy.csv"

centresfile = "/Volumes/SAMSUNG/ESCOM/allframes.csv"
# centresfile = "/Volumes/SAMSUNG/ESCOM/centresperframe_masked.csv"

# Using a single threshold and single timepoint.  These can be looped over if necessary.
# timestamp = 150354

thresholdrange = [50, 100, 150, 200, 250, 300, 350, 400] # , 500, 600, 700, 800, 900]
# thresholdrange = [400]
# threshold = 50

# create_graphs_color (note: plural) builds one graph for each timepoint in the input file.  The color argument is optional, if no color is given then it will automatically create graphs for red, green and blue.  The graphs are saved as xml.gz files, images of the graphs are saved as well, with the vertices in their approximated real-world location.
# create_graph_color(centresfile, timestamp, threshold, "red", graphdir = None)
# create_graph_color(centresfile, timestamp, threshold, "green", graphdir = None)

# In case of the shared CSV file, looping over all timestamps:
frame_start = 80000
frame_step = 50
frame_stop = 85000
# frame_stop = 10000
frame_total = frame_stop + 1
# frame_stop = 369490

def errorfill(x, y, yerr, color = None, alpha_fill = 0.3, ax = None):
    ax = ax if ax is not None else plt.gca()
    if color is None:
        color = ax._get_lines.color_cycle.next()
    if np.isscalar(yerr) or len(yerr) == len(y):
        ymin = y - yerr
        ymax = y + yerr
    elif len(yerr) == 2:
        ymin, ymax = yerr
    ax.plot(x, y, color = color)
    ax.fill_between(x, ymax, ymin, color = color, alpha = alpha_fill)


for threshold in thresholdrange:
    
    fulldf = pd.DataFrame(columns = ['frameno', 'localcluster', 'globalcluster',
                                      'globalsd', 'vertexaverage', 'vertexsd'])
    
    for i in range(frame_start, frame_total, frame_step):
        print i
        
        # Get graph for current frame and threshold.
        g = create_graph(centresfile, i, threshold, "/Volumes/SAMSUNG/ESCOM/Graphs")
        
        # Test if number of vertices is greater than zero.  If n_vertices is greater than zero, do the following, if not, make the entry a NaN?  Check how matplotlib deals with NaNs.
        if get_number_vertices(g) is not 0:
            
            # Get local clustering values.
            gclust = local_clustering(g)
            (glocalc, glocalsd) = vertex_average(g, gclust)
            
            # Get vertex average.
            (gvertav, gvertsd) = vertex_average(g, 'total')
            
        else:
            print "This graph has 0 vertices."
            
            glocalc = float('NaN')
            glocalsd = float('NaN')
            gvertav = float('NaN')
            gvertsd = float('NaN')
        
        # Get global clustering averages.
        (gglobalc, gglobalsd) = global_clustering(g)
        
        # Append values to dataframes.
        fulldf = fulldf.append({'frameno': i, 
                                'localcluster': glocalc,
                                'localsd': glocalsd,
                                'globalcluster': gglobalc,
                                'globalsd': gglobalsd,
                                'vertexaverage': gvertav,
                                'vertexsd': gvertsd},
                                ignore_index = True)
    
    globalplotname = ("/Volumes/SAMSUNG/ESCOM/Plots/global_" + str(threshold) + "_" +
                     str(frame_start) + "_" + str(frame_stop) + ".png")
    localplotname = ("/Volumes/SAMSUNG/ESCOM/Plots/local_" + str(threshold) + "_" +
                    str(frame_start) + "_" + str(frame_stop) + ".png")
    vertavplotname = ("/Volumes/SAMSUNG/ESCOM/Plots/vertav_" + str(threshold) + "_" + 
                     str(frame_start) + "_" + str(frame_stop) + ".png")
    
    # Plot global clustering + shaded standard deviation.
    plt.plot(fulldf.frameno, fulldf.globalcluster, color = 'blue')
    plt.fill_between(fulldf.frameno, 
                     fulldf.globalcluster - fulldf.globalsd, 
                     fulldf.globalcluster + fulldf.globalsd,
                     color = 'blue', alpha = 0.25)
    axes = plt.gca()
    # axes.set_ylim([0, 1])
    axes.set_xlim([frame_start, frame_total])
        
    plt.savefig(globalplotname)
    plt.clf()
    
    # Plot local clustering + shaded standard deviation.
    plt.plot(fulldf.frameno, fulldf.localcluster, color = 'green')
    plt.fill_between(fulldf.frameno,
                     fulldf.localcluster - fulldf.localsd,
                     fulldf.localcluster + fulldf.localsd,
                     color = 'green', alpha = 0.25)
    axes = plt.gca()
    # axes.set_ylim([0, 1])
    axes.set_xlim([frame_start, frame_total])
    
    plt.savefig(localplotname)
    plt.clf()
    
    # Plot vertex average + shaded standard deviation.
    plt.plot(fulldf.frameno, fulldf.vertexaverage, color = 'green')
    plt.fill_between(fulldf.frameno,
                     fulldf.vertexaverage - fulldf.vertexsd,
                     fulldf.vertexaverage + fulldf.vertexsd,
                     color = 'green', alpha = 0.25)
    axes = plt.gca()
    # axes.set_ylim([0, 1])
    axes.set_xlim([frame_start, frame_total])
    plt.savefig(vertavplotname)
    
    plt.clf()
    