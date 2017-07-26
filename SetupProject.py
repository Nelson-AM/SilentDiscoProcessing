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
    else:
        print "Main working directory %s already exists." % maindir

    # Define and add subdirectories
    directories = ["csv", "frames", "graphs", "masks", "music", "plots", "video"]

    for directory in directories:
        if not os.path.isdir(maindir + directory):
            os.mkdir(maindir + directory)
        else:
            print "Subdirectory %s already exists." % directory

if __name__ == "__main__":
    import argparse

    ap = argparse.ArgumentParser()

    ap.add_argument("-wd", "--workingdir", required=True, help="Path to working directory.")

    args = vars(ap.parse_args())
    workingdir = args["workingdir"]

    setup_directories(workingdir)
