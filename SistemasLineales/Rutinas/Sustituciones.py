import numpy as np
from copy import deepcopy

from Pivoteo import PivoteoParcialEscalonado , PermutarFilaPivoteo , ActualizarVectorEscala , DespermutarFilas

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
    vectorX[fila_pivote] /= matrizL[fila_pivote][fila_pivote]
    factores_escalamiento = matrizL[fila_pivote+1:,fila_pivote]
    vectorX[fila_pivote+1:] -= factores_escalamiento*vectorX[fila_pivote]
  return vectorX

def SustitucionProgresiva_Pivoteo(matrizL:np.array,vectorB:np.array,factores_escala_L:np.array) -> np.array:
    """
        Procedimiento para aplicar la sustitución progresiva 
        en la matriz L, suponiendo que sea triangular inferior 
        y realizando pivoteo, para obtener un vector X 
        tal que L*X = b. 

        matrizL : np.array :: Matriz triangular inferior 
        con unos en la diagonal
        vectorB : np.array :: Vector de términos independientes
        factores_escala_L : np.array :: Vector de factores de 
        escala asociados a la matriz L

        Devuelve vector X.
    """
    vectorX = deepcopy(vectorB)
    n = len(matrizL)
    vector_permutacion = [index_fila for index_fila in range(n)]
    for fila_pivote in range(n):
      index_pivoteo = PivoteoParcialEscalonado(fila_pivote,matrizL,factores_escala_L)
      PermutarFilaPivoteo(fila_pivote,index_pivoteo,vector_permutacion)
      PermutarFilaPivoteo(fila_pivote,index_pivoteo,factores_escala_L)
      PermutarFilaPivoteo(fila_pivote,index_pivoteo,vectorX)
      vectorX[fila_pivote] /= matrizL[fila_pivote][fila_pivote]
      factores_escalamiento = matrizL[fila_pivote+1:,fila_pivote]
      vectorX[fila_pivote+1:] -= factores_escalamiento*vectorX[fila_pivote]
      ActualizarVectorEscala(fila_pivote,matrizL,factores_escala_L)
    DespermutarFilas(vector_permutacion,vectorX)
    DespermutarFilas(vector_permutacion,matrizL)
    return vectorX