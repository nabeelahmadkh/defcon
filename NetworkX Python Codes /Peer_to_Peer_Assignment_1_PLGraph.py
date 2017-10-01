# Code for generating 
# (a)  A Power Law graph (using the preferential attachment model) with 2000 nodes
# Fucntions for calculating the degree distribution, diameter, and the clustering coefficient
#
# Libraries used are NetworkX, MatPlotlib, Numpy
# Code by Nabeel Ahmad Khan
# Written on 16th Sep, 2017
# Last Edit on 20th Sep, 2017


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

# Parameters for Power Law Graph with Preferential Attachment 
plNodes = 2000
noOfNodesToAttachExistingNodes = 2
avgDegreeForPLGraph = 0.0	# Average Degree of PL Graph (Double Value)
diameterForPLGraph = 0	# Diameter of an PL Graph (Integer Value)

# Making an Power Law Graph with Preferential Attachment with properties defines above and finding the necessary properties.
g2 = nx.barabasi_albert_graph(plNodes, noOfNodesToAttachExistingNodes) # BA algo have Power Law Distribution and uses Preferential Attachment method to add new Nodes in the Graph.
plClusteringCoefficient = nx.average_clustering(g2)		# computing the average clustering coefficient.
print("NetworkX Calculated average clustering coefficient for PL Graph is",plClusteringCoefficient)
for i in range(plNodes): avgDegreeForPLGraph += g2.degree(i)	#Calculating the average degree of the PL Graph
avgDegreeForPLGraph = avgDegreeForPLGraph/plNodes		#Calculating the average degree of the PL Graph
print("NetworkX Calculated average degree for an PL Graph is ",avgDegreeForPLGraph)
diameterForPLGraph = nx.diameter(g2)
print("NetworkX Calculated diameter of the PL Graph is ",diameterForPLGraph)

#Calculating the Degree Distribution using the NetworkX function
degreeD = nx.degree_histogram(g2)
print("NetworkX Calculated Degree Distribution is ", degreeD)



# Manual Calculation of Degree Distribution
degreeManual = plNodes * [None]
for i in range(plNodes): 
	#print("THE VALUE OF I. IS ", i)
	degreeManual[i] = len(g2.neighbors(i))
#print("The degree distribution calculated manually is ",degreeManual)
degreeDistribution = [None] * plNodes
for i in range(plNodes):
	temp = i
	count=0
	for j in range(plNodes):
		if(degreeManual[j] == temp):
			count += 1
	degreeDistribution[i] = count
print("Manually Calculated Degree Distribution of the graph is calculated as", degreeDistribution)

# Drawing Graph to show the Power Law characteristic of Degree Distribution in the PL Graph
xaxis = range(0,plNodes)
plt.plot(xaxis, degreeDistribution)
plt.show()


# Manually calculating clustering coefficient of PowerLaw Graph 
ccoverall = 0.0
for i in range(plNodes):
	neighbor = g2.neighbors(i)
	#print("the neighbors are ",neighbor)
	count = 0.0
	totaledge = (len(g2.neighbors(i)) * (len(g2.neighbors(i)) - 1))/ 2
	for j in neighbor:
		for k in neighbor:
			if(j != k):
				e = (j,k)
				#print("value of j k",e)
				if(g2.has_edge(*e)):
					count += 1
					#print("connection between j k",e)
	count = count/2
	if (totaledge != 0):
		cc = count/totaledge
	#print("the CC count totaledge ", cc, count, totaledge)
	ccoverall += cc

ccoverall = ccoverall/plNodes
print("Manually Calculated value of the cc of the graph ",ccoverall)


# Manually Calculating the Diameter of the Graph.
calcDiameter = plNodes * [0]
for i in range(plNodes):
	length=nx.single_source_shortest_path_length(g2,i)
	#print(length)
	#print(max([j for j in length.values()]))
	if (max([j for j in length.values()]) > calcDiameter[i]):
		calcDiameter[i] = max([j for j in length.values()])
#print("Diameter is ", calcDiameter)
print("Manually Calculated Diameter of the graph is ",np.amax(calcDiameter))


nx.draw(g2, node_color='green', with_labels='TRUE')
plt.show()