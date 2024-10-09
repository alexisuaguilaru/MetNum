import numpy as np
from copy import deepcopy
import math 

def MetodoJacobi(matrizA:np.array,vectorB:np.array,tolerancia_error:float=1e-9):
    """
        Procedimiento para determinar una 
        solución aproximada al sistema de 
        ecuaciones lineales Ax=b haciendo 
        uso de método de Jacobi.
    
        matrizA : np.array :: Matriz de 
        coeficientes del sistema
        vectorB : np.array :: Vector de 
        términos independientes
        tolerancia_error : float :: Tolerancia 
        para indicar que el método convergió 
        a una solución.

        Devuelve vector solución X 
        aproximado
    """
    n = len(vectorB)
    vectorX = np.zeros(n)
    vectorX_actualizado = np.zeros(n)
    vectorResto = vectorB - matrizA@vectorX 
    while np.linalg.norm(vectorResto) > tolerancia_error:
        for i_index in range(n):
            vectorX_actualizado[i_index] = (vectorB[i_index] - matrizA[i_index,:i_index]@vectorX[:i_index] - matrizA[i_index,i_index+1:]@vectorX[i_index+1:])/matrizA[i_index][i_index]
        vectorX = deepcopy(vectorX_actualizado)
        vectorResto = vectorB - matrizA@vectorX
    return vectorX

def MetodoGaussSeidel(matrizA:np.array,vectorB:np.array,tolerancia_error:float=1e-9):
    """
        Procedimiento para determinar una 
        solución aproximada al sistema de 
        ecuaciones lineales Ax=b haciendo 
        uso de método de Gauss-Seidel.
    
        matrizA : np.array :: Matriz de 
        coeficientes del sistema
        vectorB : np.array :: Vector de 
        términos independientes
        tolerancia_error : float :: Tolerancia 
        para indicar que el método convergió 
        a una solución.

        Devuelve vector solución X 
        aproximado
    """
    n = len(vectorB)
    vectorX = np.zeros(n)
    vectorResto = vectorB - matrizA@vectorX 
    while np.linalg.norm(vectorResto) > tolerancia_error:
        for i_index in range(n):
            vectorX[i_index] = (vectorB[i_index] - matrizA[i_index,:i_index]@vectorX[:i_index] - matrizA[i_index,i_index+1:]@vectorX[i_index+1:])/matrizA[i_index][i_index]
        vectorResto = vectorB - matrizA@vectorX
    return vectorX

# Por pruebas, usar relajación empeora la convergencia
def MetodoJacobi_Relajacion(matrizA:np.array,vectorB:np.array,p_iteraciones:int,tolerancia_error:float=1e-9) -> np.array:
    """
        Procedimiento para determinar una 
        solución aproximada al sistema de 
        ecuaciones lineales Ax=b haciendo 
        uso de método de Jacobi.
    
        matrizA : np.array :: Matriz de 
        coeficientes del sistema
        vectorB : np.array :: Vector de 
        términos independientes
        p_iteraciones : int :: Entero que indica 
        la diferencia que se debe que considerar 
        para calcular el factor de relajación
        tolerancia_error : float :: Tolerancia 
        para indicar que el método convergió 
        a una solución.

        Devuelve vector solución X 
        aproximado
    """
    n = len(vectorB)
    vectorX = np.zeros(n)
    vectorX_actualizado = np.zeros(n)
    vectorResto = vectorB - matrizA@vectorX 
    factorRelajacion = 1
    DiferenciasVectores = []
    while np.linalg.norm(vectorResto) > tolerancia_error:
        for i_index in range(n):
            vectorX_actualizado[i_index] = (vectorB[i_index] - matrizA[i_index,:i_index]@vectorX[:i_index] - matrizA[i_index,i_index+1:]@vectorX[i_index+1:])/matrizA[i_index][i_index]
        vectorX_actualizado = factorRelajacion*vectorX_actualizado + (1-factorRelajacion)*vectorX
        if len(DiferenciasVectores) > (p_iteraciones + 10):
            factorRelajacion = __FactorRelajacion(DiferenciasVectores,p_iteraciones)
        DiferenciasVectores.append(np.linalg.norm(vectorX_actualizado-vectorX))
        vectorX = deepcopy(vectorX_actualizado)
        vectorResto = vectorB - matrizA@vectorX
    return vectorX

def MetodoGaussSeidel_Relajacion(matrizA:np.array,vectorB:np.array,p_iteraciones:int,tolerancia_error:float=1e-9):
    """
        Procedimiento para determinar una 
        solución aproximada al sistema de 
        ecuaciones lineales Ax=b haciendo 
        uso de método de Gauss-Seidel.
    
        matrizA : np.array :: Matriz de 
        coeficientes del sistema
        vectorB : np.array :: Vector de 
        términos independientes
        p_iteraciones : int :: Entero que indica 
        la diferencia que se debe que considerar 
        para calcular el factor de relajación
        tolerancia_error : float :: Tolerancia 
        para indicar que el método convergió 
        a una solución.

        Devuelve vector solución X 
        aproximado
    """
    n = len(vectorB)
    vectorX = np.zeros(n)
    vectorX_actualizado = np.zeros(n)
    vectorResto = vectorB - matrizA@vectorX 
    factorRelajacion = 1
    DiferenciasVectores = []
    while np.linalg.norm(vectorResto) > tolerancia_error:
        for i_index in range(n):
            vectorX_actualizado[i_index] = factorRelajacion*(vectorB[i_index] - matrizA[i_index,:i_index]@vectorX_actualizado[:i_index] - matrizA[i_index,i_index+1:]@vectorX[i_index+1:])/matrizA[i_index][i_index] + (1-factorRelajacion)*vectorX[i_index]
        if len(DiferenciasVectores) > (p_iteraciones + 10):
            factorRelajacion = __FactorRelajacion(DiferenciasVectores,p_iteraciones)
        DiferenciasVectores.append(np.linalg.norm(vectorX_actualizado-vectorX))
        vectorX = deepcopy(vectorX_actualizado)
        vectorResto = vectorB - matrizA@vectorX
    return vectorX

def __FactorRelajacion(DiferenciaVectores:list[float],p_iteraciones:int) -> float:
    """
        Procedimiento auxliar para calcular 
        el factor de relajación optimo dado 
        las diferencias entre vectores 
        consecutivos.

        DiferenciaVectores : list[float] :: Lista 
        con las normas de las diferencias entre los 
        vectores obtenidos del método iterativo
        p_iteraciones : int :: Entero que indica 
        la diferencia que se debe que considerar 
        para calcular el factor de relajación

        Devuelve el factor de relajación.
    """
    valorDiferencias = DiferenciaVectores[-1]/DiferenciaVectores[-p_iteraciones-1] 
    valorRaiz = 1 - math.pow(valorDiferencias,1/p_iteraciones)
    valorCociente = 1 + math.pow(abs(valorRaiz),1/2)
    return 2/valorCociente