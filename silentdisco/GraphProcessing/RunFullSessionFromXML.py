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
            print(file)
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
