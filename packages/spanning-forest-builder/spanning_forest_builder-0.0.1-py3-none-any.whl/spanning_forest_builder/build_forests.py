import networkx as nx
import matplotlib.pyplot as plt
import PIL
import os, shutil
from .algorithm import algorithm as alg
from .algorithm import full_Edmonds
from .drawing import draw_graph as dg

def list_to_dict(l):
    d = []
    for i in range(len(l)):
        x = (l[i][0], l[i][1], {'w':l[i][2]})
        d.append(x)
    return d

def make_image_folder():
    folder = "images"
    if not os.path.exists(folder):
        os.makedirs(folder)
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))

def build_all_forests(nodes, edges, disp=False):

    make_image_folder()

    n = len(nodes)
    
    G = nx.DiGraph(directed=True)
    G.add_nodes_from(nodes)
    G.add_edges_from(list_to_dict(edges))

    fig = dg.draw_graph(G)
    plt.title("Исходный граф")
    fig.savefig("images\\0.png")
    images = [PIL.Image.frombytes('RGB',
                                  fig.canvas.get_width_height(),
                                  fig.canvas.tostring_rgb())]
    result = alg.build_forest(nodes, edges, 1)
    for i in range(len(result)):
        G = nx.DiGraph(directed=True)
        G.add_nodes_from(nodes)
        G.add_edges_from(list_to_dict(result[i]))
        fig = dg.draw_graph(G)
        plt.title("Лес из " + str(n-i) + " деревьев")
        fig.savefig("images\\" + str(i+1) + ".png")
        images += [PIL.Image.frombytes('RGB',
                                       fig.canvas.get_width_height(),
                                       fig.canvas.tostring_rgb())]

    # Берем первый кадр и в него добавляем оставшееся кадры.
    images[0].save(
        "images\\graph.gif",
        save_all=True,
        append_images=images[1:],  # Срез который игнорирует первый кадр.
        optimize=True,
        duration=2000,
        loop=False
    )

    
    if disp:
        plt.show()

def build_tree_Edmonds(nodes, edges, disp=False):

    make_image_folder()

    n = len(nodes)
    
    G = nx.DiGraph(directed=True)
    G.add_nodes_from(nodes)
    G.add_edges_from(list_to_dict(edges))

    fig = dg.draw_graph(G)
    plt.title("Исходный граф")
    fig.savefig("images\\0.png")
    images = [PIL.Image.frombytes('RGB',
                                  fig.canvas.get_width_height(),
                                  fig.canvas.tostring_rgb())]
    
    tree = full_Edmonds.build_tree(nodes, edges)
    G = nx.DiGraph(directed=True)
    G.add_nodes_from(nodes)
    G.add_edges_from(list_to_dict(tree))
    
    fig = dg.draw_graph(G)
    plt.title("Дерево")
    fig.savefig("images\\1.png")
    images += [PIL.Image.frombytes('RGB',
                                   fig.canvas.get_width_height(),
                                   fig.canvas.tostring_rgb())]
    
    if disp:
        plt.show()
