import numpy as np
from copy import deepcopy

def PivoteoParcialEscalonado(index_k:int,matrizA:np.array,factores_escala:np.array=None,tolerancia:float=1.0e-14) -> int:
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
        tolerancia : float :: Tolerancia para 
        considerar una matriz como singular

        Devuelve el indice de la fila con la cual 
        se intercambio para hacer pivoteo
    """
    if not factores_escala:
        factores_escala = __FactoresEscala(matrizA)
    index_pivoteo = np.argmax(np.abs(matrizA[index_k:,index_k])/factores_escala[index_k:].T)
    if np.abs(factores_escala[index_pivoteo]) < tolerancia: raise BaseException('Matriz Singular')
    PermutarFilaPivoteo(index_k,index_pivoteo,matrizA)
    return index_pivoteo

def __FactoresEscala(matrizA:np.array) -> np.array:
    """
        Procedimiento auxiliar para inicializar 
        los factores de escala asociados a la matriz A

        matrizA : np.array :: Matriz de la que 
        se determinan los factores de escala
    """
    return np.apply_over_axes(np.max,np.abs(matrizA),[1])

def ActualizarVectorEscala(index_k:int,matrizA:np.array,factores_escala:np.array) -> None:
    """
        index_k : int :: Indice sobre el cual 
        se va actualizar el vector de escalas
        matrizA : np.array :: Matriz en la 
        que se base para los factores de escalar
        factores_escala : np.array :: Vector de 
        escala el cual se actualiza.

        No devuelve nada.
    """
    factores_escala[index_k:] = np.apply_over_axes(np.max,np.abs(matrizA[index_k:]),[1])

def PermutarFilaPivoteo(index_k:int,index_pivoteo:int,matriz_general):
    """
        Procedimiento para intercambiar las filas 
        con indice k y pivoteo entre sí.

        index_k : int :: Indice k con el se va 
        intercambiar con otro
        index_pivoteo : int :: Indice de la fila 
        de pivoteo
        matriz_general :: Matriz de coeficientes, 
        vector de términos independientes o lista 
        de indices de filas permutadas a la que 
        se le aplica la permutación.
 
        No devuelve nada.
    """
    if type(matriz_general) == list:
        matriz_general[index_k] , matriz_general[index_pivoteo] = matriz_general[index_pivoteo] , matriz_general[index_k]
    else:
        fila_general_temporal = deepcopy(matriz_general[index_k])
        matriz_general[index_k] = matriz_general[index_pivoteo]
        matriz_general[index_pivoteo] = fila_general_temporal

def DespermutarFilas(vector_permutacion:list,matriz_general:np.array) -> None:
    """
        Procedimiento para revertir las permutaciones 
        realizadas en una matriz general.

        vector_permutacion : list :: Vector que refleja en 
        qué indice están las filas originales
        matriz_general : np.array :: Matriz a la que 
        se quiere regresar a su versión original, sin 
        ninguna permutación

        No devuelve nada.
    """
    matriz_original = np.zeros(matriz_general.shape)
    for index_permutado , index_original in enumerate(vector_permutacion):
        matriz_original[index_original] = matriz_general[index_permutado]
    matriz_general = matriz_original