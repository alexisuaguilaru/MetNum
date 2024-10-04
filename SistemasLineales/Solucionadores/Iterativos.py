import numpy as np
from copy import deepcopy

def MetodoJacobi(matrizA:np.array,vectorB:np.array,limite_inferior:float=-10,limite_superior:float=10,tolerancia:float=1e-15):
    """
        Procedimiento para determinar una 
        solución aproximada al sistema de 
        ecuaciones lineales Ax=b haciendo 
        uso de método de Jacobi.
    
        matrizA : np.array :: Matriz de 
        coeficientes del sistema
        vectorB : np.array :: Vector de 
        términos independientes
        limite_inferior : float :: Límite 
        inferior de la estimación inicial
        limite_superior : float :: Límite 
        superior de la estimación inicial
        tolerancia : float :: Tolerancia 
        para indicar que el método convergió 
        a una solución.

        Devuelve vector solución X 
        aproximado
    """
    n = len(vectorB)
    vectorX = np.random.random(n)*limite_inferior + (limite_superior-limite_inferior)
    vectorX_actualizado = np.random.random(n)*limite_inferior + (limite_superior-limite_inferior)
    while not np.any(np.abs(vectorX-vectorX_actualizado) < tolerancia):
        for i_index in range(n):
            vectorX_actualizado[i_index] = (vectorB[i_index] - matrizA[i_index,:i_index]@vectorX[:i_index] - matrizA[i_index,i_index+1:]@vectorX[i_index+1:])/matrizA[i_index][i_index]
        vectorX = deepcopy(vectorX_actualizado)
    return vectorX

def MetodoGaussSeidel(matrizA:np.array,vectorB:np.array,limite_inferior:float=-10,limite_superior:float=10,tolerancia:float=1e-15):
    """
        Procedimiento para determinar una 
        solución aproximada al sistema de 
        ecuaciones lineales Ax=b haciendo 
        uso de método de Gauss-Seidel.
    
        matrizA : np.array :: Matriz de 
        coeficientes del sistema
        vectorB : np.array :: Vector de 
        términos independientes
        limite_inferior : float :: Límite 
        inferior de la estimación inicial
        limite_superior : float :: Límite 
        superior de la estimación inicial
        tolerancia : float :: Tolerancia 
        para indicar que el método convergió 
        a una solución.

        Devuelve vector solución X 
        aproximado
    """
    n = len(vectorB)
    vectorX = np.random.random(n)*limite_inferior + (limite_superior-limite_inferior)
    vectorX_actualizado = np.random.random(n)*limite_inferior + (limite_superior-limite_inferior)
    while not np.any(np.abs(vectorX-vectorX_actualizado) < tolerancia):
        for i_index in range(n):
            vectorX_actualizado[i_index] = (vectorB[i_index] - matrizA[i_index,:i_index]@vectorX_actualizado[:i_index] - matrizA[i_index,i_index+1:]@vectorX[i_index+1:])/matrizA[i_index][i_index]
        vectorX = deepcopy(vectorX_actualizado)
    return vectorX