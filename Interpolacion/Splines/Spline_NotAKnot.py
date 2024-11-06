import numpy as np

from .Spline_GeneralAut import Spline_GeneralAut

class Spline_NotAKnotAut(Spline_GeneralAut):
    def __init__(self,conjuntoPuntos:np.ndarray):
        """
            Clase para la definición y evaluación del
            spline con condición de not-a-knot de 
            forma artesanal.
        
            conjuntoPuntos : np.array :: Conjuntos de
            puntos en donde se define el spline
        """
        super().__init__(conjuntoPuntos)

    def _CondicionFrontera_MatrizC(self) -> tuple[list[float],list[float]]:
        n = len(self.puntosX)
        return [self._deltas_X[1],-(self._deltas_X[1]+self._deltas_X[0]),self._deltas_X[0]] + [0]*(n-3) , [0]*(n-3) + [self._deltas_X[-1],-(self._deltas_X[-1]+self._deltas_X[-2]),self._deltas_X[-2]]

    def _CondicionFrontera_VectorIndependiente(self) -> tuple[float,float]:
        return 0 , 0