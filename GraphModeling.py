import os
import csv
import numpy as np
import pandas as pd
from graph_tool.all import *

from matplotlib import pyplot as plt


################################################
#####     AUX CSV AND GRAPH PROCESSING     #####
################################################

def read_csv(filename):
    """ Read CSV file and return it as a list.
    """
    
    filename = os.path.expanduser(filename)
    
    with open(filename, "rb") as csvfile:
        spamreader = csv.reader(csvfile, quoting = csv.QUOTE_ALL)
        
        spamlist = list(spamreader)
        return spamlist


def save_graph(g, name, threshold, v_color, v_x, v_y, pos):
    """ Saves graph g, including properties of vertices and edges.
    
    To-do:
    - Add directory as parameter for saving in any location.
    - Add e_weight as parameter.
    """
    
    # Build filename based on name and threshold.
    graphnamegz = "../graph_" + name + "_" + str(threshold) + ".xml.gz"

    # Make properties internal.
    g.vertex_properties["xcoordinate"] = v_x
    g.vertex_properties["ycoordinate"] = v_y
    g.vertex_properties["color"] = v_color
    g.vertex_properties["position"] = pos
    # g.edge_properties["weight"] = e_weight
    
    # now we can save it
    g.save(graphnamegz)


def save_graph_img(g, name, threshold, pos):
    """ Saves png image of graph g with vertices at "real" locations.
    
    Plots vertices based on x- and y-coordinates, making 
    visualisation correspond to real-life situation.
    
    To-do:
    - Add custom directory support.
    - Take into account e_weight.
        - Check if line color can be shaded for this.
    - Fill in vertices as the color that they are (r/g/b).
    """
    
    graphnameim = "../graph_" + name + "_" + str(threshold) + ".png"
    print graphnameim
    
    graph_draw(g, pos, output_size = (1000, 1000), 
               vertex_color = [1, 1, 1, 0],
               vertex_size = 5, edge_pen_width = 1.2, 
               vcmap = plt.cm.gist_heat_r, output = graphnameim)


def image_graph(filename, outdir):
    """ Takes a saved graph and saves it as an image.
    
    To-do:
    - 
    """
    
    graphnameim = "../graph_" + name + "_" + str(threshold) + ".png"
    print graphnameim
    
    g = load_graph(filename)
    
    x = g.vertex_properties["xcoordinate"]
    y = g.vertex_properties["ycoordinate"]
    color = g.vertex_properties["color"]
    pos = g.vertex_properties["position"]
    
    
    graph_draw(g, pos, output_size = (1000, 1000), 
               vertex_color = [1, 1, 1, 0],
               vertex_size = 5, edge_pen_width = 1.2, 
               vcmap = plt.cm.gist_heat_r, output = graphnameim)


##################################
#####     GRAPH BUILDING     #####
##################################


def create_vertices(g, clist, xlist, ylist):
    """ Support function, creates vertices for graph g from create_graphs.
    """
    
    vlist = []
    dlist = []
    
    v_age = g.new_vertex_property("int")
    v_color = g.new_vertex_property("string")
    v_x = g.new_vertex_property("int")
    v_y = g.new_vertex_property("int")
    pos = g.new_vertex_property("vector<double>")
    
    for i in range(len(clist)):
        
        v = g.add_vertex()
        v_color[v] = clist[i]
        v_x[v] = xlist[i]
        v_y[v] = ylist[i]
        
        pos[i] = (v_x[i], v_y[i])
        
        vlist.append(v)
    
    return vlist, v_x, v_y, v_color, pos


def create_edges(g, vlist, v_x, v_y, threshold):
    """ Support function, creates edges for graph g from create_graphs.
    """
    
    e_weight = g.new_edge_property("double")
    distancelist = []
    
    for i in range(len(vlist)):
        for j in range(i + 1, len(vlist)):    
            
            distance = np.hypot(v_x[i] - v_x[j], v_y[i] - v_y[j]) 
            distancelist.append(distance)
            
            if distance < threshold:
                source = vlist[i]
                target = vlist[j]
                e = g.add_edge(source, target)
    
    distance_norm = []
    weights = []
    
    
    
    for i in range(len(distancelist)):
        distance_norm.append((distancelist[i] - min(distancelist)) / 
                             (max(distancelist) - min(distancelist)))
        
        weights.append(1 - distance_norm[i])


def create_graph(filename, timestamp, threshold):
    """ Takes data from CSV file and creates graph for given timestamp.
    
    Single-use case of greate_graphs.
    """
    
    centreslist = read_csv(filename)
    centresdf = pd.DataFrame(centreslist,
                              columns = ["Timestamp", "Color", "X", "Y"])
    
    timedf = centresdf.loc[centresdf["Timestamp"] == str(timestamp)]
    
    g = Graph()
    
    clist = timedf["Color"].tolist()
    xlist = timedf["X"].tolist()
    ylist = timedf["Y"].tolist()
    
    vlist, v_x, v_y, v_color, pos = create_vertices(g, clist, xlist, ylist)
    
    create_edges(g, vlist, v_x, v_y, threshold)
    
    save_graph(g, name, threshold, v_color, v_x, v_y, pos)   # e_weight
    
    save_graph_img(g, name, threshold, pos)


def create_graphs(filename, threshold):
    """ Creates graph from data in CSV file for each timepoint.
    """
    
    centreslist = read_csv(filename)
    centresdf = pd.DataFrame(centreslist,
                             columns = ["Timestamp", "Color", "X", "Y"])
    
    for name, group in centresdf.groupby("Timestamp"):
        
        clist = group["Color"].tolist()
        xlist = group["X"].tolist()
        ylist = group["Y"].tolist()
        
        g = Graph()
        
        vlist, v_x, v_y, v_color, pos = create_vertices(g, clist, xlist, ylist)
        
        create_edges(g, vlist, v_x, v_y, threshold)
        
        save_graph(g, name, threshold, v_color, v_x, v_y, pos)   # e_weight
        
        save_graph_img(g, name, threshold, pos)


def create_graph_color(filename, timestamp, threshold, color = None):
    """ Creates graph from data in CSV file for each or a specific color at each timepoint.
    
    NECESSARY?
    This function might not be necessary given the _rg version.  On the other hand this function 
    allows testing with any stray blue nodes that might still be around, to check the measures that
    we get from the modelling.  Blue should do something entirely different from red and green.
    """
    
    # Checks if a color is entered as a parameter.
    if color:
        # If a color is entered, build graph for only that color.
    else:
        # If no color is entered, build graphs separately for each color.


def create_graphs_color(filename, threshold, color = None):
    """ Creates graph from data in CSV file for each or a specific color at each timepoint.
    """
    
    
    # Checks if a color is entered as a parameter.
    if color:
        # If a color is entered, build graph for only that color.
    else:
        # If no color is entered, build graphs separately for each color.


def create_graphs_rg(filename, threshold, pgreen, pred):
    """ Creates graphs with randomly sampled red and green nodes in the given ratios
    """
    
    if pred + pgreen == 100:
        # Awesome, do stuff!
        
        # Make list of all red nodes.
        # Make list of all green nodes.
        
        # Determine number of vertices that have to be selected for each color.
        # nred = round(pred / length(redlist))
        # ngreen = round(pgreen / length(greenlist))
        
        # Randomly sample each list until the desired amount of vertices is chosen for each list.
        
        # Build graph.
        
    else:
        # Error / warning that red + green has to add up to 100.



##################################
#####     GRAPH ANALYSIS     #####
##################################


