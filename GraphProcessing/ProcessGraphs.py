# TODO: create script similar to ProcessVideo.py for graph processing.
import os, shutil, glob
from graph_tool.all import *


def read_graph(graphin):
    """ Reads graph from .xml.gz file
    
    Args:
        graphin:
    Returns:
        graph
    """
    
    if isinstance(graphin, str):
        graphin = os.path.expanduser(graphin)
        return load_graph(graphin)
    else:
        return graphin


#######################################
#####     STRUCTURAL ANALYSIS     #####
#######################################


def get_n_vertices(graphin):
    """ Reads graphs and returns number of vertices.
    
    Args:
    Returns:
    """
    
    g = read_graph(graphin)
    return g.num_vertices()


def get_n_vertices_color():
    """ Reads _full_ graph and returns number of vertices per color. """
    
    colors = [red, green, blue]
    g = read_graph(graphin)
    
    for color in colors:
        pass
        # Return vertices with correct color propertymap.

def get_n_edges(graphin):
    """ Reads graphs and returns number of edges.
    
    Args:
    Returns:
    """
    
    g = read_graph(graphin)
    return g.num_edges()


def save_local_cluster(graphin, savedir = None):
    """docstring for save_local_clust
    
    Args:
        graphin:
        savedir:
    Returns:
        saves local clustering and sd for graph in csvfile 
        (if exists: append to file, if not: create file)
    """
    pass
    
    # TODO: calculate local clustering and SD
    # TODO: save to file in savedir


def save_global_cluster(graphin, savedir = None):
    """docstring for save_global_clust
    
    Args:
        graphin:
        savedir:
    Returns:
        saves global clustering and sd for graph in csvfile 
        (if exists: append to file, if not: create file)
    """
    pass
    
    # TODO: calculate global clustering and SD
    # TODO: save to file in savedir


def save_vertex_average(graphin, savedir = None):
    """docstring for save_vertex_average
    
    Args:
        graphin:
        savedir:
    Returns:
        saves vertex average and sd for graph in csvfile 
        (if exists: append to file, if not: create file)
    """
    pass
    
    # TODO: calculate vertex average and SD
    # TODO: save to file in savedir
    # TODO: get threshold from graphname


def save_graph_measures(graphin, savedir = None):
    """docstring for save_graph_measures
    
    Args:
        graphin:
        savedir:
    Returns:
        None.
    """
    
    g = read_graph(graphin)
    
    
    
    # TODO: get frameno from graph name
    # TODO: number of edges
    # TODO: number of vertices
    # TODO: get all relevant graph measures (see separate functions)
    # save_vertex_average()
    # save_global_cluster()
    # save_local_cluster()
    # TODO: save to file (check if savefile exists, append to, etc.)
    # TODO: get threshold from graph name.
    pass


def save_graphs_list(graphdir, savedir = None):
    """ Save list of all graphs to textfile.
    
    Args:
        graphdir:
        savedir:
    Returns:
        saves textfile in savedir (or current directory if savedir == None)
    """
    
    graphdir = os.path.expanduser(graphdir)
    if not graphdir.endswith("/"):
        graphdir = graphdir + "/"
    if not savedir:
        savedir = os.getcwd()
    
    # savefile = savedir + last two directory names of graphdir because graphs are saved in color/threshold.
    typegraph = graphdir.split("/")[-3]
    threshold = graphdir.split("/")[-2]
    savefile = savedir + "/" +  typegraph + "_" + threshold + ".txt"
    print savefile
    with open(savefile, "w") as f:
        for files in sorted(glob.glob(graphdir + "*.xml.gz")):
            f.write(files.split("/")[-1] + "\n")





########################################
#####       DRAFT FUNCTIONS        #####
########################################


def global_clustering(graph):
    """This function might do something with global clustering"""
    pass


def create_graph_color_test(filename, timestamp, threshold, color = None):
    """ Creates graph from data in CSV file for each or a specific color at each timepoint.
    """
    
    # Checks if a color is entered as a parameter.
    if color:
        print "Yay, color is: " + color + "."
        # If a color is entered, build graph for only that color.
    else:
        # If no color is entered, build graphs separately for each color.
        print "Boo, you didn't enter a color!"


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


def add_weights():
    """ This should become part of the create_edges function"""
    pass
    
    # e_length[e] = distance
    
    # distlist_norm = []
    # weights = []
    
    # Need to loop over edges, and then add the weight based on normalised distance.
    # for i in range(len(distancelist)):
    #    
    #    distlist_norm.append((distancelist[i] - min(distancelist)) / 
    #                         (max(distancelist) - min(distancelist)))
    #    
    #    # Simple linear weight, inverse of normalised distance.
    #    weights.append(1 - distlist_norm[i])
    
    # print "Weights for current graph are: "
    # print weights
    

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