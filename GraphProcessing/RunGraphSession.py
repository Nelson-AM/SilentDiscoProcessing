# TODO: create script similar to RunVideoSession.py for graph processing.

import argparse
from ProcessGraphs import *

ap = argparse.ArgumentParser()

# TODO: toggle when done debugging
ap.add_argument("-cgd", "--colordir", help = "Path to color graphs directory.")
# ap.add_argument("-fcd", "--fulldir", help = "Path to full graphs directory.")
# ap.add_argument("-cgd", "--colordir", required = True, help = "Path to color graphs directory.")
# ap.add_argument("-fcd", "--fulldir", required = True, help = "Path to full graphs directory.")

args = vars(ap.parse_args())
colordir = args["colordir"]
# fulldir = args["fulldir"]

save_graphs_list(colordir)