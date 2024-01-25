import numpy as np
from . import Edmonds as Edm

def get_min_tree(T1, T2, edges_all):
    
    nodes = T1[0] + T2[0]       
    edges = list(filter(lambda edge: ((edge[0] in nodes) and (edge[1] in nodes)),
                   edges_all))
    
    # Алгоритм Чу-Ли-Эдмонда
    edges_merged = Edm.Edmonds(nodes, edges, T2[3])

    w = np.inf
    if len(edges_merged) == len(nodes) - 1:
        w = sum(edge[2] for edge in edges_merged)
        
    T = (nodes, edges_merged, w, T2[3])
    return T


def find_tree(trees, vertex):
    for i in range(len(trees)):
        if vertex in trees[i][0]:
            return i


def get_edges_from_F(F):
    edges = []
    for i in range(len(F)):
        edges += F[i][1]
    return edges


def iteration(F, edges_all, edges_other):
    
    mu_dot = []
    for i in range(len(F)):
        mu_dot.append(F[i][2])

    # Можно оптимизировать перебор (пройти по списку только 1 раз)?
    mu_zero = []
    edge_zero = []
    T_index = []
    T_merged = []
    for i in range(len(F)):
        edge = (-1, -1, 0)
        for j in range(len(edges_other)):
            if edges_other[j][1] in F[i][0]:
                if edge[0] == -1:
                    edge = edges_other[j]
                elif edge[2] > edges_other[j][2]:
                    edge = edges_other[j]
                    
        if edge[0] == -1:
            mu_zero.append(np.inf)
            edge_zero.append(edge)
            T_index.append(i)
            T_merged.append(([], [], 0))
        else:
            k = find_tree(F, edge[0])
            T = get_min_tree(F[i], F[k], edges_all)
            
            mu_zero.append(T[2])
            edge_zero.append(edge)
            T_index.append(k)
            T_merged.append(T)

    delta = np.subtract(mu_zero, mu_dot)
    (i, min_delta) = min(enumerate(delta), key=lambda pair: pair[1])
    if np.isinf(min_delta):
        print("Stop!")
        return (F, [])

    edge_new = edge_zero[i]
    mu_new = mu_zero[i]
    
    F_new = F.copy()
    F_new.remove(F[i])
    F_new.remove(F[T_index[i]])
    F_new.append(T_merged[i])
    
    edges_other_new = list(filter(
        lambda edge: ((edge[0] not in T_merged[i][0]) or
                      (edge[1] not in T_merged[i][0])),
        edges_other))

    return (F_new, edges_other_new)

def build_forest(nodes, edges, k):
    n = len(nodes)
    F = []
    for i in range(n):
        F.append(([nodes[i]], [], 0, i))
    edges_other = edges.copy()

    result = [get_edges_from_F(F)]
    for i in range(n-k):
        (F, edges_other) = iteration(F, edges, edges_other)
        result = result + [get_edges_from_F(F)]
        if ((len(edges_other) == 0) and (i != n-k-1)):
            print("Невозможно построить лес с таким количеством деревьев!")
            break
    return result
