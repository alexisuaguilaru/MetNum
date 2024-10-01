import numpy as np
from copy import deepcopy

import sys
sys.path.insert(1,'../Rutinas')
from Sustituciones import SustitucionRegresiva

def EliminacionGauss(matrizA:np.array,vectorB:np.array) -> np.array:
    """
        Procedimiento que resuelve el sistema de ecuaciones 
        lineales de la forma Ax=b haciendo uso de Eliminación 
        de Gauss. No realiza pivoteo.

        matrizA : np.array :: Matriz de coeficientes del sistema
        vectorB : np.array :: Vector de términos independientes

        Devuelve vector X.
    """
    n = len(matrizA)
    matrizU = deepcopy(matrizA)
    vectorX = deepcopy(vectorB)
    for k_index in range(n-1):
        for i_index in range(k_index+1,n):
            factor_escalamiento = matrizU[i_index][k_index] / matrizU[k_index][k_index]
            matrizA[i_index] -= factor_escalamiento*matrizU[k_index]
            vectorX[i_index] -= factor_escalamiento*vectorX[k_index]
    return SustitucionRegresiva(matrizU,vectorX)