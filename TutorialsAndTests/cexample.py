
# import graph_tool as gt
from graph_tool.all import *

g = random_graph(1000, lambda: (5,5))
clust = local_clustering(g)
