# TODO: create script similar to ProcessVideo.py for graph processing.
import os, shutil, glob, csv, sys
import numpy as np
import pandas as pd

from graph_tool.all import *
from matplotlib import pyplot as plt





################################################
#####          GENERAL TO-DO LIST          #####
################################################


# NOTE: Also check design notes in notebook.
# TODO: Add and complete docstrings for functions.
# TODO: Add edge weight as graph property.
# TODO: Make every call relative to a project directory (e.g. ESCOM).




################################################
#####     FILE INPUT + OUTPUT + SAVING     #####
################################################


def read_csv(filename):
    """ Read CSV file and return it as a pandas dataframe.
    """
    
    if isinstance(filename, str):
        filename = os.path.expanduser(filename)
        # TODO: simplify using Pandas built-in from.csv
        with open(filename, "rb") as csvfile:
            spamreader = csv.reader(csvfile, quoting = csv.QUOTE_ALL)
            spamlist = list(spamreader)
            dataframe = pd.DataFrame(spamlist, columns = ["Timestamp", "Color", "X", "Y"])
        return dataframe
    else:
        return filename


def read_graph(graphin):
    """ Reads graph from .xml.gz file
    """
    
    if isinstance(graphin, str):
        graphin = os.path.expanduser(graphin)
        return load_graph(graphin)
    else:
        return graphin


def save_graph(g, name, threshold, graphdir = None):
    """ Saves graph g, including properties of vertices and edges.
    
    Args:
        g
        name
        threshold
        graphdir
    """
    
    if graphdir:
        graphdir = os.path.expanduser(graphdir)
        # Build filename based on graphdir, name and threshold.
        graphnamegz = graphdir + "/graph_" + str(name) + "_" + str(threshold) + ".xml.gz"
    else:
        # Build filename based on name and threshold, saves to current working directory.
        graphnamegz = "graph_" + str(name) + "_" + str(threshold) + ".xml.gz"
    print graphnamegz
    # Now we can save it.
    g.save(graphnamegz)


def save_graph_img(g, name, threshold, graphdir = None):
    """ Saves png image of graph g with vertices at "real" locations.
    
    Plots vertices based on x- and y-coordinates, making visualisation correspond to real-life 
    situation.
    
    Args:
    Returns:
    """
    
    # TODO: take into account edge weight (line thickness or opacity)
    # TODO: fill in vertices as color that they represent.
    
    if isinstance(g, basestring):
        g = load_graph(g, directed = False)
    if graphdir:
        graphdir = os.path.expanduser(graphdir)
        print graphdir
        graphnameim = graphdir + "/graph_" + str(name) + "_" + str(threshold) + ".png"
    else:
        graphnameim = "graph_" + str(name) + "_" + str(threshold) + ".png"
    print graphnameim
    pos = g.vertex_properties["pos"]
    color = g.vertex_properties["color"]
    
    graph_draw(g, pos, output_size = (1920, 1080), 
               fit_view = False,
               vertex_color = color,
               vertex_fill_color = color,
               vertex_size = 5, edge_pen_width = 1.2, 
               vcmap = plt.cm.gist_heat_r, output = graphnameim)


def image_graph(filename, outdir = None):
    """ Takes a saved graph and saves it as an image.
    
    Args:
    Returns:
    """
    
    if outdir:
        if not os.path.isdir(outdir):
            os.mkdir(outdir)
        fileext = filename.split("/")[-1]
        filename = fileext.split(".")[0]
        graphnameim = outdir + filename + ".png"
        # print graphnameim
    else:
        filename = filename.split(".")[0]
        graphnameim = filename + ".png"
        print graphnameim
    g = load_graph(filename)
    x = g.vertex_properties["x"]
    y = g.vertex_properties["y"]
    color = g.vertex_properties["color"]
    pos = g.vertex_properties["pos"]
    
    graph_draw(g, pos, output_size = (1920, 1080),
               fit_view = False,
               vertex_color = color,
               vertex_fill_color = color,
               vertex_size = 10, edge_pen_width = 1.2,
               bg_color = [1, 1, 1, 1],
               output = graphnameim)


