#!/usr/bin/env python

# TODO: create script similar to RunVideoSession.py for graph processing.

import argparse
import fnmatch
import pandas as pd
import numpy as np
import os 
import glob

workingdir = "/Volumes/SAMSUNG/MOSI/"
csvdir = workingdir + "csv/"

thresholds = ["150", "200", "250"]
for threshold in thresholds:
    # get frame data
    # ff = pd.read_csv(csvdir + "framedata_full_" + threshold + ".csv")
    gf = pd.read_csv(csvdir + "framedata_green_" + threshold + ".csv")
    rf = pd.read_csv(csvdir + "framedata_red_" + threshold + ".csv")
    bf = pd.read_csv(csvdir + "framedata_blue_" + threshold + ".csv")
    
    # get local, global, vertex data
    # fl = pd.read_csv(csvdir + "localdata_full_" + threshold + ".csv")
    gl = pd.read_csv(csvdir + "localdata_green_" + threshold + ".csv")
    rl = pd.read_csv(csvdir + "localdata_red_" + threshold + ".csv")
    bl = pd.read_csv(csvdir + "localdata_blue_" + threshold + ".csv")
    
    # fg = pd.read_csv(csvdir + "globaldata_full_" + threshold + ".csv")
    gg = pd.read_csv(csvdir + "globaldata_green_" + threshold + ".csv")
    rg = pd.read_csv(csvdir + "globaldata_red_" + threshold + ".csv")
    bg = pd.read_csv(csvdir + "globaldata_blue_" + threshold + ".csv")
    
    # fv = pd.read_csv(csvdir + "vertexdata_full_" + threshold + ".csv")
    gv = pd.read_csv(csvdir + "vertexdata_green_" + threshold + ".csv")
    rv = pd.read_csv(csvdir + "vertexdata_red_" + threshold + ".csv")
    bv = pd.read_csv(csvdir + "vertexdata_blue_" + threshold + ".csv")
    
    gf = gf.rename(columns={"green_frameno": "full_frameno"})
    
    gf.reset_index(inplace=True)
    rf.reset_index(inplace=True)
    bf.reset_index(inplace=True)
    gl.reset_index(inplace=True)
    rl.reset_index(inplace=True)
    bl.reset_index(inplace=True)
    gg.reset_index(inplace=True)
    rg.reset_index(inplace=True)
    bg.reset_index(inplace=True)
    gv.reset_index(inplace=True)
    rv.reset_index(inplace=True)
    bv.reset_index(inplace=True)
    
    framedata = pd.merge(pd.merge(gf, rf), bf)
    localdata = pd.merge(pd.merge(gl, rl), bl)
    globaldata = pd.merge(pd.merge(gg, rg), bg)
    vertexdata = pd.merge(pd.merge(gv, rv), bv)
    localdata["full_frameno"] = gf["full_frameno"]
    globaldata["full_frameno"] = gf["full_frameno"]
    vertexdata["full_frameno"] = gf["full_frameno"]
    del framedata["index"]
    del framedata["Unnamed: 0"]
    del framedata["red_frameno"]
    del framedata["blue_frameno"]
    
    del localdata["index"]
    del localdata["Unnamed: 0"]
    
    del globaldata["index"]
    del globaldata["Unnamed: 0"]
    
    del vertexdata["index"]
    del vertexdata["Unnamed: 0"]
    
    framename = csvdir + "framedata_" + threshold + ".csv"
    localname = csvdir + "localdata_" + threshold + ".csv"
    globalname = csvdir + "globaldata_" + threshold + ".csv"
    vertexname = csvdir + "vertexdata_" + threshold + ".csv"
    
    framedata.to_csv(framename)
    localdata.to_csv(localname)
    globaldata.to_csv(globalname)
    vertexdata.to_csv(vertexname)