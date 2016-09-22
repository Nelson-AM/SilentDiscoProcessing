# RunSession

from ProcessImage import *
from ProcessVideo import *
from ProcessGraphs import *
from graph_tool.all import *
import cv2

from matplotlib import pyplot as plt
import numpy as np

centresfile = "/Volumes/SAMSUNG/MOSI/csv/split_colors_10.csv"

# thresholdrange = [50, 100, 150, 200, 250, 300, 350, 400, 500, 600, 700, 800, 900]
thresholdrange = [150]

frame_start = 1 
frame_step = 10
frame_stop = 139201
frame_total = frame_stop + 1

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

savedir = "/Volumes/SAMSUNG/MOSI/graphs/"

if not os.path.isdir(savedir):
    os.mkdir(savedir)

centresfile = read_csv(centresfile)

for threshold in thresholdrange:
    
    # fulldf = pd.DataFrame(columns = ['frameno', 'localcluster', 'globalcluster', 'globalsd', 'vertexaverage', 'vertexsd'])
    
    reddir = savedir + "red_" + str(threshold)
    greendir = savedir + "green_" + str(threshold)
    bluedir = savedir + "blue_" + str(threshold)
    if not os.path.isdir(reddir):
        os.mkdir(reddir)
    if not os.path.isdir(greendir):
        os.mkdir(greendir)
    if not os.path.isdir(bluedir):
        os.mkdir(bluedir)
    
    print threshold
    
    for i in range(frame_start, frame_total, frame_step):
        # print i
        
        # Get graph for current frame and threshold.
        g_red = create_graph_color(centresfile, i, threshold, "red", graphdir=reddir)
        g_red = create_graph_color(centresfile, i, threshold, "green", graphdir=greendir)
        g_blue = create_graph_color(centresfile, i, threshold, "blue", graphdir=bluedir)
        
        printProgress(i, frame_total, 
                      prefix="Progress:", suffix="Complete", barLength=50)
    
    """
        
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
    """