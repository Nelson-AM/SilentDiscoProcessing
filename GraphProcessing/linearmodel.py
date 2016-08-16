import scipy as sp
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# library(car)
# library(heplots)

# TODO: Read data from pandas dataframe (saved as CSV)
# TODO: Restructure dataframe as follows (one df per measure):
#       time, green-measure, green-sd, red-measure, red-sd, hour (or other time-segments)
# TODO: Rewrite graph -> csv functions with this structure.

# redpath <- "/Volumes/SAMSUNG/csv/reddata_t150.csv"
# greenpath <- "/Volumes/SAMSUNG/csv/greendata_t150.csv"
# reddata <- read.csv(redpath, header = T, dec = ".", sep = ",")
# greendata <- read.csv(greenpath, header = T, dec = ".", sep = ",")

# print(reddata)

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