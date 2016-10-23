#!/usr/bin/env python

from ProcessGraphs import *

csvfile = "/Volumes/SAMSUNG/MOSI/csv/globaldata_150.csv"

dataframe = read_csv(csvfile)

x = dataframe["full_frameno"]
x = x/25
print dataframe.head()
ys = [dataframe["green_global_cluster"], 
      dataframe["red_global_cluster"], 
      dataframe["blue_global_cluster"]]
yerrors = [dataframe["green_global_sd"], 
           dataframe["red_global_sd"],
           dataframe["blue_global_sd"]]

# print dataframe["green_vertices"].head()
# x = dataframe["full_frameno"]
# ys = [dataframe["green_vertices"], dataframe["red_vertices"]]#, dataframe["blue_vertices"]]
colors = ["green", "magenta", "blue"]

figure, ax = setup_axes()

# smoothfig = lineplot_smooth(x, ys, colors, span=50)
# smootherror = lineplot_smooth(x, ys, colors, ax, span=250)
smootherror = errorfill_smooth(x, ys, yerrors, colors, span=500, ax=ax)

ax.set_ylim([0,1])
ax.set_xlim([min(x), max(x)])
# ax.set_ylim([0,15])
plt.xlabel("Time (min.)")
plt.ylabel("Global clustering")
plt.savefig("/Volumes/SAMSUNG/MOSI_global_150.png")