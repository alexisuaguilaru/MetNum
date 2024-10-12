import numpy as np
from copy import deepcopy

import sys
sys.path.insert(1,'../../..')
from MetNum.SistemasLineales.Rutinas.Pivoteo import AplicarPermutacion
from MetNum.SistemasLineales.Solucionadores.EliminacionGauss import SimulacionEliminacionGaussPivoteo

def FactorizacionLU_Doolittle(matrizA:np.array) -> tuple[np.array,np.array]:
  """
    Procedimiento para factorizar una matriz cuadrada 
    A en el producto de una matriz triangular inferior L 
    y una superior U, haciendo uso de la restricción 
    de Doolittle. A = LU.

    matrizA : np.array :: Matriz cuadrada

    Devuelve las matrices L y U.
  """
  n = len(matrizA)
  matrizL = np.eye(n,dtype=float)
  matrizU = deepcopy(matrizA)
  for fila_pivote in range(n-1):
    for fila_i in range(fila_pivote+1,n):
      factor_escalamiento = matrizU[fila_i][fila_pivote] / matrizU[fila_pivote][fila_pivote]
      matrizU[fila_i] -= factor_escalamiento*matrizU[fila_pivote]
      matrizL[fila_i][fila_pivote] = factor_escalamiento
  return matrizL , matrizU

def FactorizacionLU_Choleski(matrizA:np.array) -> np.array:
  """
    Procedimiento para factorizar una matriz cuadrada 
    simétrica A en el producto de una matriz triangular L
    y de su transpuesta L^T, haciendo uso de la restricción 
    de Choleski. A = LL^T.

    matrizA : np.array :: Matriz cuadrada simétrica

    Devuelve la matriz L
  """
  n = len(matrizA)
  matrizL = np.zeros((n,n),dtype=float)
  for index_j in range(n):
    for index_i in range(index_j,n):
      __Elemento_ijMatrizL(index_i,index_j,matrizA,matrizL)
  return matrizL

def __Elemento_ijMatrizL(index_i:int,index_j:int,matrizA:np.array,matrizL:np.array) -> None:
  """
    Procedimiento auxiliar para determinar la entrada 
    (i,j) de la matriz L de la factorización de 
    Choleski, derivada del producto matricial LL^T 
    comparado con la matriz A a factorizar. 

    index_i : int :: Indice la fila 
    index_j : int :: Indice la columna 
    matrizA : np.array :: Matriz original a factorizar
    matrizL : np.array :: Matriz resultante de la factorización 
    y en donde se guardan los elementos calculados
  """
  suma_elementos_previos = matrizL[index_i,:index_j]@matrizL[index_j,:index_j]
  if index_i == index_j:
    elemento_ij = np.sqrt(matrizA[index_i][index_j] - suma_elementos_previos)
    matrizL[index_i][index_j] = elemento_ij
  else:
    elemento_ij = (matrizA[index_i][index_j] - suma_elementos_previos) / matrizL[index_j][index_j]
    matrizL[index_i][index_j] = elemento_ij

def FactorizacionLUPivoteo_Doolittle(matrizA:np.array) -> tuple[np.array,np.array,list[int],list[int]]:
  """
    Procedimiento para factorizar una matriz cuadrada 
    A en el producto de una matriz triangular inferior L 
    y una superior U, haciendo uso de la restricción 
    de Doolittle y pivoteo. PA = LU.

    matrizA : np.array :: Matriz cuadrada

    Devuelve las matrices L y U, junto con la 
    lista de permutaciones de filas pivoteadas y 
    la lista de la permutación que se le aplica 
    a la matriz original. 
  """
  permutacion_filas_pivoteadas , permutacion_filas_originales = SimulacionEliminacionGaussPivoteo(matrizA)
  matrizA_pivoteada = AplicarPermutacion(permutacion_filas_originales,matrizA)
  return *FactorizacionLU_Doolittle(matrizA_pivoteada) , permutacion_filas_pivoteadas , permutacion_filas_originales