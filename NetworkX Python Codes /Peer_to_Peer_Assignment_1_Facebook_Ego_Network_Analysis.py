# Code for generating 
# Graph for Facebook Ego Network and doing the analysis 
# Libraries used are NetworkX, MatPlotlib, community
# Code by Nabeel Ahmad Khan
# Written on 16th Sep, 2017
# Last Edit on 20th Sep, 2017

import community
import networkx as nx
import matplotlib.pyplot as plt


# Function for Finding the Centrality of the Nodes in the Graph 
def closenss_centrality(G):
	closenessCentralityRanking = nx.closeness_centrality(G).items()
	r = [x[1] for x in closenessCentralityRanking]
	print("the value of r is ",r)
	meanCentrality = sum(r)/len(r) # mean centrality
	t = meanCentrality # threshold, we keep equal to mean
	reducedgraph = G.copy()
	for key, value in closenessCentralityRanking:
  		if value < t:
   			reducedgraph.remove_node(key)
 	return reducedgraph



# Making The facebook ego network graph 
G = nx.read_edgelist("/Users/nabeel/Desktop/Peer to Peer & Social Networks/Data Sets/facebook_combined.txt", create_using=nx.Graph(), nodetype=int)



# Displaying the properties of the Facebook Ego Network 
print(nx.info(G))
degreeD = nx.degree_histogram(G)
print("NetworkX Calculated Degree Distribution is ", degreeD)
fbClusteringCoefficient = nx.average_clustering(G)		# computing the average clustering coefficient.
print("The average clustering coefficient for FaceBook Ego Network is : %f" %fbClusteringCoefficient)
diameterForFBGraph = nx.diameter(G)
print("The diameter of the ER Graph is : %f" %diameterForFBGraph)



# Drawing Graph to show the Power Law characteristics
xaxis = range(0,1046)
plt.plot(xaxis, degreeD)
plt.show()




#Finding Closeness Centrality in the FaceBook Ego Network Graph 
reducedgraph = closenss_centrality(G)
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(reducedgraph,pos,node_color='red',alpha=0.4,node_size=254)
nx.draw_networkx_nodes(G,pos,node_color='green',alpha=0.2,node_size=8)
nx.draw_networkx_edges(G,pos,alpha=0.1)

nx.draw_networkx_labels(reducedgraph,pos,font_size=2,font_color='b')
plt.show()



# Showing Community Detection
parts = community.best_partition(G)
values = [parts.get(node) for node in G.nodes()]
plt.axis("off")
nx.draw_networkx(G, pos = spring_pos, cmap = plt.get_cmap("jet"), node_color = values, node_size = 35, with_labels = False)
plt.show()
