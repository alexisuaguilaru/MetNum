import numpy as np
from copy import deepcopy

from ..Rutinas.Sustituciones import SustitucionRegresiva

import sys
sys.path.insert(1,'../../..')
from MetNum.SistemasLineales.Rutinas.Pivoteo import __FactoresEscala , PivoteoParcialEscalonado , PermutarFilaPivoteo , ActualizarVectorEscala , __PermutacionInversa

def EliminacionGauss(matrizA:np.ndarray,vectorB:np.ndarray) -> np.ndarray:
    """
        Procedimiento que resuelve el sistema de ecuaciones 
        lineales de la forma Ax=b haciendo uso de Eliminación 
        de Gauss. No realiza pivoteo.

        matrizA : np.ndarray :: Matriz de coeficientes del sistema
        vectorB : np.ndarray :: Vector de términos independientes

        Devuelve vector X.
    """
    n = len(matrizA)
    matrizU = deepcopy(matrizA)
    vectorX = deepcopy(vectorB)
    for k_index in range(n-1):
        for i_index in range(k_index+1,n):
            factor_escalamiento = matrizU[i_index][k_index] / matrizU[k_index][k_index]
            matrizU[i_index] -= factor_escalamiento*matrizU[k_index]
            vectorX[i_index] -= factor_escalamiento*vectorX[k_index]
    return SustitucionRegresiva(matrizU,vectorX)

def EliminacionGaussPivoteo(matrizA:np.ndarray,vectorB:np.ndarray) -> np.ndarray:
    """
        Procedimiento que resuelve el sistema de ecuaciones
        lineales de la forma Ax=b haciendo uso de Eliminación
        de Gauss realizando pivoteo.

        matrizA : np.ndarray :: Matriz de coeficientes del sistema
        vectorB : np.ndarray :: Vector de términos independientes

        Devuelve vector X.
    """
    n = len(matrizA)
    matrizU = deepcopy(matrizA)
    vectorX = deepcopy(vectorB)
    factores_escala = __FactoresEscala(matrizA)
    for index_k in range(n-1):
        index_pivoteo = PivoteoParcialEscalonado(index_k,matrizU,factores_escala)
        PermutarFilaPivoteo(index_k,index_pivoteo,vectorX)
        for i_index in range(index_k+1,n):
            factor_escalamiento = matrizU[i_index][index_k] / matrizU[index_k][index_k]
            matrizU[i_index] -= factor_escalamiento*matrizU[index_k]
            vectorX[i_index] -= factor_escalamiento*vectorX[index_k]
        ActualizarVectorEscala(index_k,matrizU,factores_escala)
    return SustitucionRegresiva(matrizU,vectorX)

def SimulacionEliminacionGaussPivoteo(matrizA:np.ndarray) -> tuple[list,list]:
    """
        Procedimiento auxiliar que realiza la eliminación de 
        Gauss a la matriz A con pivote, para obtener la lista 
        de la permutación de las filas pivoteadas adecuadamente 
        y la lista de la permutación que se debe que aplicar 
        para obtener una matriz pivoteada adecuadamente.

        matrizA : np.ndarray :: Matriz de coeficientes del sistema

        Devuelve la lista de la permutación las filas 
        pivoteadas y la lista de la permutación a aplicar.
    """
    n = len(matrizA)
    matrizU = deepcopy(matrizA)
    factores_escala = __FactoresEscala(matrizA)
    permutacion_filas_pivoteadas = [index_fila for index_fila in range(n)]
    for index_k in range(n-1):
        index_pivoteo = PivoteoParcialEscalonado(index_k,matrizU,factores_escala)
        PermutarFilaPivoteo(index_k,index_pivoteo,permutacion_filas_pivoteadas)
        for i_index in range(index_k+1,n):
            factor_escalamiento = matrizU[i_index][index_k] / matrizU[index_k][index_k]
            matrizU[i_index] -= factor_escalamiento*matrizU[index_k]
        ActualizarVectorEscala(index_k,matrizU,factores_escala)
    return permutacion_filas_pivoteadas , __PermutacionInversa(permutacion_filas_pivoteadas) 