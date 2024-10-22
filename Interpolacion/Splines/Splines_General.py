import numpy as np

class Splines_General:
    def __init__(self,conjuntoPuntos:np.array):
        """
            Clase base para calcular y evaluar la 
            interpolación por splines cúbicos

            conjuntoPuntos : np.array :: Conjuntos 
            de puntos que serán interpolados con 
            la interpolación de Newton
        """
        self.puntosX = conjuntoPuntos[:,0]
        self.puntosY = conjuntoPuntos[:,1]
        self.PolinomiosCubicos()

    def __call__(self,valorX:float):
        pass

    def PolinomiosCubicos(self):
        """
            Método que calcula los polinomios 
            asociados a los splines cúbicos en 
            cada par de puntos consecutivos. 
            Se usa definir la matriz de coeficientes 
            en términos del término c_i (coeficiente 
            cuadrático de los polinomios)
        """
        self._deltas_X = self.__Deltas(self.puntosX)
        self._deltas_Y = self.__Deltas(self.puntosY)
        _vectoresCondicionesFrontera = self._CondicionesFrontera()

    def _CondicionesFrontera(self) -> list[list[float]]:
        """
            Método interno que devuelve las 
            condiciones de frontera definidas para 
            el caso del spline, en términos de los 
            coeficientes c_i.

            Devuelve una lista con las filas 
            relacionadas con las condiciones de frontera.        
        """
        return None

    def __Deltas(self,puntos:np.array) -> np.array:
        """
            Método auxiliar para calcular los 
            incrementos sobre un mismo eje en 
            un conjunto de observaciones.

            puntos : np.array :: Conjunto de 
            observaciones sobre las que se 
            calculan los incrementos

            Devuelve el vector de los incrementos
        """
        return puntos[1:] - puntos[:-1]