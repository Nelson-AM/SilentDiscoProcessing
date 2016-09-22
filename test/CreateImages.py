# RunSession

from ProcessImage import *
from ProcessVideo import *
from GraphModeling import *
from graph_tool.all import *
import cv2
import glob

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


graphdir = "/Volumes/SAMSUNG/fullgraphs/"
graphlist = os.listdir(graphdir)
thresholds = [150]

frame_start = 134850
frame_step = 10
frame_stop = 137100
frame_total = frame_stop + 1

for threshold in thresholds:
    
    greendf = pd.DataFrame(columns = ["frameno", "localcluster", "localsd",
                                      "globalcluster", "globalsd", 
                                      "vertexaverage", "vertexsd"])
    reddf = pd.DataFrame(columns = ["frameno", "localcluster", "localsd",
                                    "globalcluster", "globalsd", 
                                    "vertexaverage", "vertexsd"])
    
    for file in sorted(glob.glob(graphdir + str(threshold) + "/*.xml.gz")):
        
        # print file
        i = file.split("_")
        idot = i[1].split(".")
        # print i[1]
        # print i
        
        if float(i[1]) in range(frame_start, frame_total, frame_step):
            print file
            
            image_graph(file, "/Volumes/SAMSUNG/PNG/")

"""
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
frame_start = 50000
frame_step = 50
frame_stop = 75000
# frame_stop = 10000
frame_total = frame_stop + 1
# frame_stop = 369490

# create_graphs does the same, but takes every point in the image regardless of color.
create_graphs(centresfile, threshold, graphdir = None)

# In case of the shared CSV file, looping over all timestamp.  This also works for create_graphs.
frame_start = 0
frame_step = 100
frame_total = 369400


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
    
    greendf = pd.DataFrame(columns = ['frameno', 'localcluster', 'globalcluster',
                                      'globalsd', 'vertexaverage', 'vertexsd'])
    reddf = pd.DataFrame(columns = ['frameno', 'localcluster', 'globalcluster',
                                    'globalsd', 'vertexaverage', 'vertexsd'])
    
    for i in range(frame_start, frame_total, frame_step):
        print i
        
        # Get graph for current frame and threshold.
        greeng = create_graph_color(centresfile, i, threshold, 
                                    "green", "/Volumes/SAMSUNG/ESCOM/Graphs")
        redg = create_graph_color(centresfile, i, threshold, 
                                  "red", "/Volumes/SAMSUNG/ESCOM/Graphs")
        

        # Test if number of vertices is greater than zero.  If n_vertices is greater than zero, do the following, if not, make the entry a NaN?  Check how matplotlib deals with NaNs.
        if get_number_vertices(greeng) is not 0:
            
            # Get local clustering values.
            greenclust = local_clustering(greeng)
            (greenlocalc, greenlocalsd) = vertex_average(greeng, greenclust)
            
            # Get vertex average.
            (greenvertav, greenvertsd) = vertex_average(greeng, 'total')
            
        else:
            print "Green graph number bla has 0 vertices."
            
            greenlocalc = float('NaN')
            greenlocalsd = float('NaN')
            greenvertav = float('NaN')
            greenvertsd = float('NaN')
        
        if get_number_vertices(redg) is not 0:
            
            # Get local clustering values.
            redclust = local_clustering(redg)
            (redlocalc, redlocalsd) = vertex_average(redg, redclust)
            
            # Get vertex average.
            (redvertav, redvertsd) = vertex_average(redg, 'total')
            
        else:
            print "Red graph number bla has 0 vertices."
            
            redlocalc = float('NaN')
            redlocalsd = float('NaN')
            redvertav = float('NaN')
            redvertsd = float('NaN')
        
        # Get global clustering averages.
        (greenglobalc, greenglobalsd) = global_clustering(greeng)
        (redglobalc, redglobalsd) = global_clustering(redg)
        
        # Append values to dataframes.
        greendf = greendf.append({'frameno': i, 
                                  'localcluster': greenlocalc,
                                  'localsd': greenlocalsd,
                                  'globalcluster': greenglobalc,
                                  'globalsd': greenglobalsd,
                                  'vertexaverage': greenvertav,
                                  'vertexsd': greenvertsd},
                                  ignore_index = True)
        reddf = reddf.append({'frameno': i,
                              'localcluster': redlocalc,
                              'localsd': redlocalsd,
                              'globalcluster': redglobalc,
                              'globalsd': redglobalsd,
                              'vertexaverage': redvertav,
                              'vertexsd': redvertsd},
                              ignore_index = True)
    
    globalplotname = ("/Volumes/SAMSUNG/ESCOM/Plots/global_" + str(threshold) + "_" +
                     str(frame_start) + "_" + str(frame_stop) + ".png")
    localplotname = ("/Volumes/SAMSUNG/ESCOM/Plots/local_" + str(threshold) + "_" +
                    str(frame_start) + "_" + str(frame_stop) + ".png")
    vertavplotname = ("/Volumes/SAMSUNG/ESCOM/Plots/vertav_" + str(threshold) + "_" + 
                     str(frame_start) + "_" + str(frame_stop) + ".png")
    
    # Plot global clustering + shaded standard deviation.
    plt.plot(greendf.frameno, greendf.globalcluster, color = 'green')
    plt.fill_between(greendf.frameno, 
                     greendf.globalcluster - greendf.globalsd, 
                     greendf.globalcluster + greendf.globalsd,
                     color = 'green', alpha = 0.25)
    plt.plot(reddf.frameno, reddf.globalcluster, color = 'red')
    plt.fill_between(reddf.frameno,
                     reddf.globalcluster - reddf.globalsd,
                     reddf.globalcluster + reddf.globalsd,
                     color = 'red', alpha = 0.25)
    axes = plt.gca()
    # axes.set_ylim([0, 1])
    axes.set_xlim([frame_start, frame_total])
        
    plt.savefig(globalplotname)
    plt.clf()
    
    # Plot local clustering + shaded standard deviation.
    plt.plot(greendf.frameno, greendf.localcluster, color = 'green')
    plt.fill_between(greendf.frameno,
                     greendf.localcluster - greendf.localsd,
                     greendf.localcluster + greendf.localsd,
                     color = 'green', alpha = 0.25)
    plt.plot(reddf.frameno, reddf.localcluster, color = 'red')
    plt.fill_between(reddf.frameno,
                     reddf.localcluster - reddf.localsd,
                     reddf.localcluster + reddf.localsd,
                     color = 'red', alpha = 0.25)
    axes = plt.gca()
    # axes.set_ylim([0, 1])
    axes.set_xlim([frame_start, frame_total])
    
    plt.savefig(localplotname)
    plt.clf()
    
    # Plot vertex average + shaded standard deviation.
    plt.plot(greendf.frameno, greendf.vertexaverage, color = 'green')
    plt.fill_between(greendf.frameno,
                     greendf.vertexaverage - greendf.vertexsd,
                     greendf.vertexaverage + greendf.vertexsd,
                     color = 'green', alpha = 0.25)
    plt.plot(reddf.frameno, reddf.vertexaverage, color = 'red')
    plt.fill_between(reddf.frameno,
                     reddf.vertexaverage - reddf.vertexsd,
                     reddf.vertexaverage + reddf.vertexsd,
                     color = 'red', alpha = 0.25)
    axes = plt.gca()
    # axes.set_ylim([0, 1])
    axes.set_xlim([frame_start, frame_total])
    plt.savefig(vertavplotname)
    
    plt.clf()
"""