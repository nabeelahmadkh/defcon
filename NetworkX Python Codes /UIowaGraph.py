import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import random
import community

style.use('ggplot')

#g = nx.read_edgelist('/Users/nabeel/Documents/Developer/uiowaCrawler/uiowaCrawler/uiowaCrawler/uiowaCrawler.csv',create_using = nx.Graph(),nodetype=str)
x, y = np.loadtxt('/Users/nabeel/Documents/Developer/uiowaCrawler.csv',
					dtype = str,
					unpack = True,
					delimiter = ',')

length1 = len(x)
length2 = len(y)
print("length of x & y ",length1,length2)

'''
print nx.info(g)

nx.draw(g)
plt.show()
'''