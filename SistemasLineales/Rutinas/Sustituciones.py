import numpy as np
from copy import deepcopy

def SustitucionRegresiva(matrizU:np.ndarray,vectorB:np.ndarray) -> np.ndarray :
  """
    Procedimiento para aplicar la sustitución regresiva 
    en la matriz U, suponiendo que sea triangular superior, 
    para obtener un vector X tal que U*X = b. 

    matrizU : np.ndarray :: Matriz triangular superior
    vectorB : np.ndarray :: Vector de términos independientes

    Devuelve vector X.
  """
  vectorX = deepcopy(vectorB)
  n = len(matrizU)
  for fila_pivote in range(n-1,-1,-1):
    vectorX[fila_pivote] -= matrizU[fila_pivote,fila_pivote+1:]@vectorX[fila_pivote+1:]
    vectorX[fila_pivote] /= matrizU[fila_pivote,fila_pivote]
  return vectorX

def SustitucionProgresiva(matrizL:np.ndarray,vectorB:np.ndarray) -> np.ndarray:
  """
    Procedimiento para aplicar la sustitución progresiva 
    en la matriz L, suponiendo que sea triangular inferior, 
    para obtener un vector X tal que L*X = b. 

    matrizL : np.ndarray :: Matriz triangular inferior 
    con unos en la diagonal
    vectorB : np.ndarray :: Vector de términos independientes

    Devuelve vector X.
  """
  vectorX = deepcopy(vectorB)
  n = len(matrizL)
  for fila_pivote in range(n):
    vectorX[fila_pivote] /= matrizL[fila_pivote][fila_pivote]
    factores_escalamiento = matrizL[fila_pivote+1:,fila_pivote]
    vectorX[fila_pivote+1:] -= factores_escalamiento*vectorX[fila_pivote]
  return vectorX