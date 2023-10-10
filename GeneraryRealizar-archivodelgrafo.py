'''

Elaboro

1999491 Francisco Javier Blas Garza      
2007872 Kevin Eduardo Guajardo Vigil

Laboratorio de Sistemas adaptativos Martes 205

Sistema que te crea y genera un grafo, apartir de tu lista de amigos, y tambien indicando y colocando 
cada color distinto para diferenciar mejor cada dato (amigo), ademas en el sistema te genera en la 
matriz de adyacencia realizado de este grafo generado apartir de lista de amigos, en que se realizo.

'''


import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

# Crear un objeto grafo vacío
G = nx.Graph()

# Añadir nodos al grafo
creadores = 'Francisco', 'Kevin'
amigos = ['Kevin', 'Leonardo', 'Facundo', 'Juan', 'Cristian', 'Zaid', 'Vicente', 'Alan', 'JuanFra', 'Benito']
G.add_nodes_from(amigos)

# Añadir aristas al grafo (puedes modificar esto para reflejar las relaciones reales)
G.add_edge('Francisco', 'Kevin')
G.add_edge('Francisco', 'Facundo')
G.add_edge('Francisco', 'JuanFra')
G.add_edge('Francisco', 'Zaid')
G.add_edge('Francisco', 'Leonardo')
G.add_edge('Francisco', 'Vicente')
G.add_edge('Francisco', 'Cristian')
G.add_edge('Francisco', 'Juan')
G.add_edge('Francisco', 'Benito')
G.add_edge('Francisco', 'Alan')
G.add_edge('Kevin', 'Facundo')
G.add_edge('Kevin', 'Benito')
G.add_edge('Kevin', 'JuanFra')
G.add_edge('Kevin', 'Juan')
G.add_edge('Kevin', 'Alan')
G.add_edge('Kevin', 'Zaid')
G.add_edge('Kevin', 'Vicente')
G.add_edge('Kevin', 'Leonardo')
G.add_edge('Kevin', 'Cristian')
G.add_edge('Kevin', 'Francisco')
G.add_edge('Facundo', 'Leonardo')
G.add_edge('Facundo', 'JuanFra')
G.add_edge('Facundo', 'Kevin')
G.add_edge('Facundo', 'Cristian')
G.add_edge('Facundo', 'Zaid')
G.add_edge('Facundo', 'Vicente')
G.add_edge('Leonardo', 'JuanFra')
G.add_edge('Leonardo', 'Cristian')
G.add_edge('Leonardo', 'Zaid')
G.add_edge('Leonardo', 'Facundo')
G.add_edge('Leonardo', 'Vicente')
G.add_edge('Juan', 'Kevin')
G.add_edge('Juan', 'Benito')
G.add_edge('Juan', 'Alan')
G.add_edge('Cristian', 'Vicente')
G.add_edge('Cristian', 'Leonardo')
G.add_edge('Cristian', 'Facundo')
G.add_edge('Cristian', 'Zaid')
G.add_edge('Cristian', 'JuanFra')
G.add_edge('Zaid', 'Cristian')
G.add_edge('Zaid', 'JuanFra')
G.add_edge('Zaid', 'Leonardo')
G.add_edge('Zaid', 'Vicente')
G.add_edge('Zaid', 'Facundo')
G.add_edge('Vicente', 'JuanFra')
G.add_edge('Vicente', 'Zaid')
G.add_edge('Vicente', 'Facundo')
G.add_edge('Vicente', 'Leonardo')
G.add_edge('Vicente', 'Cristian')
G.add_edge('Alan', 'Benito')
G.add_edge('Alan', 'Kevin')
G.add_edge('JuanFra', 'Zaid')
G.add_edge('JuanFra', 'Cristian')
G.add_edge('JuanFra', 'Vicente')
G.add_edge('JuanFra', 'Leonardo')
G.add_edge('JuanFra', 'Facundo')
G.add_edge('JuanFra', 'Kevin')

colores_nodo=['green', 'yellow', 'red', 'lightgreen', 'purple', 'orange', 'crimson', 'olive', 'brown', 'pink', 'skyblue']

# Dibujar el grafo
nx.draw(G, with_labels=True, node_color=colores_nodo, edge_color='black', font_color='black')
plt.show()

# Obtener la matriz de adyacencia
matriz_adyacencia = nx.adjacency_matrix(G)
# Guardar la matriz en un archivo
np.savetxt("matriz_adyacencia.txt", matriz_adyacencia.todense(), fmt='%d')

print("La matriz de adyacencia se ha guardado en el archivo 'matriz_adyacencia.txt'")


