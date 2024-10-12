import numpy as np
from copy import deepcopy

class InterpolacionPolinomial_Lagrange:
    def __init__(self,conjuntoPuntos:np.array):
        """
            Clase para calcular y evaluar el 
            polinomio interpolante de Lagrange.

            conjuntoPuntos : np.array :: Conjuntos 
            de puntos que serán interpolados con 
            la interpolación de Lagrange
        """
        self.puntosX = np.reshape(conjuntoPuntos[:,0],shape=(len(conjuntoPuntos),1))
        self.puntosY = conjuntoPuntos[:,1]
        self.coeficientesPolinomiosComponentes = self.__CalcularCoeficientesPolinomiosComponentes()

    def __call__(self,valorX:float) -> float:
        """
            Método para evaluar un valor x en 
            polinomio interpolante de 
            Lagrange.

            valorX : float :: Valor en donde se 
            evalúa el polinomio

            Devuelve el valor de P_n(x).
        """
        n_CantidadCoeficientes = len(self.puntosX)
        polinomiosComponentesEvaluados = valorX*np.ones((n_CantidadCoeficientes,n_CantidadCoeficientes))
        polinomiosComponentesEvaluados -= self.__matrizValoresX
        for diagonal_index in range(n_CantidadCoeficientes):
            polinomiosComponentesEvaluados[(diagonal_index,diagonal_index)] = 1
        polinomiosComponentesEvaluados = np.apply_along_axis(np.prod,0,polinomiosComponentesEvaluados)
        polinomiosComponentesEvaluados /= self.coeficientesPolinomiosComponentes
        return polinomiosComponentesEvaluados@self.puntosY

    def __CalcularCoeficientesPolinomiosComponentes(self) -> np.array:
        """
            Método para calcular los coeficientes 
            de los polinomios componentes.

            Devuelve el vector de coeficientes de 
            los polinomios componentes.
        """
        n_CantidadCoeficientes = len(self.puntosX)
        self.__matrizValoresX = self.puntosX@np.ones((n_CantidadCoeficientes,1)).T
        coeficientesPolinomiosComponentes = deepcopy(self.__matrizValoresX)
        coeficientesPolinomiosComponentes -= coeficientesPolinomiosComponentes.T
        for diagonal_index in range(n_CantidadCoeficientes):
            coeficientesPolinomiosComponentes[(diagonal_index,diagonal_index)] = 1
        return np.apply_along_axis(np.prod,1,coeficientesPolinomiosComponentes)