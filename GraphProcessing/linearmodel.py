import scipy as sp
import pandas as pd
import numpy as np
import os, csv
import argparse
import matplotlib.pyplot as plt

from matplotlib.pylab import rcParams
rcParams['figure.figsize'] = 15, 6

# TODO: check if scipy, numpy, pandas and matplotlib have the same functionality as these R packages.
# They probably do.
# library(car)
# library(heplots)

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
greendf = pd.read_csv(greencsv, index_col = "frameno")
reddf = pd.read_csv(redcsv, index_col = "frameno")

gts = greendf["localcluster"]
rts = reddf["localcluster"]

plt.plot(gts)
plt.show()
plt.plot(rts)
plt.show()
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
print savedir

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

print localdf.head()
print "\n Data Types:"
print localdf.dtypes


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

# TODO: define segment (can also be done in the model creation based on the index)
# TODO: Save dataframes for testing.


# TODO: create linear model in scipy function.
# A typical model (first variable of lm) has the following form:
# 	response ~ terms
# where response is the (numeric) response vector and terms is a series of terms which specifies a linear predictor for response.  A terms specification of the form first * second

# Response is a vector of values for a channel (in a given time segment).
# Terms is two things: 
# myfit <- lm(dependent_variable ~ channel * time_segment, data = mydata)

# TODO: anova and py-equivalent of etasq for the fitted model.
# Anova(my_fit)
# etasq(my_fit, type = 2)