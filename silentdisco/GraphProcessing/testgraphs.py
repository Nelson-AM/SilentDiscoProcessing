#!/usr/bin/env python
import argparse
import fnmatch
import glob
import os

from silentdisco.GraphProcessing.ProcessGraphs import read_graph
from silentdisco.Utilities import printProgress

ap = argparse.ArgumentParser()

# TODO: toggle when done debugging
ap.add_argument("-wd", "--workingdir", help="Path to working directory.")

args = ap.parse_args()
workingdir = args.workingdir

if not workingdir.endswith("/"):
    workingdir = workingdir + "/"

csvdir = workingdir + "csv/"
graphdir = workingdir + "graphs/"

print("Entering directory: %s" % graphdir)
os.chdir(graphdir)
typedirs = os.listdir(os.getcwd())

for typedir in typedirs:
    if str(typedir) == "green":
        print("Entering type directory: %s" % typedir)
        os.chdir(typedir)
        thresholddirs = os.listdir(os.getcwd())
        for threshold in thresholddirs:
            print("Entering threshold directory: %s" % threshold)
            os.chdir(threshold)
            maxlength = len(fnmatch.filter(os.listdir(os.getcwd()), '*.xml.gz'))
            i = float(0)
            for filename in sorted(glob.glob("*.xml.gz")):
                try:
                    g = read_graph(filename)
                    # TODO: add progress bar tracking i over number of filenames.
                    printProgress(i, maxlength, prefix="Progress:", suffix="Complete", barLength=50)
                    i += 1
                except IOError as e:
                    print("\nError:", e)
                    continue
            os.chdir("..")
print("Going back to: %s" % graphdir)
os.chdir(graphdir)
