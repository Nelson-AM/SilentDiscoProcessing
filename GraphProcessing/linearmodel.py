import scipy as sp
import pandas as pd
import numpy as np
import os, csv
import matplotlib.pyplot as plt
import argparse

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

# Read green csv into dataframe.
greendf = pd.DataFrame.from_csv(greencsv)
reddf = pd.DataFrame.from_csv(redcsv)

# Create new dataframes.
localdf = pd.DataFrame(columns = ["greenframe", "redframe", 
                                  "green", "greensd", 
                                  "red", "redsd", "segment"])
globaldf = pd.DataFrame(columns = ["greenframe", "redframe",
                                   "green", "greensd",
                                   "red", "redsd", "segment"])
#vertavdf = pd.DataFrame(columns = ["greenframe", "redframe", 
#                                   "green", "greensd", 
#                                   "red", "redsd", "segment"])

# TODO: Copy data from red and green frames to measure frames.
savedir = str(greencsv.rsplit("/", 1)[0])
print savedir

# TODO: Check names (they probably work).
localdf["greenframe"] = greendf["frameno"]
localdf["green"] = greendf["localcluster"]
localdf["greensd"] = greendf["localsd"]
localdf["redframe"] = reddf["frameno"]
localdf["red"] = reddf["localcluster"]
localdf["redsd"] = reddf["localsd"]

print localdf[0:10]

# TODO: check if column names are correct.
globaldf["greenframe"] = greendf["frameno"]
globaldf["green"] = greendf["globalcluster"]
globaldf["greensd"] = greendf["globalsd"]
globaldf["redframe"] = reddf["frameno"]
globaldf["red"] = reddf["globalcluster"]
globaldf["redsd"] = reddf["globalsd"]

print globaldf[0:10]

# TODO: Fix column names.
vertavdf["greenframe"] = greendf["frameno"]
vertavdf["green"] = greendf["localcluster"]
vertavdf["greensd"] = greendf["localsd"]
vertavdf["redframe"] = reddf["frameno"]
vertavdf["red"] = reddf["localcluster"]
vertavdf["redsd"] = reddf["localsd"]

print vertavdf[0:10]


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