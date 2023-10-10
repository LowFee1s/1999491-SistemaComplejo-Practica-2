'''
Elaboro

1999491  Francisco Javier Blas Garza    
2007872 Kevin Eduardo Guajardo Vigil

Laboratorio de Sistemas Adaptativos Martes 205

Sistema que lee archivos de matrices de adyacencia y calcula valores 
de m vertices, grado de cada vertices y n vertices.


'''

import numpy as np

def leer_matriz_desde_archivo(nombre_archivo):
    return np.loadtxt(nombre_archivo, dtype=int)

def calcular_valores(matriz):
    n = len(matriz)  # cantidad de vértices
    m = np.sum(matriz) // 2  # cantidad de aristas
    grados = np.sum(matriz, axis=1)  # grado de cada vértice
    return n, m, grados

nombre_archivo = 'matriz_adyacencia.txt'  # reemplaza esto con el nombre de tu archivo
matriz = leer_matriz_desde_archivo(nombre_archivo)
n, m, grados = calcular_valores(matriz)


print(f'Cantidad de vértices (n): {n}')
print(f'Cantidad de aristas (m): {m}')
print('Grado de cada vértice:' , grados)

