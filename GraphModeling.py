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
    """ Read CSV file and return it as a pandas dataframe.
    """
    
    filename = os.path.expanduser(filename)
    
    with open(filename, "rb") as csvfile:
        spamreader = csv.reader(csvfile, quoting = csv.QUOTE_ALL)
        spamlist = list(spamreader)
        dataframe = pd.DataFrame(spamlist, columns = ["Timestamp", "Color", "X", "Y"])
        
        return dataframe


def save_graph(g, name, threshold, v_color, v_x, v_y, pos, graphdir = None):
    """ Saves graph g, including properties of vertices and edges.
    
    To-do:
    - Add directory as parameter for saving in any location.
    - Add e_weight as parameter.
    """
    
    if graphdir:
        # Build filename based on graphdir, name and threshold.
        graphnamegz = graphdir + '/' + name + "_" + str(threshold) + ".xml.gz"
        
    else:
        # Build filename based on name and threshold, saves to current working directory.
        graphnamegz = "../graph_" + name + "_" + str(threshold) + ".xml.gz"
    
    # Make properties internal.
    # g.vertex_properties["xcoordinate"] = v_x
    # g.vertex_properties["ycoordinate"] = v_y
    # g.vertex_properties["color"] = v_color
    # g.vertex_properties["position"] = pos
    # g.edge_properties["weight"] = e_weight
    
    print "Properties at time of saving: "
    g.list_properties()
    
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


def image_graph(filename, name, outdir):
    """ Takes a saved graph and saves it as an image.
    """
    
    # Build name based on given name and threshold.
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
    
    # >>> vprop = g.new_vertex_property("double")
    # >>> g.vp.foo = vprop
    #     equivalent to g.vertex_properties["foo"] = vprop
    # >>> v = g.vertex(0)
    # >>> g.vp.foo[v] = 3.14
    # >>> print(g.vp.foo[v])
    # 3.14
    
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
    
    # Make properties internal.
    g.vertex_properties["x"] = v_x
    g.vertex_properties["y"] = v_y
    g.vertex_properties["color"] = v_color
    g.vertex_properties["position"] = pos
    
    print "Properties after vertex creation: "
    g.list_properties()
    
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


def create_base_graph(dataframe, name, threshold):
    """ 
    """
    
    g = Graph()
    
    clist = dataframe["Color"].tolist()
    xlist = dataframe["X"].tolist()
    ylist = dataframe["Y"].tolist()
    
    vlist, v_x, v_y, v_color, pos = create_vertices(g, clist, xlist, ylist)
    create_edges(g, vlist, v_x, v_y, threshold)
    
    print "Properties after edge creation: "
    g.list_properties()
    
    # Make these functions external?
    save_graph(g, name, threshold, v_color, v_x, v_y, pos)      # e_weight
    save_graph_img(g, name, threshold, pos)


def create_graph(filename, timestamp, threshold):
    """ Takes data from CSV file and creates graph for given timestamp.
    
    Single-use case of greate_graphs.
    """
    
    centresdf = read_csv(filename)
    
    timedf = centresdf.loc[centresdf["Timestamp"] == str(timestamp)]
    
    create_base_graph(timedf, timestamp, threshold)


def create_graphs(filename, threshold):
    """ Creates graph from data in CSV file for each timepoint.
    """
    
    centresdf = read_csv(filename)
    
    for name, group in centresdf.groupby("Timestamp"):
        create_base_graph(group, name, threshold)


def create_graphs_color(filename, threshold, color = None):
    """ Creates graph from data in CSV file for each or a specific color at each timepoint.
    """
    
    centresdf = read_csv(filename)
    
    if color:
        # If a color is entered, build graph for only that color.
        # Note: is str(color) necessary?
        colordf = centresdf.loc[centresdf["Color"] == str(color)]
        
        for name, group in colordf.groupby("Timestamp"):
            cname = name + "_" + color
            create_base_graph(colordf, cname, threshold)
            
    else:
        # If no color is entered, build separate graphs for each color.
        colors = ["red", "green", "blue"]
        for color in colors:
            colordf = centresdf.loc[centresdf["Color"] == color]
            
            for name, group in colordf.groupby("Timestamp"):
                cname = name + "_" + color
                create_base_graph(colordf, cname, threshold)


def create_graphs_rg(filename, threshold, pgreen, pred):
    """ Creates graphs with randomly sampled red and green nodes in the given ratios
    """
    
    if  pgreen + pred == 100:
        # Awesome, do stuff!
        print pgreen + pred
        # Make list of all red nodes.
        # Make list of all green nodes.
        
        # Determine number of vertices that have to be selected for each color.
        # nred = round(pred / length(redlist))
        # ngreen = round(pgreen / length(greenlist))
        
        # Randomly sample each list until the desired amount of vertices is chosen for each list.
        
        # Build graph.
        
    else:
        # Error / warning that red + green has to add up to 100.
        print "pgreen and pred should add up to 100."
        sys.exit(-1)





#######################################
#####     STRUCTURAL ANALYSIS     #####
#######################################


def grah_analysis_function(arguments):
    """
    """
    
    # Here we do the statistical analysis part of the graph modeling.
    print "Yay, time for statistical analysis!"





########################################
#####       DRAFT FUNCTIONS        #####
########################################


def create_graph_color(filename, timestamp, threshold, color = None):
    """ Creates graph from data in CSV file for each or a specific color at each timepoint.
    
    NECESSARY?
    This function might not be necessary given the _rg version.  On the other hand this function 
    allows testing with any stray blue nodes that might still be around, to check the measures that
    we get from the modelling.  Blue should do something entirely different from red and green.
    """
    
    # Checks if a color is entered as a parameter.
    if color:
        print "Yay, color is: " + color + "."
        # If a color is entered, build graph for only that color.
    else:
        # If no color is entered, build graphs separately for each color.
        print "Boo, you didn't enter a color!"