def create_df(savedir = None, colors = None):
    """ Creates a pandas data frame for saving graph measures.
    
    Args:
        savedir: directory to save "fulldata.csv" (optional). Defaults to current working directory.
        colors: the colors for which data exists (optional). Defaults to ["red", "blue", "green", 
                "full"]
    Returns:
        saves dataframe to savedir + "fulldata.csv"
    """
    
    if not savedir:
        savedir = os.getcwd()
    if not colors:
        colors = ["red", "blue", "green", "full"]
    if savedir.endswith("/"):
        filename = savedir + "fulldata.csv"
    else:
        filename = savedir + "/fulldata.csv"
    values = ["n_vertices", "n_edges",
              "local_clustering", "local_sd",
              "global_clustering", "global_sd",
              "vertex_average", "vertex_sd"]
    # TODO: check if indexing and other parameters are necessary to set beforehand.
    df1 = pd.DataFrame(columns = ["Frameno"])
    # df1 = df1.set_index("Frameno")
    for color in colors:
        for value in values:
            df1[value + "_" + color] = ""
    df1.to_csv(filename)



##################################
#####     GRAPH BUILDING     #####
##################################


def create_vertices(g, clist, xlist, ylist):
    """ Support function, creates vertices for graph g from create_graphs.
    """
    
    vlist = []
    dlist = []
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
    g.vertex_properties["pos"] = pos
    
    return vlist, v_x, v_y


def create_edges(g, vlist, v_x, v_y, threshold):
    """ Support function, creates edges for graph g from create_graphs.
    """
    
    # TODO: add weight as edge property (proportional to euclidian distance)
    e_length = g.new_edge_property("double")
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


def create_base_graph(dataframe, name, threshold, graphdir = None):
    """ Base function that creates the graph and saves it.
    """
    
    g = Graph(directed = False)
    
    clist = dataframe["Color"].tolist()
    xlist = dataframe["X"].tolist()
    ylist = dataframe["Y"].tolist()
    
    vlist, v_x, v_y = create_vertices(g, clist, xlist, ylist)
    create_edges(g, vlist, v_x, v_y, threshold)
    
    if graphdir:
        save_graph_img(g, name, threshold, graphdir)
        save_graph(g, name, threshold, graphdir)
    else:
        # v_color, v_x, v_y, pos, e_weight
        save_graph(g, name, threshold)
        save_graph_img(g, name, threshold)
    
    return g


def create_graph(filename, timestamp, threshold, graphdir = None):
    """ Takes data from CSV file and creates graph for given timestamp.
    
    Single-use case of greate_graphs.
    """
    
    centresdf = read_csv(filename)
    timedf = centresdf.loc[centresdf["Timestamp"] == str(timestamp)]
    
    if graphdir:
        g = create_base_graph(timedf, timestamp, threshold, graphdir)
    else:
        g = create_base_graph(timedf, timestamp, threshold)


def create_graphs(filename, threshold, graphdir = None):
    """ Creates graph from data in CSV file for each timepoint.
    """
    
    centresdf = read_csv(filename)
    
    for time, group in centresdf.groupby("Timestamp"):
        if graphdir:
            create_base_graph(group, time, threshold, graphdir)
        else:
            create_base_graph(group, time, threshold)


def create_graph_color(filename, timestamp, threshold, color, graphdir = None):
    """ Creates graph from data in CSV file for specified timepoint and color.
    """
    
    centresdf = read_csv(filename)
    
    timedf = centresdf.loc[centresdf["Timestamp"] == str(timestamp)]
    timecolordf = timedf.loc[timedf["Color"] == color]
    
    graphname = color + "_" + str(timestamp)
    if graphdir:
        g = create_base_graph(timecolordf, graphname, threshold, graphdir)
    else:
        g = create_base_graph(timecolordf, graphname, threshold)
    
    return g


def create_graphs_color(filename, threshold, color = None, graphdir = None):
    """ Creates graph from data in CSV file for each or a specific color at each timepoint.
    """
    
    centresdf = read_csv(filename)
    
    if color:
        # If a color is entered, build graph for only that color.
        # Note: is str(color) necessary?
        colordf = centresdf.loc[centresdf["Color"] == str(color)]
        
        for name, group in colordf.groupby("Timestamp"):
            cname = name + "_" + color
            
            if graphdir:
                create_base_graph(group, cname, threshold, graphdir)
            else:
                create_base_graph(group, cname, threshold)
    
    else:
        # If no color is entered, build separate graphs for each color.
        colors = ["red", "green", "blue"]
        for color in colors:
            colordf = centresdf.loc[centresdf["Color"] == color]
            
            for name, group in colordf.groupby("Timestamp"):
                cname = name + "_" + color
                
                if graphdir:
                    create_base_graph(group, cname, threshold, graphdir)
                else:
                    create_base_graph(group, cname, threshold)





