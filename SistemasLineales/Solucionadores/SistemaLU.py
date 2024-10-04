import numpy as np
from copy import deepcopy

import sys
sys.path.insert(1,'../Rutinas')
from Sustituciones import SustitucionRegresiva , SustitucionProgresiva
from Pivoteo import AplicarPermutacion

def SistemaLU(matrizL:np.array,matrizU:np.array,vectorB:np.array) -> np.array:
    """
        Procedimiento que resuelve el sistema de ecuaciones 
        lineales de la forma LUx=b haciendo uso de sustituciones 
        progresiva y regresiva. No realiza pivoteo.

        matrizL : np.array :: Matriz triangular inferior 
        matrizU : np.array :: Matriz triangular superior
        vectorB : np.array :: Vector de términos independientes

        Devuelve el vector X.
    """
    vectorY = SustitucionProgresiva(matrizL,vectorB)
    return SustitucionRegresiva(matrizU,vectorY)

def SistemaLU_Pivoteo(matrizL:np.array,matrizU:np.array,vectorB:np.array,permutacion_filas_originales:list[int]) -> np.array:
    """
        Procedimiento que resuelve el sistema de ecuaciones 
        lineales de la forma LUx=b haciendo uso de sustituciones 
        progresiva y regresiva, y de pivoteo parcial escalonado.

        matrizL : np.array :: Matriz triangular inferior 
        matrizU : np.array :: Matriz triangular superior
        vectorB : np.array :: Vector de términos independientes
        permutacion_filas_originales : list[int] :: Permutación 
        de las filas sin pivotear para tenerlas pivoteadas

        Devuelve el vector X, con el adecuado orden de 
        las entradas.
    """
    vectorB_pivoteado = AplicarPermutacion(permutacion_filas_originales,vectorB)
    return  SistemaLU(matrizL,matrizU,vectorB_pivoteado)