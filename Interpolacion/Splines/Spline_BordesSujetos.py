import numpy as np

import sys
sys.path.insert(1,'../../..')
from MetNum.Interpolacion.Splines.Spline_General import Spline_General

class Spline_BordesSujetos(Spline_General):
    def __init__(self,conjuntoPuntos:np.ndarray,valorDerivadaS1:float=0,valorDerivadaSn:float=0):
        """
            Clase para la definición y evaluación del
            spline bordes sujetos.
        
            conjuntoPuntos : np.array :: Conjuntos de
            puntos en donde se define el spline
            valorDerivadaS1 : float :: Valor de la 
            primera derivada en el primer spline S_1 
            en el punto x_1
            valorDerivadaSn : float :: Valor de la 
            primera derivada en el primer spline S_{n-1} 
            en el punto x_{n-1}
        """
        bc_type = ((1,valorDerivadaS1),(1,valorDerivadaSn))
        super().__init__(conjuntoPuntos,bc_type)