#!/usr/bin/env python

from ProcessGraphs import *

cat = "frame"
csvbase = "/Volumes/SAMSUNG/ESCOM/csv/" + cat + "data_150"
csvext = ".csv"

dataframe = read_csv(csvbase + csvext)
x = dataframe["full_frameno"]
x = x / 25 / 60
print(dataframe.head())
ys = [dataframe["green_vertices"], 
      dataframe["red_vertices"]]
#       dataframe["blue_vertices"]]
# yerrors = [dataframe["green_" + cat + "_sd"], 
# dataframe["red_" + cat + "_sd"]]
#            dataframe["blue_" + cat + "_sd"]]

# print dataframe["green_vertices"].head()
# x = dataframe["full_frameno"]
# ys = [dataframe["green_vertices"], dataframe["red_vertices"]]#, dataframe["blue_vertices"]]
colors = ["green", "magenta"] # , "blue"]
figure, ax = setup_axes()

smoothfig = lineplot_smooth(x, ys, colors, ax, span=500)
# smootherror = lineplot_smooth(x, ys, colors, ax, span=250)
# smootherror = errorfill_smooth(x, ys, yerrors, colors, span=500, ax=ax)
    
ax.set_ylim([0, 140])
# ax.set_ylim([0, 1])
# ax.set_ylim([0, 40])
ax.set_xlim([min(x), max(x)])
# ax.set_ylim([0,15])
plt.xlabel("Time (min.)", fontsize=25)
plt.ylabel("Number of vertices", fontsize=25)
savename = "/Volumes/SAMSUNG/ESCOM_vertex_average.png"
plt.savefig(savename, bbox_inches='tight')
    
"""
for i in [150, 200, 250]:
    dataframe = read_csv(csvbase + str(i) + csvext)

    x = dataframe["full_frameno"]
    x = x / 25 / 60
    print dataframe.head()
    ys = [dataframe["green_" + cat + "_average"], 
          dataframe["red_" + cat + "_average"]] 
    #       dataframe["blue_" + cat + "_average"]]
    yerrors = [dataframe["green_" + cat + "_sd"], 
               dataframe["red_" + cat + "_sd"]]
    #            dataframe["blue_" + cat + "_sd"]]

    # print dataframe["green_vertices"].head()
    # x = dataframe["full_frameno"]
    # ys = [dataframe["green_vertices"], dataframe["red_vertices"]]#, dataframe["blue_vertices"]]
    colors = ["green", "magenta", "blue"]

    figure, ax = setup_axes()

    # smoothfig = lineplot_smooth(x, ys, colors, span=50)
    # smootherror = lineplot_smooth(x, ys, colors, ax, span=250)
    smootherror = errorfill_smooth(x, ys, yerrors, colors, span=500, ax=ax)
    
    ax.set_ylim([0, 15])
    # ax.set_ylim([0, 1])
    # ax.set_ylim([0, 40])
    ax.set_xlim([min(x), max(x)])
    # ax.set_ylim([0,15])
    plt.xlabel("Time (min.)", fontsize=25)
    plt.ylabel("Vertex average", fontsize=25)
    savename = "/Volumes/SAMSUNG/ESCOM_" + cat + "_"
    saveext = ".png"
    plt.savefig(savename + str(i) + saveext, bbox_inches='tight')


f, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, sharex='col', sharey='row')
ax1.plot(x, y)
ax1.set_title('Sharing x per column, y per row')
ax2.scatter(x, y)
ax3.scatter(x, 2 * y ** 2 - 1, color='r')
ax4.plot(x, 2 * y ** 2 - 1, color='r')
"""
