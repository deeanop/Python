import networkx as nx
import matplotlib.pyplot as mp
G1 = nx.Graph()
G1.add_nodes_from(["A", "B", "C", "D"])
G1.add_edges_from([
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("C", "D")
])
G2 = nx.DiGraph()
G2.add_nodes_from(["A", "B", "C", "D"])
G2.add_edges_from([
    ("A", "B"),
    ("A", "C"),
    ("B", "C"),
    ("C", "D")
])
mp.figure(figsize = (10, 4))
mp.subplot(2, 2, 1)
nx.draw(G1, with_labels = True, node_color = "lightblue", node_size = 800, font_weight = "bold")
mp.title("Graf neorientat")
mp.subplot(2, 2, 3)
nx.draw(G2, with_labels = True, node_color = "red", node_size = 800,
        font_weight = "bold", arrows = True, arrowsize = 20)
mp.title("Graf orientat")
mp.show()
