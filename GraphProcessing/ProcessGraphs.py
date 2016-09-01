# TODO: create script similar to ProcessVideo.py for graph processing.
import os, csv, shutil, glob
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