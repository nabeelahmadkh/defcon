# Code for generating 
# (a) A Watts and Strogatz Small World graph with 1000 nodes
# Fucntions for calculating the degree distribution, diameter, and the clustering coefficient
#
# Libraries used are NetworkX, MatPlotlib, numpy
# Code by Nabeel Ahmad Khan
# Written on 16th Sep, 2017
# Last Edit on 20th Sep, 2017

 
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Parameters for Watts and Strogatz Small World graph 
wsNodes = 1000
connectedToNearestNeighbors = 10
probabiltyOfAddingNewEdge = 0.1
avgDegreeForWSGraph = 0.0	# Average Degree of WS Graph (Double Value)
diameterForWSGraph = 0	# Diameter of an WS Graph (Integer Value)


# Making an Watts & Strogatz Small World Graph with properties defined above and finding the necessary properties.
g3 = nx.newman_watts_strogatz_graph(wsNodes, connectedToNearestNeighbors, probabiltyOfAddingNewEdge)
wsClusteringCoefficient = nx.average_clustering(g3)		# computing the average clustering coefficient.
print("The average clustering coefficient for WS Graph is",wsClusteringCoefficient)
for i in range(wsNodes): avgDegreeForWSGraph += g3.degree(i)	#Calculating the average degree of the WS Graph
avgDegreeForWSGraph = avgDegreeForWSGraph/wsNodes		#Calculating the average degree of the WS Graph
print("The average degree for an WS Graph is ",avgDegreeForWSGraph)
diameterForWSGraph = nx.diameter(g3)
print("The diameter of the WS Graph is ",diameterForWSGraph)

#Calculating the Degree Distribution using the NetworkX function
degreeD = nx.degree_histogram(g3)
print("NetworkX Calculated Degree Distribution is ", degreeD)



# Manual Calculation of Degree Distribution
degreeManual = wsNodes * [None]
for i in range(wsNodes): 
	#print("THE VALUE OF I. IS ", i)
	degreeManual[i] = len(g3.neighbors(i))
#print("The degree distribution calculated manually is ",degreeManual)
degreeDistribution = [None] * wsNodes
for i in range(wsNodes):
	temp = i
	count=0
	for j in range(wsNodes):
		if(degreeManual[j] == temp):
			count += 1
	degreeDistribution[i] = count
print("Manually Calculated Degree Distribution of the graph is calculated as", degreeDistribution)

# Drawing Graph to show the characteristic of Degree Distribution in the SW Graph
xaxis = range(0,wsNodes)
#plt.plot(xaxis, degreeDistribution)
#plt.show()


# Manually calculating clustering coefficient of Small World Graph again
ccoverall = 0.0
for i in range(wsNodes):
	neighbor = g3.neighbors(i)
	#print("the neighbors are ",neighbor)
	count = 0.0
	totaledge = (len(g3.neighbors(i)) * (len(g3.neighbors(i)) - 1))/ 2
	for j in neighbor:
		for k in neighbor:
			if(j != k):
				e = (j,k)
				#print("value of j k",e)
				if(g3.has_edge(*e)):
					count += 1
					#print("connection between j k",e)
	count = count/2
	if (totaledge != 0):
		cc = count/totaledge
	#print("the CC count totaledge ", cc, count, totaledge)
	ccoverall += cc

ccoverall = ccoverall/wsNodes
print("Manually Calculated value of the cc of the graph ",ccoverall)


# Manually Calculating the Diameter of the Graph.
calcDiameter = wsNodes * [0]
for i in range(wsNodes):
	length=nx.single_source_shortest_path_length(g3,i)
	#print(length)
	#print(max([j for j in length.values()]))
	if (max([j for j in length.values()]) > calcDiameter[i]):
		calcDiameter[i] = max([j for j in length.values()])
#print("Diameter is ", calcDiameter)
print("Manually Calculated Diameter of the graph is ",np.amax(calcDiameter))


nx.draw(g3, node_color='yellow', with_labels='TRUE')
plt.show()