import numpy as np

from .Spline_GeneralAut import Spline_GeneralAut

class Spline_BordesSujetosAut(Spline_GeneralAut):
    def __init__(self,conjuntoPuntos:np.ndarray,valorDerivadaS1:float=0,valorDerivadaSn:float=0):
        """
            Clase para la definición y evaluación del
            spline con condición de bordes sujetos de 
            forma artesanal.
        
            conjuntoPuntos : np.array :: Conjuntos de
            puntos en donde se define el spline
            valorDerivadaS1 : float :: Valor de la 
            primera derivada en el primer spline S_1 
            en el punto x_1
            valorDerivadaSn : float :: Valor de la 
            primera derivada en el primer spline S_{n-1} 
            en el punto x_{n-1}
        """
        self._valorDerivadaS1 = valorDerivadaS1
        self._valorDerivadaSn = valorDerivadaSn
        super().__init__(conjuntoPuntos)
    
    def _CondicionFrontera_MatrizC(self) -> tuple[list[float],list[float]]:
        n = len(self.puntosX)
        return [2*self._deltas_X[0],self._deltas_X[0]] + [0]*(n-2) , [0]*(n-2) + [self._deltas_X[-1],2*self._deltas_X[-1]]

    def _CondicionFrontera_VectorIndependiente(self) -> tuple[float,float]:
        return 3*(self._deltas_Y[0]/self._deltas_X[0] - self._valorDerivadaS1) , 3*(self._valorDerivadaS1 - self._deltas_Y[-1]/self._deltas_X[-1])