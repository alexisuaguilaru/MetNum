import numpy as np
from copy import deepcopy

def FactorizacionLU_Doolittle(matrizA:np.array):
  """
    Procedimiento para factorizar una matriz cuadrada 
    A en el producto de una matriz triangular inferior L 
    y una superior U, haciendo uso de la restricción 
    de Doolittle.

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

