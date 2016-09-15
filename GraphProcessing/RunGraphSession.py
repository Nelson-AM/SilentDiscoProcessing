# TODO: create script similar to RunVideoSession.py for graph processing.

import argparse
from ProcessGraphs import *

ap = argparse.ArgumentParser()

# TODO: toggle when done debugging
ap.add_argument("-wd", "--workingdir", help="Path to graphs directory.")
# parser.add_argument("integers", metavar="N", type=int, nargs="+", help="an integer for the accumulator")
# ap.add_argument("-cgd", "--colordir", help = "Path to color graphs directory.")
# ap.add_argument("-fcd", "--fulldir", help = "Path to full graphs directory.")
# ap.add_argument("-cgd", "--colordir", required = True, help = "Path to color graphs directory.")
# ap.add_argument("-fcd", "--fulldir", required = True, help = "Path to full graphs directory.")

args = ap.parse_args()
workingdir = args.workingdir

if not workingdir.endswith("/"):
    workingdir = workingdir + "/"

csvdir = workingdir + "csv/"
graphdir = workingdir + "graphs/"

"""
reddir = graphdir + "red/"
greendir = graphdir + "green/"
fulldir = graphdir + "full/"

thresholds = [50, 100, 150, 200, 250, 300, 350, 400]


for threshold in thresholds:
    save_graphs_list(reddir + str(threshold) + "/")
    save_graphs_list(greendir + str(threshold) + "/")
    save_graphs_list(fulldir + str(threshold) + "/")

# Specify thresholds to make sure not all folders are done (saves time and resources).
thresholds = [150, 200, 250]
# TODO: add prompt?
# Loop over all (relevant) thresholds and 

for threshold in thresholds:
    
    # TODO: update directory name to fit with the actual directories (red, ..., full).
    for filename in sorted(glob.glob(directory) + str(threshold) + "/*.xml.gz"):
        
        
        # TODO: get frame number from file, take into account (currently existing) differences
        # between color graphs and full graphs.
        # TODO: get type from file so 
        # TODO: in graph creation, make sure every graph follows the same pattern
        #   graphname_graphtype_frameno_threshold.xml.gz
        # TODO: save graph measures, take into account the graph type and threshold.
"""



print("Entering directory: %s" % graphdir)
os.chdir(graphdir)
typedirs = os.listdir(os.getcwd())

for typedir in typedirs:
    print("Entering type directory: %s" % typedir)
    os.chdir(typedir)
    
    thresholddirs = os.listdir(os.getcwd())
    
    for threshold in thresholddirs:
        print("Entering threshold directory: %s" % threshold)
        
        framedf = pd.DataFrame(columns = [typedir + "_frameno", 
                                          typedir + "_vertices", 
                                          typedir + "_edges"])
        localdf = pd.DataFrame(columns = [typedir + "_local_cluster", 
                                          typedir + "_local_sd"])
        globaldf = pd.DataFrame(columns = [typedir + "_global_cluster",
                                           typedir + "_global_sd"])
        vertavdf = pd.DataFrame(columns = [typedir + "_vertex_average",
                                           typedir + "_vertex_sd"])
        
        
        for filename in sorted(glob.glob(threshold + "/*.xml.gz")):
            g = read_graph(filename)
            frameno = get_frameno(filename)
            n_edge = get_n_vertices(g)
            n_vert = get_n_edges(g)
            localc, localsd = get_local_cluster(g)
            globalc, globalsd = get_global_cluster(g)
            vertexa, vertexsd = get_vertex_average(g)
            
            framedf.append({typedir + "_frameno": frameno,
                            typedir + "_vertices": n_edge,
                            typedir + "_edges": n_vert})
            localdf.append({typedir + "_local_cluster": localc,
                            typedir + "_local_sd": localsd})
            globaldf.append({typedir + "_global_cluster": globalc,
                             typedir + "_global_sd": globalsd})
            vertavdf.append({typedir + "_vertex_average": vertexa,
                             typedir + "_vertex_sd": vertexsd})
        
        # TODO: save dataframes.
        print("Going up one directory, back to type.")
        os.chdir("..")
    
    print("Going back to: %s" % graphdir)
    os.chdir(graphdir)

