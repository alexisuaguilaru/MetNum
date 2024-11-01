import numpy as np
from copy import deepcopy

from ..Rutinas.Sustituciones import SustitucionRegresiva , SustitucionProgresiva
from ..Rutinas.Pivoteo import AplicarPermutacion

def SistemaLU(matrizL:np.ndarray,matrizU:np.ndarray,vectorB:np.ndarray) -> np.ndarray:
    """
        Procedimiento que resuelve el sistema de ecuaciones 
        lineales de la forma LUx=b haciendo uso de sustituciones 
        progresiva y regresiva. No realiza pivoteo.

        matrizL : np.ndarray :: Matriz triangular inferior 
        matrizU : np.ndarray :: Matriz triangular superior
        vectorB : np.ndarray :: Vector de términos independientes

        Devuelve el vector X.
    """
    vectorY = SustitucionProgresiva(matrizL,vectorB)
    return SustitucionRegresiva(matrizU,vectorY)

def SistemaLU_Pivoteo(matrizL:np.ndarray,matrizU:np.ndarray,vectorB:np.ndarray,permutacion_filas_originales:list[int]) -> np.ndarray:
    """
        Procedimiento que resuelve el sistema de ecuaciones 
        lineales de la forma LUx=b haciendo uso de sustituciones 
        progresiva y regresiva, y de pivoteo parcial escalonado.

        matrizL : np.ndarray :: Matriz triangular inferior 
        matrizU : np.ndarray :: Matriz triangular superior
        vectorB : np.ndarray :: Vector de términos independientes
        permutacion_filas_originales : list[int] :: Permutación 
        de las filas sin pivotear para tenerlas pivoteadas

        Devuelve el vector X, con el adecuado orden de 
        las entradas.
    """
    vectorB_pivoteado = AplicarPermutacion(permutacion_filas_originales,vectorB)
    return  SistemaLU(matrizL,matrizU,vectorB_pivoteado)