# python program for demostration of networkx
# uncomment the lines for the demonstration of code  

# importing different libraries to be used in the program  
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from pylab import rcParams
import seaborn as sb
import numpy as np

# Basic Graph Drawing Methods
# g = nx.Graph()		# creating a graph object g

# g.add_node(1)  # method to add node in a graph
# g.add_nodes_from([2,3,4,5,8,9])		# method to add multiple node
# g.add_edges_from([(1,2),(4,3),(1,9),(2,8)])		# method to add edges to the graph
# g.remove_node(1)	# method to remove nodes from the graph

# nx.draw(g)		# drawing the Graph
# nx.draw_circular(g)		# to draw the graph in circular form 
# nx.draw_spring(g)		# to draw the graph in spring form 
# plt.show()		# plotting the graph 


# Commands for Labeling and Coloring the Graph
# nx.draw_circular(g, node_color='bisque', with_labels='TRUE')		# to draw the graph with bisque color and nodes marked with with_labels


# Command to show the stats of the Graph
# stats = nx.degree(g)	# this method will give the number of nodes, edges, avg. degree of the graph
# print stats
# print nx.degree(g)		# this methood will display the degree of each node in the graph


# Graph Generators Functions
# g = nx.complete_graph(25)		# this method will make a complete graph with 25 nodes
# nx.draw(g, node_color='bisque', with_labels='TRUE')

g = nx.gnc_graph(7, seed=25)	# creating a random graph with GNC function
# nx.draw(g, node_color='bisque', with_labels='TRUE')

ego_g = nx.ego_graph(g, 3, radius=5)	# creating a ego graph as a sub graph to g, 3 is the center nodes and radius of the graph is 5
nx.draw(ego_g, node_color='bisque', with_labels='TRUE')

plt.show()



