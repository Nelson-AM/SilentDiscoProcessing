# RunSession

from ProcessImage import *
from ProcessVideo import *
from GraphModeling import *
from graph_tool.all import *
import cv2
import glob


import numpy as np
import matplotlib.pyplot as plt

# from mpltools import special

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

def errorfill(x, y, yerr, color = None, alpha_fill = 0.3, ax = None):
    ax = ax if ax is not None else plt.gca()
    if color is None:
        color = ax._get_lines.color_cycle.next()
    if np.isscalar(yerr) or len(yerr) == len(y):
        ymin = y - yerr
        ymax = y + yerr
    elif len(yerr) == 2:
        ymin, ymax = yerr
    ax.plot(x, y, color=color)
    ax.fill_between(x, ymax, ymin, color=color, alpha=alpha_fill)

# Directory for the xml files + threshold values (for sub-directories).
# xmldir = "/Volumes/SAMSUNG/ESCOM/Graphs/20160510NewMask/"
xmldir = "/Volumes/SAMSUNG/ESCOM/graphs/20160602/"
thresholds = [50, 100, 150, 200, 250, 300, 350, 400] # , 500, 600, 700, 800, 900]
# thresholds = [150, 200, 250, 300, 350, 400] # , 500, 600, 700, 800, 900]

# In case of the shared CSV file, looping over all timestamps:
frame_start = 3000
frame_step = 10
frame_stop = 4000
frame_total = frame_stop + 1

for threshold in thresholds:
    
    greendf = pd.DataFrame(columns = ["frameno", "localcluster", "localsd",
                                      "globalcluster", "globalsd", 
                                      "vertexaverage", "vertexsd"])
    reddf = pd.DataFrame(columns = ["frameno", "localcluster", "localsd",
                                    "globalcluster", "globalsd", 
                                    "vertexaverage", "vertexsd"])
     
    for file in sorted(glob.glob(xmldir + str(threshold) + "/*.xml.gz")):
        
        print file
        i = file.split("_")
        idot = i[2].split(".")
        print i
        print idot
        # print i
        
        if float(i[2]) in range(frame_start, frame_total, frame_step):
            print "Succes!"
        
            g = load_graph(file)
        
            if 'red' in file:
            
                if get_number_vertices(g) is not 0:
                    print "Succes, yet again! It's red!"
                    
                    # Get local clustering values.
                    redclust = local_clustering(g)
                    (redlocalc, redlocalsd) = vertex_average(g, redclust)
            
                    # Get vertex average.
                    (redvertav, redvertsd) = vertex_average(g, 'total')
            
                else:
                    print "This red graph has 0 vertices."
            
                    redlocalc = float('NaN')
                    redlocalsd = float('NaN')
                    redvertav = float('NaN')
                    redvertsd = float('NaN')
            
                # Get global clustering averages.
                (redglobalc, redglobalsd) = global_clustering(g)
        
                # Append values to dataframes.
                reddf = reddf.append({'frameno': int(i[2]),
                                      'localcluster': redlocalc,
                                      'localsd': redlocalsd,
                                      'globalcluster': redglobalc,
                                      'globalsd': redglobalsd,
                                      'vertexaverage': redvertav,
                                      'vertexsd': redvertsd},
                                      ignore_index = True)
        
            elif 'green' in file:
                if get_number_vertices(g) is not 0:
                    print "Succes, yet again! It's green!"
                    
                    # Get local clustering values.
                    greenclust = local_clustering(g)
                    (greenlocalc, greenlocalsd) = vertex_average(g, greenclust)
            
                    # Get vertex average.
                    (greenvertav, greenvertsd) = vertex_average(g, 'total')
            
                else:
                    print "This green graph has 0 vertices."
            
                    greenlocalc = float('NaN')
                    greenlocalsd = float('NaN')
                    greenvertav = float('NaN')
                    greenvertsd = float('NaN')
            
                # Get global clustering averages.
                (greenglobalc, greenglobalsd) = global_clustering(g)
                
                # Append values to dataframes.
                greendf = greendf.append({'frameno': int(i[2]), 
                                          'localcluster': greenlocalc,
                                          'localsd': greenlocalsd,
                                          'globalcluster': greenglobalc,
                                          'globalsd': greenglobalsd,
                                          'vertexaverage': greenvertav,
                                          'vertexsd': greenvertsd},
                                          ignore_index = True)
            
            else:
                print 'Oops, this is not a red or a green graph.'
    
    # Moving average localcluster + SD
    # Moving average globalcluster + SD
    # 
    
    pltdir = "/Volumes/SAMSUNG/ESCOM/plots/20160603xmlplots/"
    if not os.path.isdir(pltdir):
        os.mkdir(pltdir)
    
    globalplotname = (pltdir + "global_" + str(threshold) + "_" +
                     str(frame_start) + "_" + str(frame_stop) + ".png")
    localplotname = (pltdir + "local_" + str(threshold) + "_" +
                    str(frame_start) + "_" + str(frame_stop) + ".png")
    vertavplotname = (pltdir + "vertav_" + str(threshold) + "_" + 
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
    axes.set_ylim([0, 1.2])
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
    axes.set_ylim([0, 1.2])
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
    axes.set_ylim([0, 20])
    axes.set_xlim([frame_start, frame_total])
    plt.savefig(vertavplotname)
    
    plt.clf()
    
    