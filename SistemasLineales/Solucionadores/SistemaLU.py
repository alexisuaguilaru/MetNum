import numpy as np
from copy import deepcopy

import sys
sys.path.insert(1,'../Rutinas')
from Sustituciones import SustitucionRegresiva , SustitucionProgresiva

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