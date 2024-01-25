import numpy as np
from . import Edmonds as Edm

def build_tree(nodes, edges):

    weight = 0
    tree = []
    
    for i in range(len(nodes)):
        edges_merged = Edm.Edmonds(nodes, edges, i)
        
        w = np.inf
        if len(edges_merged) == len(nodes) - 1:
            w = sum(edge[2] for edge in edges_merged)

        if ((weight == 0) or (weight > w)):
            weight = w
            tree = edges_merged

    return tree
