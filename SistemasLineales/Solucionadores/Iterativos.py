import numpy as np
from copy import deepcopy

from EliminacionGauss import SimulacionEliminacionGaussPivoteo
import sys 
sys.path.insert(1,'../Rutinas')
from Pivoteo import AplicarPermutacion

def MetodoJacobi(matrizA:np.array,vectorB:np.array,tolerancia_error:float=1e-9):
    """
        Procedimiento para determinar una 
        solución aproximada al sistema de 
        ecuaciones lineales Ax=b haciendo 
        uso de método de Jacobi.
    
        matrizA : np.array :: Matriz de 
        coeficientes del sistema
        vectorB : np.array :: Vector de 
        términos independientes
        tolerancia_error : float :: Tolerancia 
        para indicar que el método convergió 
        a una solución.

        Devuelve vector solución X 
        aproximado
    """
    n = len(vectorB)
    vectorX = np.zeros(n)
    vectorX_actualizado = np.zeros(n)
    vectorResto = vectorB - matrizA@vectorX 
    while np.linalg.norm(vectorResto) > tolerancia_error:
        for i_index in range(n):
            vectorX_actualizado[i_index] = (vectorB[i_index] - matrizA[i_index,:i_index]@vectorX[:i_index] - matrizA[i_index,i_index+1:]@vectorX[i_index+1:])/matrizA[i_index][i_index]
        vectorX = deepcopy(vectorX_actualizado)
        vectorResto = vectorB - matrizA@vectorX
    return vectorX

def MetodoGaussSeidel(matrizA:np.array,vectorB:np.array,tolerancia_error:float=1e-9):
    """
        Procedimiento para determinar una 
        solución aproximada al sistema de 
        ecuaciones lineales Ax=b haciendo 
        uso de método de Gauss-Seidel.
    
        matrizA : np.array :: Matriz de 
        coeficientes del sistema
        vectorB : np.array :: Vector de 
        términos independientes
        tolerancia_error : float :: Tolerancia 
        para indicar que el método convergió 
        a una solución.

        Devuelve vector solución X 
        aproximado
    """
    n = len(vectorB)
    vectorX = np.zeros(n)
    vectorResto = vectorB - matrizA@vectorX 
    while np.linalg.norm(vectorResto) > tolerancia_error:
        for i_index in range(n):
            vectorX[i_index] = (vectorB[i_index] - matrizA[i_index,:i_index]@vectorX[:i_index] - matrizA[i_index,i_index+1:]@vectorX[i_index+1:])/matrizA[i_index][i_index]
        vectorResto = vectorB - matrizA@vectorX
    return vectorX