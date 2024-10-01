import numpy as np
from copy import deepcopy

def PivoteoParcialEscalonado(index_k:int,matrizA:np.array,factores_escala:np.array=None) -> int:
    """
        Procedimiento para aplicar pivoteo parcial 
        escalonado sobre la columna k de la matriz 
        A, en base al vector de factores de escala 
        (si no se le pasa, se crea en base a la 
        matriz A).

        index_k : int :: Indice de la columna sobre 
        la cual se hará pivote
        matrizA : np.array :: Matriz en la que se 
        aplica el pivote 
        factores_escala : np.array :: Vector de 
        factores de escala de la matriz

        Devuelve el indice de la fila con la cual 
        se intercambio para hacer pivoteo
    """
    if not factores_escala:
        factores_escala = __FactoresEscala(matrizA)
    index_pivoteo = np.argmax(np.abs(matrizA[index_k:,index_k])/factores_escala[index_k:].T)
    matrizA[index_k] , matrizA[index_pivoteo] = deepcopy(matrizA[index_pivoteo]) , deepcopy(matrizA[index_k])
    return index_pivoteo

def __FactoresEscala(matrizA):
    """
        Procedimiento auxiliar para inicializar 
        los factores de escala asociados a la matriz A
    """
    return np.apply_over_axes(np.max,np.abs(matrizA),[1])