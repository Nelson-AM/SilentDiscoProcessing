# We will need some things from several places.
from __future__ import division, absolute_import, print_function
import sys
if sys.version_info < (3,):
    range = xrange
import os
from pylab import *             # For plotting
from numpy.random import *      # For random sampling

seed(42)

# Import the graph_tool module itself
from graph_tool.all import *

# Start with an empty, directed graph
g = Graph()

# Create property maps to save age information for each vertex and edge.
v_age = g.new_vertex_property("int")
e_age = g.new_edge_property("int")

# Final size of network
N = 100000

# Start with one vertex.
v = g.add_vertex()
v_age[v] = 0

# Make list of vertices.
vlist = [v]

# Add new edges and vertices.
for i in range(1, N):
    
    # Create new vertex.
    v = g.add_vertex()
    v_age[v] = i
    
    # Randomly sample a vertex from vlist.
    i = randint(0, len(vlist))
    target = vlist[i]
    
    # Add edge
    e = g.add_edge(v, target)
    e_age[e] = i
    
    # Put v and target in the list.
    vlist.append(target)
    vlist.append(v)

# Random walk on the graph, print age of vertices we encounter
v = g.vertex(randint(0, g.num_vertices()))

while True:
    print("vertex:", int(v), "in-degree:", v.in_degree(), 
          "out-degree:", v.out_degree(), "age", v_age[v])
    
    if v.out_degree() == 0:
        print("Nowhere else to go... We found the main hub!")
        break
    
    n_list = []
    for w in v.out_neighbours():
        n_list.append(w)
    
    v = n_list[randint(0, len(n_list))]

# Including age properties of vertices and edges.
g.vertex_properties["age"] = v_age
g.edge_properties["age"] = e_age

# Save graph
g.save("price.xml.gz")

# Plot in-degree distribution
in_hist = vertex_hist(g, "in")

y = in_hist[0]
err = sqrt(in_hist[0])
err[err >= y] = y[err >= y] - 1e-2

figure(figsize = (6, 4))
errorbar(in_hist[1][:-1], in_hist[0], fmt = "o", yerr = err, label = "in")
gca().set_yscale("log")
gca().set_xscale("log")
gca().set_ylim(1e-1, 1e5)
gca().set_xlim(0.8, 1e3)
subplots_adjust(left = 0.2, bottom = 0.2)
xlabel("$k_{in}$")
ylabel("$NP(k_{in})$")
tight_layout()
savefig("price-deg-dist.pdf")
savefig("price-deg-dist.png")