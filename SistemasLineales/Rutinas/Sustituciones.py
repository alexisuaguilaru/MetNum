import numpy as np
from copy import deepcopy

def SustitucionRegresiva(matrizU:np.array,vectorB:np.array) -> np.array :
  """
    Procedimiento para aplicar la sustitución regresiva 
    en la matriz U, suponiendo que sea triangular superior, 
    para obtener un vector X tal que U*X = b. 

    matrizU : np.array :: Matriz triangular superior
    vectorB : np.array :: Vector de términos independientes

    Devuelve vector X.
  """
  vectorX = deepcopy(vectorB)
  n = len(matrizU)
  for fila_pivote in range(n-1,-1,-1):
    vectorX[fila_pivote] -= matrizU[fila_pivote,fila_pivote+1:]@vectorX[fila_pivote+1:]
    vectorX[fila_pivote] /= matrizU[fila_pivote,fila_pivote]
  return vectorX

def SustitucionProgresiva(matrizL:np.array,vectorB:np.array) -> np.array:
  """
    Procedimiento para aplicar la sustitución progresiva 
    en la matriz L, suponiendo que sea triangular inferior, 
    para obtener un vector X tal que L*X = b. 

    matrizL : np.array :: Matriz triangular inferior 
    con unos en la diagonal
    vectorB : np.array :: Vector de términos independientes

    Devuelve vector X.
  """
  vectorX = deepcopy(vectorB)
  n = len(matrizL)
  for fila_pivote in range(n-1):
    factores_escalamiento = matrizL[fila_pivote+1:,fila_pivote]
    vectorX -= factores_escalamiento*vectorX[fila_pivote]
  return vectorX