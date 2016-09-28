#!/usr/bin/env python

from ProcessGraphs import *

csvfile = "/Volumes/SAMSUNG/ESCOM/localdata_150.csv"

dataframe = read_csv(csvfile)

x = dataframe["full_frameno"]
ys = [dataframe["green_local_cluster"], dataframe["red_local_cluster"]]
yerrors = [dataframe["green_local_sd"], dataframe["red_local_sd"]]
# print dataframe["green_vertices"].head()
# x = dataframe["full_frameno"]
# ys = [dataframe["green_vertices"], dataframe["red_vertices"]]
colors = ["green", "magenta"]

# smoothfig = lineplot_smooth(x, ys, colors, span=50)
smootherror = errorfill_smooth(x, ys, yerrors, colors, span=500)