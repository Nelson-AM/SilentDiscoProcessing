#!/usr/bin/env python
import os

def setup_directories(maindir):
    """docstring for setup_directories"""
    
    directories = ["csv", "frames", "graphs", "masks", "music", "plots", "video"]
    
    if not maindir.endswith("/"):
        maindir = maindir + "/"
    
    for directory in directories:
        if not os.path.exists(maindir + directory):
            os.mkdir(maindir + directory)