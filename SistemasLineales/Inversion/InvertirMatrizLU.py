import numpy as np
from copy import deepcopy

import sys
sys.path.insert(1,'../Rutinas')
from FactoriazcionLU import FactorizacionLU_Choleski
sys.path.insert(1,'../Solucionadores')
from SistemaLU import SistemaLU

def InvertirMatrizSimetrica(matrizA:np.array) -> np.array:
    """
        Procedimiento que invierte una matriz 
        simétrica haciendo uso de su factorización 
        LU de Choleski y resolviendo N sistemas 
        de ecuaciones lineales con los diferentes 
        vectores columna de la matriz identidad. 
        No realiza pivoteo.

        matrizA : np.array :: Matriz simétrica

        Devuelve la matriz inversa de A.
    """
    n = len(matrizA)
    matrizL = FactorizacionLU_Choleski(matrizA)
    matrizU = matrizL.T
    matrizIdentidad = np.eye(n,dtype=float)
    matrizA_Inversa = np.zeros((n,n),dtype=float)
    for columna_index , vectorColumnaIdentidad in enumerate(matrizIdentidad):
        vectorColumnaA_Inverso = SistemaLU(matrizL,matrizU,vectorColumnaIdentidad)
        matrizA_Inversa[:,columna_index] = vectorColumnaA_Inverso
    return matrizA_Inversa