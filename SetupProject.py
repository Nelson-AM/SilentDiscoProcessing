#!/usr/bin/env python
import os
import argparse
import fnmatch
from ProcessGraphs import *

ap = argparse.ArgumentParser()

ap.add_argument("-wd", "--workingdir", help="Path to working directory.")

workingdir = args["workingdir"]

def setup_directories(workingdir):
    """Create directory structure used by rest of the software."""
    
    # Make sure given path ends with a slash.
    if not workingdir.endswith("/"):
        workingdir = workingdir + "/"
    
    # Check if given directory exists, of it doesnt: create it.
    if not os.path.isdir(workingdir):
        os.mkdir(workingdir)
    
    # Define and add subdirectories
    directories = ["csv", "frames", "graphs", "masks", "music", "plots", "video"]

    for directory in directories:
            os.mkdir(workingdir + directory)