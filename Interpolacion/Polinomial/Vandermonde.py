import numpy as np

import sys
sys.path.insert(1,'../../..')
from MetNum.SistemasLineales.Solucionadores.EliminacionGauss import EliminacionGauss

class InterpolacionPolinomial_Vandermonde:
    def __init__(self,conjuntoPuntos:np.ndarray):
        """
            Clase para calcular y evaluar el 
            polinomio interpolante de Vandermonde.

            conjuntoPuntos : np.ndarray :: Conjuntos 
            de puntos que serán interpolados con 
            la interpolación de Vandermonde
        """
        self.puntosX = conjuntoPuntos[:,0]
        self.puntosY = conjuntoPuntos[:,1]
        self.coeficientes = self.__CalcularCoeficientes()[::-1]

    def __call__(self,valorX:float) -> float:
        """
            Método para evaluar un valor x en 
            polinomio interpolante definido 
            por los coeficientes.

            valorX : float :: Valor en donde se 
            evalúa el polinomio

            Devuelve el valor de P_n(x).
        """
        return np.polyval(self.coeficientes,valorX)

    def __CalcularCoeficientes(self) -> np.ndarray:
        """
            Método para calcular los coeficientes 
            del polinomio interpolante usando 
            interpolación de Vandermonde.

            Devuelve el vector de coeficientes en 
            orden creciente
        """
        matrizCoeficientes = self.__MatrizCoeficientes()
        return EliminacionGauss(matrizCoeficientes,self.puntosY)

    def __MatrizCoeficientes(self) -> np.ndarray:
        """
            Método para construir la matriz 
            de coeficientes cuyas entradas son 
            potencias de los puntos de X hasta
            el grado del polinomio interpolante.

            Devuelve la matriz de coeficientes 
            asociada al conjunto de las X de 
            los puntos.
        """
        gradoPolinomioInterpolante = len(self.puntosX)-1
        matrizCoeficientes = []
        for puntoX in self.puntosX:
            potenciasPuntoX = [1]
            for _ in range(gradoPolinomioInterpolante):
                potenciasPuntoX.append(potenciasPuntoX[-1]*puntoX)
            matrizCoeficientes.append(potenciasPuntoX)
        return np.array(matrizCoeficientes,dtype=float)