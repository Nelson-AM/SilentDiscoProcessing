import scipy as sp
import pandas as pd
import numpy as np
import os, csv
import argparse
import matplotlib.pyplot as plt

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

# Construct argument parser and parse arguments.
ap = argparse.ArgumentParser()

ap.add_argument("-g", "--greencsv", help = "Path to green csv file.")
ap.add_argument("-r", "--redcsv", help = "Path to red csv file.")
args = vars(ap.parse_args())

greencsv = args["greencsv"]
redcsv = args["redcsv"]

greencsv = os.path.expanduser(greencsv)
redcsv = os.path.expanduser(redcsv)

# Read read and green csv into dataframe.
greendf = pd.read_csv(greencsv) #, index_col = "frameno")
reddf = pd.read_csv(redcsv) #, index_col = "frameno")

# Create new dataframes.
"""
localdf = pd.DataFrame(columns = ["greenframe", "redframe", 
                                  "green", "greensd", 
                                  "red", "redsd", "segment"])
globaldf = pd.DataFrame(columns = ["greenframe", "redframe",
                                   "green", "greensd",
                                   "red", "redsd", "segment"])
vertavdf = pd.DataFrame(columns = ["greenframe", "redframe", 
                                   "green", "greensd", 
                                   "red", "redsd", "segment"])
"""

savedir = str(greencsv.rsplit("/", 1)[0])
threshold = str(greencsv.rsplit("_", 1)[-1])
print savedir
print threshold

# Check if the index columns (frameno) are the same for red and green.
"""
for gframes, rframes in zip(greendf["frameno"], reddf["frameno"]):
    if not gframes == rframes:
        print "something went wrong, the frames are unequal \n"
        print "green: " + str(gframes)
        print "red: " + str(rframes)
"""

"""
localdf["greenframe"] = greendf["frameno"]
localdf["green"] = greendf["localcluster"]
localdf["greensd"] = greendf["localsd"]
localdf["redframe"] = reddf["frameno"]
localdf["red"] = reddf["localcluster"]
localdf["redsd"] = reddf["localsd"]

globaldf["greenframe"] = greendf["frameno"]
globaldf["green"] = greendf["globalcluster"]
globaldf["greensd"] = greendf["globalsd"]
globaldf["redframe"] = reddf["frameno"]
globaldf["red"] = reddf["globalcluster"]
globaldf["redsd"] = reddf["globalsd"]

vertavdf["greenframe"] = greendf["frameno"]
vertavdf["green"] = greendf["localcluster"]
vertavdf["greensd"] = greendf["localsd"]
vertavdf["redframe"] = reddf["frameno"]
vertavdf["red"] = reddf["localcluster"]
vertavdf["redsd"] = reddf["localsd"]
"""

localpath = savedir + "local_clustering_" + threshold
globalpath = savedir + "global_clustering_" + threshold
vertavpath = savedir + "vertex_average_" + threshold

localdf.to_csv(localpath)
globaldf.to_csv(globalpath)
vertavdf.to_csv(vertavpath)
