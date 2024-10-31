import numpy as np

from Spline_GeneralAut import Spline_GeneralAut

class Spline_ParabolicoAut(Spline_GeneralAut):
    def __init__(self,conjuntoPuntos:np.ndarray):
        """
            Clase para la definición y evaluación del
            spline con condición de bordes parabólicos 
            de forma artesanal.
        
            conjuntoPuntos : np.array :: Conjuntos de
            puntos en donde se define el spline
        """
        super().__init__(conjuntoPuntos)

    def _CondicionFrontera_MatrizC(self) -> tuple[list[float],list[float]]:
        n = len(self.puntosX)
        return [1,-1] + [0]*(n-2) , [0]*(n-2) + [1,-1]

    def _CondicionFrontera_VectorIndependiente(self) -> tuple[float,float]:
        return 0 , 0