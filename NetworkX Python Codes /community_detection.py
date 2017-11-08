import networkx as nx
import matplotlib.pyplot as plt
import numpy as np
import random

#myarray = np.fromfile('zachary.dat',dtype=float)

G=nx.karate_club_graph()
print("Node Degree")
#for v in G:
#    print('%s %s %s' % (v,G.degree(v),G.neighbors(v)))

labels = {}   
nodeColor = {} 
for node in G.nodes():
    labels[node] = node

#for node in G.nodes():
#	print('%s %s'%(node, labels[node]))


numberOfNodes = len(G.nodes())
switch = 34

while(switch > 0):
	displayedList = []
	count = 0
	print("Number of Nodes are ", numberOfNodes)
	switch = 0

	while(count < numberOfNodes):
		item = random.choice(G.nodes())
		colors = {}
		flag = 0
		maxRank = 0
		maxT = 0
		if item not in displayedList:
			print("item randomly selected is ",item)
			temp = []
			displayedList.append(item)
			count += 1
			temp = G.neighbors(item)
			for k in range(len(temp)):
				temp[k] = labels[temp[k]]
			for i in temp:
				if colors.has_key(i):
					colors[i] += 1
				else:
					colors[i] = 1
			#print("temp ",temp)
			#print("colors are ",colors)
			for j in colors:
				#print(" key value ",j, colors[j])
				if colors[j] > maxRank:
					maxRank = colors[j]
					maxT = j
					flag = 1

			if flag == 0:
				temp = random.choice(list(colors))
				if labels[item] != temp:
					switch += 1
					print("switch set to 1")
				labels[item] = temp
				#print("Labels item is ",labels[item])
			else:
				if labels[item] != maxT:
					switch += 1 
					print("switch set to  1")
				labels[item] = maxT
				#print("Labels item is ",labels[item])

			#print('%s %s'%(item, temp))
	
color_map = {0:'#FF0099', 1:'#660066' ,2:'#770066', 3:'#abcd99', 4:'#663456' ,5:'#321ab5'}

communities = {}
count = 0
for node in G.nodes():
	if communities.has_key(labels[node]):
		G.node[node]['community'] = communities[labels[node]]
	else:
		communities[labels[node]] = count
		G.node[node]['community'] = count
		count += 1

	print(" node Label",node, labels[node])
print("communities are ",communities)
print("labels are ",labels)
nx.draw(G, node_color=[color_map[G.node[node]['community']] for node in G], with_labels=True)	#Settign the parameters for ER Graph
#nx.draw_networkx_labels(G, pos)		# find out how to mark labels ????? IMPORTANT 
plt.show()