#######################################
#####     STRUCTURAL ANALYSIS     #####
#######################################


def get_frameno(graphin):
    """ Extract frameno from filename. """
    
    if not isinstance(graphin, str):
        raise TypeError("Graphin must be a string.")
    
    frameno = graphin.split("_")[-2]
    return frameno


def get_n_vertices(graphin):
    """ Reads graphs and returns number of vertices.
    
    Args:
    Returns:
    """
    
    g = read_graph(graphin)
    return g.num_vertices()


def get_n_edges(graphin):
    """ Reads graphs and returns number of edges.
    
    Args:
    Returns:
    """
    
    g = read_graph(graphin)
    return g.num_edges()


def get_local_cluster(graphin):
    """docstring for save_local_clust
    
    Args:
        graphin:
        savedir:
    Returns:
        localc
        localsd
    """
    
    # TODO: write save_local_cluster to save data to file.
    
    g = read_graph(graphin)
    
    if get_n_vertices(g) > 0:
        cluster = local_clustering(g)
        (localc, localsd) = vertex_average(g, cluster)
    elif get_n_vertices(graphin) == 0:
        localc = float("NaN")
        localsd = float("NaN")
    
    return localc, localsd

                
def get_global_cluster(graphin):
    """docstring for save_global_clust
    
    Args:
        graphin:
    Returns:
        globalc
        globalsd
    """
    
    # TODO: write save_global_cluster to save data to file.
    
    g = read_graph(graphin)
    (globalc, globalsd) = global_clustering(g)
    
    return globalc, globalsd


def get_vertex_average(graphin):
    """docstring for save_vertex_average
    
    Args:
        graphin:
    Returns:
        vertexav
        vertexsd
    """
    
    # TODO: write save_vertex_average to save data to file.
    g = read_graph(graphin)
    
    if get_n_vertices(g) > 0:
        (vertexav, vertexsd) = vertex_average(g, "total")
    elif get_n_vertices(graphin) == 0:
        vertexav = float("NaN")
        vertexsd = float("NaN")
    
    return vertexav, vertexsd


def save_graph_measures(graphin, savedir = None):
    """docstring for save_graph_measures
    
    FULL graphs only.
    
    Args:
        graphin:
    Returns:
        None.
    """
    
    g = read_graph(graphin)
    
    # TODO: get frameno from graph name
    frameno = graphin.split("_")[-2]
    
    n_edges = get_n_edges(g)
    n_vertices = get_n_vertices(g)
    localc, localsd = get_local_cluster(g)
    globalc, globalsd = get_global_cluster(g)
    vertexav, vertexsd = get_vertex_average(g)
    
    threshold = graphin.split("_")[-1].split(".")[0]
    
    if savedir:
        csvfile = savedir + "graphdata_full_" + threshold + ".csv"
    else:
        csvfile = "graphdata_full_" + threshold + ".csv"
    
    # TODO: save to file (check if savefile exists, append to, etc.)
    if exists(csvfile):
        with open_csvfile as bla:
            append_data_to_file = []
    else:
        # create_csvfile (assign columns)
        with open_csvfile as bla:
            append_data_to_file = []





def save_graphs_list(graphdir, savedir = None):
    """ Save list of all graphs to textfile.
    """
    
    # TODO: add threshold subdirectory support.
    
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
#####         MISC SUPPORT         #####
########################################


def printProgress(iteration, total, prefix = "", suffix = "", decimals = 1, barLength = 100):
    """ Call in a loop to create terminal progress bar.
    
    Params:
        iteration
        total
        prefix
        suffix
        decimals
        barLength
    """
    
    formatStr = "{0:." + str(decimals) + "f}"
    percents = formatStr.format(100 * (iteration / float(total)))
    filledLength = int(round(barLength * iteration / float(total)))
    bar = "X" * filledLength + "=" * (barLength - filledLength)
    sys.stdout.write("\r%s |%s| %s%s %s" % (prefix, bar, percents, "%", suffix)),
    sys.stdout.flush()
    
    if iteration == total:
        sys.stdout.write("\n")
        sys.stdout.flush()



########################################
#####       DRAFT FUNCTIONS        #####
########################################





def get_n_vertices_color():
    """ Reads _full_ graph and returns number of vertices per color. """
    
    colors = [red, green, blue]
    g = read_graph(graphin)
    
    for color in colors:
        pass
        # Return vertices with correct color propertymap.


# def global_clustering(graph):
#    """This function might do something with global clustering"""
#    pass


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