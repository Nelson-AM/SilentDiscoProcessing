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

def set_n_vertices_color(graphin, colors = None):
    """ Read _full_ graph and save number of vertices per color as propertymap.
    
    Adds values to existing graph.  Need to update this so it also works in creating graphs (so 
    basically skip the graph reading, just set the properties).
    """
    
    if colors is None:
        colors = ["red", "green", "blue"]
    
    for color in colors:
        
        colornum = g.new_graph_property("int")
        g.graph_properties[color] = colornum
        
        count = 0
        
        for v in g.vertices():
            if g.vp.color[v] == color:
                count += 1
        
        g.graph_properties[color] = count


def get_n_vertices_color(graphin):
    """ Reads _full_ graph and returns number of vertices per color. """
    
    colors = ["red", "green", "blue"]
    g = read_graph(graphin)
    
    for v in g.vertices():
        for color in colors:
            if g.vp.color[v] == color:
                
                pass
                # TODO: update counts per color and save in array.
                
                # TODO: separate function for adding and extracting the values?
                # TODO: requires saving the graph again. Not as useful for extracting the data.
                
    
    # TODO: return counts per color

filename = "~/Documents/PYTHON/SilentDiscoProcessing/graph_000150_150.xml.gz"
get_n_vertices_color(filename)