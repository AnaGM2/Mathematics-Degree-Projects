# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 19:28:49 2024

@author: gilpe
"""

import networkx as nx
import matplotlib.pyplot as plt

node_color = 'black'

# Ejemplo 1
G = nx.Graph()
G.is_directed()

G.add_nodes_from(["1","2","3"])
G.add_edges_from([("1", "2"), ("2", "3")])

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(G, with_labels=True, ax=ax, node_color=node_color, font_color='white')
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])
print(G)


# Ejemplo 2
G = nx.DiGraph()
G.is_directed()

G.add_nodes_from(["1","2","3"])
G.add_edges_from([("2", "1"), ("2", "3")])

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(G, with_labels=True, ax=ax, node_color=node_color, font_color='white')
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])
print(G)


# Ejemplo 3 G
G = nx.Graph()
G.is_directed()

G.add_nodes_from(["1","2","3","4"])
G.add_edges_from([("1", "2"),("1", "3"),("2", "3"),("3", "4")])

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(G, with_labels=True, ax=ax, node_color=node_color, font_color='white')
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])
print(G)


# Ejemplo 3 G'
G = nx.Graph()
G.is_directed()

G.add_nodes_from(["1","2","3","4"])
G.add_edges_from([("1", "1"),("1", "2"),("1", "3"),("2", "3"),("3", "4")])

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(G, with_labels=True, ax=ax, node_color=node_color, font_color='white')
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])
print(G)


# Ejemplo 3 G alternativo
G = nx.Graph()
G.is_directed()

G.add_nodes_from(["1","2","3","4"])
G.add_edges_from([("1", "2"),("1", "3"),("1", "4"),("2", "4")])

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(G, with_labels=True, ax=ax, node_color=node_color, font_color='white')
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])
print(G)


# Ejemplo 3 G complementario
G = nx.Graph()
G.is_directed()

G.add_nodes_from(["1","2","3","4"])
G.add_edges_from([("1", "4"),("2", "4")])

fig, ax = plt.subplots(figsize=(4, 2))
nx.draw(G, with_labels=True, ax=ax, node_color=node_color, font_color='white')
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])
print(G)


# Definición K4
K4 = nx.Graph()
K4.is_directed()

K4.add_nodes_from(["1","2","3","4"])
K4.add_edges_from([("1", "2"),("1", "3"),("1", "4"),("2", "3"),("2", "4"),("3", "4")])

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(K4, with_labels=True, ax=ax, node_color=node_color, font_color='white')
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])
print(K4)


# Definición K5
K5 = nx.Graph()
K5.is_directed()

K5.add_nodes_from(["1","2","3","4","5"])
K5.add_edges_from([("1", "2"),("1", "3"),("1", "4"),("1", "5"),("2", "3"),("2", "4"),
                   ("2", "5"),("3", "4"),("3", "5"),("4", "5"),])

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(K5, with_labels=True, ax=ax, node_color=node_color, font_color='white')
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])
print(K5)


# Definición C6
C6 = nx.Graph()
C6.is_directed()

C6.add_nodes_from(["1","2","3","4","5","6"])
C6.add_edges_from([("1", "2"),("2", "3"),("3", "4"),("4", "5"),("5", "6"),("6", "1")])

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(C6, with_labels=True, ax=ax, node_color=node_color, font_color='white')
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])
print(C6)


# Definición P5
P5 = nx.Graph()
P5.is_directed()

P5.add_nodes_from(["1","2","3","4","5","6"])
P5.add_edges_from([("1", "2"),("2", "3"),("3", "4"),("4", "5"),("5", "6")])

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(P5, with_labels=True, ax=ax, node_color=node_color, font_color='white')
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])
print(P5)


# Definición W6
W6 = nx.Graph()
W6.is_directed()

W6.add_nodes_from(["1","2","3","4","5","6"])
W6.add_edges_from([("1", "2"),("2", "3"),("3", "4"),("4", "5"),("5", "1"),("1", "6"),
                   ("2", "6"),("3", "6"),("4", "6"),("5", "6")])

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(W6, with_labels=True, ax=ax, node_color=node_color, font_color='white')
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])
print(W6)


# Ejemplo 14.1
G = nx.Graph()
G.is_directed()

G.add_nodes_from(["1","2","3","4","5"])
G.add_edges_from([("1", "2"),("1", "3"),("2", "3"),("2", "4"),("2", "5")])

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(G, with_labels=True, ax=ax, node_color=node_color, font_color='white')
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])
print(G)


# Ejemplo 14.2
G = nx.DiGraph()
G.is_directed()

G.add_nodes_from(["1","2","3","4","5"])
G.add_edges_from([("1", "2"),("2", "1"),("1", "4"),("3", "2"),("3", "4"),("1", "5"),("5", "4"),("6", "1")])

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(G, with_labels=True, ax=ax, node_color=node_color, font_color='white')
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])
print(G)


# Ejemplo 14.4
G = nx.Graph()
G.is_directed()

G.add_nodes_from(["1","2","3","4","5"])
G.add_edges_from([("1", "2"),("1", "3"),("1", "4"),("1", "6"),("1", "7"),("2", "3"),("3", "4"),("4", "5"),
                  ("5", "6"),("6", "7"),("4", "8"),("8", "9"),("8", "10")])

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(G, with_labels=True, ax=ax, node_color=node_color, font_color='white')
ax.set_xlim([1.2*x for x in ax.get_xlim()])
ax.set_ylim([1.2*y for y in ax.get_ylim()])
print(G)


#######################
# GRAFOS ALEATORIOS
#######################

# Figura 13 a

GERa = nx.erdos_renyi_graph(n=20, p=0)
GERa.is_directed()

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(GERa, with_labels=True, ax=ax, node_color='black', font_color='white')

# Figura 13 b

GERb = nx.erdos_renyi_graph(n=20, p=0.106)
GERb.is_directed()

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(GERb, with_labels=True, ax=ax, node_color='black', font_color='white')

# Figura 13 c

GERc = nx.erdos_renyi_graph(n=20, p=0.265)
GERc.is_directed()

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(GERc, with_labels=True, ax=ax, node_color='black', font_color='white')

# Figura 13 d

GERd = nx.erdos_renyi_graph(n=20, p=1)
GERd.is_directed()

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(GERd, with_labels=True, ax=ax, node_color='black', font_color='white')

# Ejemplo BA

GBA = nx.barabasi_albert_graph(n=25, m=10, initial_graph = GERc)
GBA.is_directed()

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(GBA, with_labels=True, ax=ax, node_color='black', font_color='white')

# Figura 17 a

GWSa = nx.watts_strogatz_graph(n=20, k=6, p=0)
GWSa.is_directed()

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(GWSa, with_labels=True, ax=ax, node_color='black', font_color='white')

# Figura 17 b

GWSb = nx.watts_strogatz_graph(n=20, k=6, p=0.1)
GWSb.is_directed()

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(GWSb, with_labels=True, ax=ax, node_color='black', font_color='white')

# Figura 17 c

GWSc = nx.watts_strogatz_graph(n=20, k=6, p=0.5)
GWSc.is_directed()

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(GWSc, with_labels=True, ax=ax, node_color='black', font_color='white')

# Figura 17 d

GWSd = nx.watts_strogatz_graph(n=20, k=6, p=0.95)
GWSd.is_directed()

fig, ax = plt.subplots(figsize=(4, 4))
nx.draw(GWSd, with_labels=True, ax=ax, node_color='black', font_color='white')
