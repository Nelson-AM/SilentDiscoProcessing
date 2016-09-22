# RunSession

from ProcessImage import *
from ProcessVideo import *
from GraphModeling import *
from graph_tool.all import *
import cv2
import glob

import pandas as pd
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

# Directory for the xml files + threshold values (for sub-directories).
# xmldir = "/Volumes/SAMSUNG/ESCOM/Graphs/20160510NewMask/"
xmldir = "/Volumes/SAMSUNG/fullgraphs/"
# xmldir = "/Volumes/SAMSUNG/fixedgraphs/"
savedir = "/Volumes/SAMSUNG/csv/"

if not os.path.isdir(savedir):
    os.mkdir(savedir)

thresholds = [150]
# thresholds = [50, 100, 150, 200, 250, 300, 350, 400]

# In case of the shared CSV file, looping over all timestamps:
frame_start = 10
frame_step = 10
frame_stop = 369490

frame_total = frame_stop + 1

span = 50

for threshold in thresholds:
    fulldf = pd.DataFrame(columns = ["frameno", "localcluster", "localsd",
                                     "globalcluster", "globalsd",
                                     "vertexaverage", "vertexsd"])
    
    smoothdf = pd.DataFrame(columns = ["frameno", "localcluster", "localsd",
                                       "globalcluster", "globalsd",
                                       "vertexaverage", "vertexsd"])
    
    for file in sorted(glob.glob(xmldir + str(threshold) + "/*.xml.gz")):
        
        i = file.split("_")
        idot = i[1].split(".")
        
        if float(i[1]) in range(frame_start, frame_total, frame_step):
            print file
            g = load_graph(file)
            
            if get_number_vertices(g) is not 0:
                
                # Get local clustering values.
                clust = local_clustering(g)
                (localc, localsd) = vertex_average(g, clust)
                
                # Get vertex average.
                (vertav, vertsd) = vertex_average(g, "total")
                
            else:
                localc = float("NaN")
                localsd = float("NaN")
                vertav = float("NaN")
                vertsd = float("NaN")
            
            # Get global clustering averages.
            (globalc, globalsd) = global_clustering(g)
        
            # Append values to dataframes.
            fulldf = fulldf.append({"frameno": int(i[1]),
                                    "localcluster": localc,
                                    "localsd": localsd,
                                    "globalcluster": globalc,
                                    "globalsd": globalsd,
                                    "vertexaverage": vertav,
                                    "vertexsd": vertsd},
                                    ignore_index = True)
            
            # TODO: save dataframe.
            fullcsvname = savedir + "rawdata_t" + str(threshold) + ".csv"
            
            fulldf.to_csv(fullcsvname, sep = ",")
    """
    # Moving averages over full data.
    localav = pd.ewma(fulldf.localcluster, span = span)
    localavsd = pd.ewma(fulldf.localsd, span = span)
    
    globalav = pd.ewma(fulldf.globalcluster, span = span)
    globalavsd = pd.ewma(fulldf.globalsd, span = span)
    
    vertexav = pd.ewma(fulldf.vertexaverage, span = span)
    vertexavsd = pd.ewma(fulldf.vertexsd, span = span)
    
    # Append smoothed values to dataframe
    smoothdf = smoothdf.append({"frameno": int(i[1]),
                                "localcluster": localav,
                                "localsd": localavsd,
                                "globalcluster": globalav,
                                "globalsd": globalavsd,
                                "vertexaverage": vertexav,
                                "vertexsd": vertexavsd},
                                ignore_index = True)
    
    # TODO: save dataframe.
    smoothcsvname = savedir + "smoothdata_t" + str(threshold) + "_s50.csv"
    smoothdf.to_csv(smoothcsvname, sep = ",")
    
    
    globalplotname = (savedir + "global_" + str(threshold) + "_" +
                     str(frame_start) + "_" + str(frame_stop) + ".png")
    globalewmaplotname = (savedir + "global" + str(threshold) + "_" +
                    str(frame_start) + "_" + str(frame_stop) + "ewma_" + str(span) + ".png")
    localplotname = (savedir + "local_" + str(threshold) + "_" +
                    str(frame_start) + "_" + str(frame_stop) + ".png")
    localewmaplotname = (savedir + "local" + str(threshold) + "_" +
                    str(frame_start) + "_" + str(frame_stop) + "ewma_" + str(span) + ".png")
    vertavplotname = (savedir + "vertav_" + str(threshold) + "_" + 
                     str(frame_start) + "_" + str(frame_stop) + ".png")
    vertavewmaplotname = (savedir + "vertav" + str(threshold) + "_" + 
                     str(frame_start) + "_" + str(frame_stop) + "ewma_" + str(span) + ".png")
    
    # Plot local clustering + shaded standard deviation.
    plt.plot(fulldf.frameno, fulldf.localcluster, color = "black")
    plt.fill_between(fulldf.frameno,
                     fulldf.localcluster - fulldf.localsd,
                     fulldf.localcluster + fulldf.localsd,
                     color = "black", alpha = 0.25)
    axes = plt.gca()
    axes.set_ylim([0, 1.2])
    axes.set_xlim([frame_start, frame_total])
    
    plt.savefig(localplotname)
    plt.clf()
    
    # Plot local clustering + shaded standard deviation.
    plt.plot(fulldf.frameno, localav, color = "black")
    plt.fill_between(fulldf.frameno,
                     localav - localsd,
                     localav + localsd,
                     color = "black", alpha = 0.25)
    axes = plt.gca()
    axes.set_ylim([0, 1.2])
    axes.set_xlim([frame_start, frame_total])
    
    plt.savefig(localewmaplotname)
    plt.clf()
    
    
    # Plot global clustering + shaded standard deviation.
    plt.plot(fulldf.frameno, fulldf.globalcluster, color = "black")
    plt.fill_between(fulldf.frameno, 
                     fulldf.globalcluster - fulldf.globalsd, 
                     fulldf.globalcluster + fulldf.globalsd,
                     color = "black", alpha = 0.25)
    axes = plt.gca()
    axes.set_ylim([0, 1.2])
    axes.set_xlim([frame_start, frame_total])
    
    
    
    plt.savefig(globalplotname)
    plt.clf()
    
    
    
    globalav = pd.ewma(fulldf.globalcluster, span = span)
    globalsd = pd.ewma(fulldf.globalsd, span = span)
    
    # EWMA GLOBAL
    # Plot global clustering + shaded standard deviation.
    plt.plot(fulldf.frameno, globalav, color = "black")
    plt.fill_between(fulldf.frameno, 
                     globalav - globalsd, 
                     globalav + globalsd,
                     color = "black", alpha = 0.25)
    axes = plt.gca()
    axes.set_ylim([0, 1.2])
    axes.set_xlim([frame_start, frame_total])
    
    plt.savefig(globalewmaplotname)
    plt.clf()
    
    
    
    # Plot vertex average + shaded standard deviation.
    plt.plot(fulldf.frameno, fulldf.vertexaverage, color = "black")
    plt.fill_between(fulldf.frameno,
                     fulldf.vertexaverage - fulldf.vertexsd,
                     fulldf.vertexaverage + fulldf.vertexsd,
                     color = "black", alpha = 0.25)
    axes = plt.gca()
    axes.set_ylim([0, 5])
    axes.set_xlim([frame_start, frame_total])
    plt.savefig(vertavplotname)
    
    plt.clf()
    
    # EWMA VERTEX AVERAGE
    # Plot vertex average + shaded standard deviation.
    plt.plot(fulldf.frameno, vertexav, color = "black")
    plt.fill_between(fulldf.frameno,
                     vertexav - vertexsd,
                     vertexav + vertexsd,
                     color = "black", alpha = 0.25)
    axes = plt.gca()
    axes.set_ylim([0, 5])
    axes.set_xlim([frame_start, frame_total])
    plt.savefig(vertavewmaplotname)
    
    plt.clf()
    """