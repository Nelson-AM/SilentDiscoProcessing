import os
import csv
# from graph_tool.all import *


centresfile = "/Volumes/SAMSUNG/centres10frames_masked.csv"


def read_csv(filename):
    """ Mirror write_csv.
    """
    
    with open(filename, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, quoting = csv.QUOTE_ALL)
        
        spamlist = list(spamreader)
        return spamlist
        
        #for row in spamreader:
        #    print ', '.join(row)

# def read_csv_rows(filename):
#    """
#    """
    
    
centreslist = read_csv(centresfile)

for rows in centreslist:
    
    print rows[2], len(rows[2])

"""
list[frameno, color, x, y] = read(CSV)

find_threshold

for frame in frameno:
    
    g = Graph()
    
    framelist = lines(frame == frameno)
    
    for lines in framelist:
        
        v = g.add_vertex()
        
        v_x = g.new_vertex_property("int")
        v_y = g.new_vertex_property("int")
        v_color = g.new_vertex_property("str")      # character string
    
    if thresh_1 < distance(v_1, v_n) and distance(v_1, v_n) < thresh_2:
        
        g.add_edge(v_1, v_n)
        
        strength = g.new_edge_property("float")
        
        strength = e^(-lamda * distance)            # lambda being the threshold.
    
    save_network
"""
