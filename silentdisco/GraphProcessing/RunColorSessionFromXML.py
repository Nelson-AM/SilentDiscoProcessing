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
xmldir = "/Volumes/SAMSUNG/colorgraphs/"
savedir = "/Volumes/SAMSUNG/csv/"

# xmldir = "/Volumes/SAMSUNG/ESCOM/graphs/20160610/color/"
# thresholds = [400] # , 500, 600, 700, 800, 900]
# thresholds = [50, 100, 150, 200, 250, 300, 350, 400]
thresholds = [250]

# In case of the shared CSV file, looping over all timestamps:
frame_start = 10
frame_step = 10
frame_stop = 369490
frame_total = frame_stop + 1

spans = [50]
# spans = [10, 20, 30, 40, 60, 70, 80, 90, 100]

for threshold in thresholds:
        
    greendf = pd.DataFrame(columns = ["frameno", "localcluster", "localsd",
                                          "globalcluster", "globalsd", 
                                          "vertexaverage", "vertexsd"])
    reddf = pd.DataFrame(columns = ["frameno", "localcluster", "localsd",
                                        "globalcluster", "globalsd", 
                                        "vertexaverage", "vertexsd"])
     
    for file in sorted(glob.glob(xmldir + str(threshold) + "/*.xml.gz")):
        
        # print file
        i = file.split("_")
        idot = i[2].split(".")
        # print i
        # print idot
        # print i
        
        if float(i[2]) in range(frame_start, frame_total, frame_step):
            # print "Succes!"

            print(file)
            g = load_graph(file)
        
            if 'red' in file:
                    
                if get_number_vertices(g) is not 0:
                    # print "Succes, yet again! It's red!"
                    
                    # Get local clustering values.
                    redclust = local_clustering(g)
                    (redlocalc, redlocalsd) = vertex_average(g, redclust)
            
                    # Get vertex average.
                    (redvertav, redvertsd) = vertex_average(g, 'total')
            
                else:
                    # print "This red graph has 0 vertices."
            
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
                    # print "Succes, yet again! It's green!"
                    
                    # Get local clustering values.
                    greenclust = local_clustering(g)
                    (greenlocalc, greenlocalsd) = vertex_average(g, greenclust)
        
                    # Get vertex average.
                    (greenvertav, greenvertsd) = vertex_average(g, 'total')
            
                else:
                    # print "This green graph has 0 vertices."
            
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
                print('Oops, this is not a red or a green graph.')
        
    redcsvname = savedir + "reddata_t" + str(threshold) + ".csv"
    greencsvname = savedir + "greendata_t" + str(threshold) + ".csv"
            
    reddf.to_csv(redcsvname, sep = ",")
    greendf.to_csv(greencsvname, sep = ",")
            
    """
    pltdir = "/Volumes/SAMSUNG/Presentationplots/"
    if not os.path.isdir(pltdir):
        os.mkdir(pltdir)
    
    globalplotname = (pltdir + "global_" + 
                          str(threshold) + "_" +
                          str(frame_start) + "_" + 
                          str(frame_stop) + ".png")
    localplotname = (pltdir + "local_" + 
                         str(threshold) + "_" +
                         str(frame_start) + "_" + 
                         str(frame_stop) + ".png")
    vertavplotname = (pltdir + "vertav_" + 
                          str(threshold) + "_" + 
                          str(frame_start) + "_" + 
                          str(frame_stop) + ".png")
        
    print globalplotname
    
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
    axes.set_ylim([0, 5])
    axes.set_xlim([frame_start, frame_total])
    plt.savefig(vertavplotname)
    
    plt.clf()
    
    for span in spans:
        
        localewmaplotname = (pltdir + "local" + 
                                 str(threshold) + "_" +
                                 str(frame_start) + "_" + 
                                 str(frame_stop) + "ewma_" + 
                                 str(span) + ".png")
        globalewmaplotname = (pltdir + "global" + 
                                  str(threshold) + "_" +
                                  str(frame_start) + "_" + 
                                  str(frame_stop) + "ewma_" + 
                                  str(span) + ".png")
        vertavewmaplotname = (pltdir + "vertav" + 
                                  str(threshold) + "_" + 
                                  str(frame_start) + "_" + 
                                  str(frame_stop) + "ewma_" + 
                                  str(span) + ".png")
        
        # Moving averages over reddf and greendf.
        glocalav = pd.ewma(greendf.localcluster, span = span)
        glocalsd = pd.ewma(greendf.localsd, span = span)
        rlocalav = pd.ewma(reddf.localcluster, span = span)
        rlocalsd = pd.ewma(reddf.localsd, span = span)
        
        gglobalav = pd.ewma(greendf.globalcluster, span = span)
        gglobalsd = pd.ewma(greendf.globalsd, span = span)
        rglobalav = pd.ewma(reddf.globalcluster, span = span)
        rglobalsd = pd.ewma(reddf.globalsd, span = span)
    
        gvertexav = pd.ewma(greendf.vertexaverage, span = span)
        gvertexsd = pd.ewma(greendf.vertexsd, span = span)
        rvertexav = pd.ewma(reddf.vertexaverage, span = span)
        rvertexsd = pd.ewma(reddf.vertexsd, span = span)
        
        plt.clf()
        
        # TODO: widen field of view on the time-axis.
        # TODO: set image sized so make it stretch more horizontally.
        
        # EWMA LOCAL
        # Plot local clustering + shaded standard deviation.
        plt.plot(greendf.frameno, glocalav, color = 'green')
        plt.fill_between(greendf.frameno, 
                         glocalav - glocalsd, 
                         glocalav + glocalsd, 
                         color = 'green', alpha = 0.25)
        plt.plot(reddf.frameno, rlocalav, color = 'red')
        plt.fill_between(reddf.frameno, 
                         rlocalav - rlocalsd, 
                         rlocalav + rlocalsd, 
                         color = 'red', alpha = 0.25)
        axes = plt.gca()
        axes.set_ylim([0, 1])
        axes.set_xlim([frame_start, frame_total])
    
        plt.savefig(localewmaplotname)
        plt.clf()
        
        # EWMA GLOBAL
        # Plot global clustering + shaded standard deviation.
        plt.plot(greendf.frameno, gglobalav, color = 'green')
        plt.fill_between(greendf.frameno, 
                         gglobalav - gglobalsd, 
                         gglobalav + gglobalsd,
                         color = 'green', alpha = 0.25)
        plt.plot(reddf.frameno, rglobalav, color = 'red')
        plt.fill_between(reddf.frameno,
                         rglobalav - rglobalsd,
                         rglobalav + rglobalsd,
                         color = 'red', alpha = 0.25)
        axes = plt.gca()
        axes.set_ylim([0, 1])
        axes.set_xlim([frame_start, frame_total])
    
        plt.savefig(globalewmaplotname)
        plt.clf()
        
        # EWMA VERTEX AVERAGE
        # Plot vertex average + shaded standard deviation.
        plt.plot(greendf.frameno, gvertexav, color = 'green')
        plt.fill_between(greendf.frameno,
                         gvertexav - gvertexsd,
                         gvertexav + gvertexsd,
                         color = 'green', alpha = 0.25)
        plt.plot(reddf.frameno, rvertexav, color = 'red')
        plt.fill_between(reddf.frameno,
                         rvertexav - rvertexsd,
                         rvertexav + rvertexsd,
                         color = 'red', alpha = 0.25)
        axes = plt.gca()
        axes.set_ylim([0, 5])
        axes.set_xlim([frame_start, frame_total])
        
        plt.savefig(vertavewmaplotname)
        plt.clf()
    """