import numpy as np

import sys
sys.path.insert(1,'../../..')
from MetNum.Interpolacion.Splines.Spline_General import Spline_General

class Spline_NotAKnot(Spline_General):
    def __init__(self,conjuntoPuntos:np.ndarray):
        """
            Clase para la definición y evaluación del
            spline not-a-knot.
        
            conjuntoPuntos : np.array :: Conjuntos de
            puntos en donde se define el spline
        """
        bc_type = 'not-a-knot'
        super().__init__(conjuntoPuntos,bc_type)