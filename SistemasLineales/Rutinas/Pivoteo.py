import numpy as np
from copy import deepcopy

def PivoteoParcialEscalonado(index_k:int,matrizA:np.array,factores_escala:np.array,tolerancia:float=1.0e-14) -> int:
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
    index_pivoteo = np.argmax(np.abs(matrizA[index_k:,index_k])/factores_escala[index_k:].T) + index_k
    if np.abs(factores_escala[index_pivoteo]) < tolerancia: raise BaseException('Matriz Singular')
    PermutarFilaPivoteo(index_k,index_pivoteo,matrizA)
    return index_pivoteo

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

def PermutarFilaPivoteo(index_k:int,index_pivoteo:int,matriz_general) -> None:
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

def AplicarPermutacion(permutacion:list[int],matriz_general):
    """
        Procedimiento para aplicar una permutación 
        a una estructura semejante a una matriz 
        (o iterable).

        permutacion : list[int] :: Lista que 
        representa la permutación a aplicar
        matriz_general :: Matriz que se le 
        aplica la permutación

        Devuelve la matriz permutada.
    """
    if type(matriz_general) == list:
        matriz_general_permutada = [0 for _ in range(len(matriz_general))]
        for index_original , index_permutado in enumerate(permutacion):
            matriz_general_permutada[index_permutado] = matriz_general[index_original]
    else:
        matriz_general_permutada = np.zeros(matriz_general.shape)
        for index_original , index_permutado in enumerate(permutacion):
            matriz_general_permutada[index_permutado] = matriz_general[index_original]
    return matriz_general_permutada

def __FactoresEscala(matrizA:np.array) -> np.array:
    """
        Procedimiento auxiliar para inicializar 
        los factores de escala asociados a la matriz A

        matrizA : np.array :: Matriz de la que 
        se determinan los factores de escala
    """
    return np.apply_over_axes(np.max,np.abs(matrizA),[1])

def __PermutacionInversa(permutacion:list[int]):
    """
        Procedimiento auxiliar para encontrar la permutación 
        inversa de una permutación dada, en específico, para 
        obtener la permutación de filas que se le tiene que 
        aplicar una matriz para estar pivoteada adecuadamente.
    
        permutacion : list[int] :: Permutación 
        de la que se quiere obtener su inversa

        Devuelve la permutación inversa.
    """
    permutacion_inversa = [0 for _ in range(len(permutacion))]
    for index_permutacion_inverso , index_permutacion in enumerate(permutacion):
        permutacion_inversa[index_permutacion] = index_permutacion_inverso
    return permutacion_inversa