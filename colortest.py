#!/usr/bin/env python
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

def get_n_vertices_color(graphin):
    """ Reads _full_ graph and returns number of vertices per color. """
    
    colors = ["red", "green", "blue"]
    counts = 
    g = read_graph(graphin)
    
    for v in g.vertices():
        for color in colors:
            if g.vp.color[v] == color:
                pass
                # TODO: update counts per color
    
    # TODO: return counts per color

filename = "~/Documents/PYTHON/SilentDiscoProcessing/graph_000150_150.xml.gz"
get_n_vertices_color(filename)