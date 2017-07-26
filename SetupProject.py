#!/usr/bin/env python
"""Sets up directory structure. Might do more in the future"""

import os


def setup_directories(maindir):
    """Create directory structure used by rest of the software."""

    # Make sure given path ends with a slash.
    if not maindir.endswith("/"):
        maindir = maindir + "/"

    # Check if given directory exists, of it doesnt: create it.
    if not os.path.isdir(maindir):
        os.mkdir(maindir)

    # Define and add subdirectories
    directories = ["csv", "frames", "graphs", "masks", "music", "plots", "video"]

    for directory in directories:
        os.mkdir(maindir + directory)

if __name__ == "__main__":
    import argparse
    
    ap = argparse.ArgumentParser()
    
    ap.add_argument("-wd", "--workingdir", type=str, help="Path to working directory.")
    
    args = vars(ap.parse_args())
    workingdir = args["workingdir"]

    setup_directories(workingdir)
