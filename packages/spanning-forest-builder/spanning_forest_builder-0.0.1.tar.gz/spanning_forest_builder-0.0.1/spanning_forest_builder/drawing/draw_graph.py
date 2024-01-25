import networkx as nx
import matplotlib.pyplot as plt
from . import draw_edge_labels as dl

def draw_graph(G):

    fig, ax = plt.subplots()
    pos=nx.spring_layout(G,seed=0)

    # set layout
    pos = nx.circular_layout(G)

    # draw graph
    nx.draw_networkx_nodes(G, pos, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax)

    curved_edges = [edge for edge in G.edges() if reversed(edge) in G.edges()]
    straight_edges = list(set(G.edges()) - set(curved_edges))
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=straight_edges)
    arc_rad = 0.2
    nx.draw_networkx_edges(G, pos, ax=ax, edgelist=curved_edges,
                       connectionstyle=f'arc3, rad = {arc_rad}')

    # draw edge labels
    edge_weights = nx.get_edge_attributes(G,'w')
    curved_edge_labels = {edge: edge_weights[edge] for edge in curved_edges}
    straight_edge_labels = {edge: edge_weights[edge] for edge in straight_edges}
    dl.draw_labels(G, pos, ax=ax,
        edge_labels=curved_edge_labels,rotate=False,rad = arc_rad)
    nx.draw_networkx_edge_labels(G, pos, ax=ax,
        edge_labels=straight_edge_labels,rotate=False)

    return fig
