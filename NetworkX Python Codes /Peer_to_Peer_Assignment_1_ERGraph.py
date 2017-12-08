# Code for generating 
# (a) An ER graph with 3000 nodes
# Fucntions for calculating the degree distribution, diameter, and the clustering coefficient.
#
# Libraries used are NetworkX, MatPlotlib, Numpy
# Code by Nabeel Ahmad Khan 
# Written on 15th Sep, 2017
# Last Edit on 20th Sep, 2017


import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


# Parameters for ER Graph
erNodes = 3000	# Nodes in an ER Graph
erProbability = 0.07  # Probability of an ER Graph 
avgDegreeForERGraph = 0.0	# Average Degree of ER Graph (Double Value)
diameterForERGraph = 0	# Diameter of an ER Graph (Integer Value)


# Making an ER Graph with properties defines above and finding the necessary Properties.
g1 = nx.fast_gnp_random_graph(erNodes, erProbability, seed=None, directed=False)


# Computing the average clustering coefficient using NetworkX inbuilt Function
erClusteringCoefficient = nx.average_clustering(g1)		# computing the average clustering coefficient.
print("NetworkX Calculated Average Clustering Coefficient for ER Graph is",erClusteringCoefficient)


# Calculating the average Degree of the graph using InBuilt Function
for i in range(erNodes): avgDegreeForERGraph += g1.degree(i)	#Calculating the average degree of the ER Graph
avgDegreeForERGraph = avgDegreeForERGraph/erNodes		#Calculating the average degree of the ER Graph
print("The Average Degree for an ER Graph is ",avgDegreeForERGraph)


# Displaying Diameter & Other Information about the Graph using the InBuilt Function.
diameterForERGraph = nx.diameter(g1)
print("NetworkX Calculated Diameter of the ER Graph is ",diameterForERGraph)
print(nx.info(g1))


#Calculating the Degree Distribution using the NetworkX function
degreeD = nx.degree_histogram(g1)
print("NetworkX Calculated Degree Distribution is ", degreeD)


# Manual Calculation of Degree Distribution
degreeManual = erNodes * [None]
for i in range(erNodes): 
	#print("THE VALUE OF I. IS ", i)
	degreeManual[i] = len(g1.neighbors(i))
#print("The degree distribution calculated manually is ",degreeManual)
degreeDistribution = [None] * erNodes
for i in range(erNodes):
	temp = i
	count=0
	for j in range(erNodes):
		if(degreeManual[j] == temp):
			count += 1
	degreeDistribution[i] = count
print("Manually Calculated Degree Distribution of the graph is calculated as", degreeDistribution)

# Drawing Graph to show the Binomial characteristic of Degree Distribution in the ER Graph
xaxis = range(0,erNodes)
plt.plot(xaxis, degreeDistribution)
plt.show()



# Manually calculating clustering coefficient of ER Graph Version 2
ccoverall = 0.0
for i in range(erNodes):
	neighbor = g1.neighbors(i)
	#print("the neighbors are ",neighbor)
	count = 0.0
	totaledge = (len(g1.neighbors(i)) * (len(g1.neighbors(i)) - 1))/ 2
	for j in neighbor:
		for k in neighbor:
			if(j != k):
				e = (j,k)
				#print("value of j k",e)
				if(g1.has_edge(*e)):
					count += 1
					#print("connection between j k",e)
	count = count/2
	if (totaledge != 0):
		cc = count/totaledge
	#print("the CC count totaledge ", cc, count, totaledge)
	ccoverall += cc

ccoverall = ccoverall/erNodes
print("Manually Calculated value of the cc of the graph ",ccoverall)


# Manually Calculating the Diameter of the Graph.
calcDiameter = erNodes * [0]
for i in range(erNodes):
	length=nx.single_source_shortest_path_length(g1,i)
	#print(length)
	#print(max([j for j in length.values()]))
	if (max([j for j in length.values()]) > calcDiameter[i]):
		calcDiameter[i] = max([j for j in length.values()])
#print("Diameter is ", calcDiameter)
print("Manually Calculated Diameter of the graph is ",np.amax(calcDiameter))



#Plotting the graph
nx.draw(g1, node_color='bisque', with_labels='TRUE')	#Settign the parameters for ER Graph
plt.show()	# Plotting the ER Graph


