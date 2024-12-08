import networkx as nx
import matplotlib.pyplot as plt

# Redefinir el grafo según los puntos especificados en la estructura proporcionada
edges_updated =  [(1, 10), (1, 7), (1, 9),
                 (2, 7), (2, 1), (2, 8),
                 (3, 7), (3, 10), (3, 2),
                 (4, 7), (4, 1), (4, 3),
                 (5, 7), (5, 3), (5, 1),
                 (6, 1), (6, 7), (6, 3),
                 (7, 10), (7, 2), (7, 6),
                 (8, 9), (8, 5), (8, 1),
                 (9, 7), (9, 2), (9, 1),
                 (10, 1), (10, 6), (10, 5)]

# Crear el grafo dirigido con los nuevos edges
G_updated = nx.DiGraph()
G_updated.add_edges_from(edges_updated)

# Usar el layout planar para minimizar cruces
pos_updated = nx.spring_layout(G_updated,k=3400, iterations=100)

# Dibujar el gráfico
plt.figure(figsize=(8, 8))
nx.draw(G_updated, pos_updated, with_labels=True, node_size=500, font_size=10, font_weight="bold", arrows=True)
plt.title("Diagrama Minimizado Actualizado")
plt.show()