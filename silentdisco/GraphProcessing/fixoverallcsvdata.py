import scipy as sp
import pandas as pd
import numpy as np
import os, csv
import argparse
import matplotlib.pyplot as plt

# Construct argument parser and parse arguments.
ap = argparse.ArgumentParser()

# TODO: load graphdata csv
# TODO: load raw data csv
ap.add_argument("-g", "--graphcsv", help = "Path to graph data csv file.")
ap.add_argument("-r", "--rawcsv", help = "Path to raw data csv file.")
args = vars(ap.parse_args())

graphcsv = os.path.expanduser(args["graphcsv"])
rawcsv = os.path.expanduser(args["rawcsv"])

graphdf = pd.read_csv(graphcsv)
rawdf = pd.read_csv(rawcsv)

print graphdf.head()
print rawdf.head()

# TODO: move relevant columns from fullgraph csv to respective graphdata csv
#   TODO: add relevant columns to graphdf (same thing?)
graphdf["fullframe"] = rawdf["frameno"]
graphdf["full"] = rawdf["globalcluster"]
graphdf["fullsd"] = rawdf["globalsd"]
# graphdf[""] = rawdf[""]

print len(rawdf["frameno"])
print len(graphdf["greenframe"])
print len(graphdf["redframe"])

# TODO: check if all frameno entries are the same
for i in rawdf["frameno"]:
    if not rawdf["frameno"][i] == (rawdf["frameno"][i] - 10):
        print i
        print rawdf["frameno"][i]

"""
for gframes, rframes, fframes in zip(graphdf["greenframe"], 
                                     graphdf["redframe"], 
                                     graphdf["fullframe"]):
    if not gframes == rframes:
        print "something went wrong, the red and green frames don't correspond \n"
        print "green: " + str(gframes)
        print "red: " + str(rframes)
    
    if not gframes == fframes:
        print "something went wrong, the green and full frames don't correspond \n"
        print "green: " + str(gframes)
        print "full: " + str(fframes)
    if not rframes == fframes:
        print "something went wrong, the red and full frames don't correspond \n"
        print "red: " + str(rframes)
        print "full: " + str(fframes)
    """
# TODO: if the same: prune (remove red and green, keep full frameno)
# TODO: save graphdata csv