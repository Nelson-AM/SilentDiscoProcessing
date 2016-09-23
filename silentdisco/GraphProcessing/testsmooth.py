#!/usr/bin/env python

from ProcessGraphs import *

csvfile = "/Volumes/SAMSUNG/ESCOM/globaldata_150.csv"

smoothdf = save_smooth_data(csvfile, 100)
print smoothdf.head()