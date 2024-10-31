import numpy as np

from Spline_GeneralAut import Spline_GeneralAut

class Spline_CurvaturaAjustadaAut(Spline_GeneralAut):
    def __init__(self,conjuntoPuntos:np.ndarray,valorDerivadaS1:float,valorDerivadaSn:float):
        """
            Clase para calcular y evaluar la interpolación 
            por splines cúbicos con condiciones de curvatura 
            ajustada de forma artesanal.         

            conjuntoPuntos : np.ndarray :: Conjuntos
            de puntos que serán interpolados con
            la interpolación de Newton
            valorDerivadaS1 : float :: Valor de la 
            segunda derivada en el primer spline S_1 
            en el punto x_1
            valorDerivadaSn : float :: Valor de la 
            segunda derivada en el primer spline S_{n-1} 
            en el punto x_{n-1}
        """
        self._valorDerivadaS1 = valorDerivadaS1
        self._valorDerivadaSn = valorDerivadaSn
        super().__init__(conjuntoPuntos)

    def _CondicionFrontera_MatrizC(self) -> tuple[list[float],list[float]]:
        n = len(self.puntosX)
        return [2] + [0]*(n-1) , [0]*(n-1) + [2]

    def _CondicionFrontera_VectorIndependiente(self) -> tuple[float,float]:
        return self._valorDerivadaS1 , self._valorDerivadaSn