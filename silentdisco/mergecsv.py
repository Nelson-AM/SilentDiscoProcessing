#!/usr/bin/env python

# TODO: create script similar to RunVideoSession.py for graph processing.

import argparse
import fnmatch
import pandas as pd
import numpy as np
import os 
import glob

workingdir = "/Volumes/WDE/ESCOM/"
csvdir = workingdir + "csv/"

thresholds = ["150", "200", "250"]
for threshold in thresholds:
    # get frame data
    ff = pd.read_csv(csvdir + "framedata_full_" + threshold + ".csv")
    gf = pd.read_csv(csvdir + "framedata_green_" + threshold + ".csv")
    rf = pd.read_csv(csvdir + "framedata_red_" + threshold + ".csv")
    
    # get local, global, vertex data
    fl = pd.read_csv(csvdir + "localdata_full_" + threshold + ".csv")
    gl = pd.read_csv(csvdir + "localdata_green_" + threshold + ".csv")
    rl = pd.read_csv(csvdir + "localdata_red_" + threshold + ".csv")
    
    fg = pd.read_csv(csvdir + "globaldata_full_" + threshold + ".csv")
    gg = pd.read_csv(csvdir + "globaldata_green_" + threshold + ".csv")
    rg = pd.read_csv(csvdir + "globaldata_red_" + threshold + ".csv")
    
    fv = pd.read_csv(csvdir + "vertexdata_full_" + threshold + ".csv")
    gv = pd.read_csv(csvdir + "vertexdata_green_" + threshold + ".csv")
    rv = pd.read_csv(csvdir + "vertexdata_red_" + threshold + ".csv")
    
    frameno = ff
    # del frameno["full_vertices"]
    # del frameno["full_edges"]
    combined = pd.merge(pd.merge(pd.merge(ff, fv), gv), rv)
    print combined.head()
    del combined["Unnamed: 0"]
    del combined["full_vertices"]
    del combined["full_edges"]
    print combined.head()
    
    filename = workingdir + "vertexdata_" + threshold + ".csv"
    combined.to_csv(filename)



    # clocal = pd.merge(pd.merge(fl, gl), rl)
    # cglobal = pd.merge(pd.merge(fg, gg), rg)
    # cvertex = pd.merge(pd.merge(fv, gv), rv)
    
    # combinedlocal = pd.merge(ff, clocal)
    # combinedglobal = pd.merge(ff, cglobal)
    # combinedvertex = pd.merge(ff, cvertex)
    # at = pd.merge(pd.merge(f, r), g)
    # print at.head()

    # at["f_g"] = np.where(at["full_frameno"] == at["green_frameno"], 1, 0)
    # at["f_r"] = np.where(at["full_frameno"] == at["red_frameno"], 1, 0)


    # at_unequal_fg = at.loc[at["f_g"] == 0]
    # at_unequal_fr = at.loc[at["f_r"] == 0]

    # at_unequal_fg.to_csv(csvdir + "uneq_fg.csv")
    # at_unequal_fr.to_csv(csvdir + "uneq_fr.csv")