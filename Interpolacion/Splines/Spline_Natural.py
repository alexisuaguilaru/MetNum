import numpy as np

from .Spline_CurvaturaAjustadaAut import Spline_CurvaturaAjustadaAut

class Spline_NaturalAut(Spline_CurvaturaAjustadaAut):
    def __init__(self, conjuntoPuntos:np.ndarray):
        """
            Clase para calcular y evaluar la interpolación 
            por splines cúbicos con condiciones de bordes 
            natural de forma artesanal.         

            conjuntoPuntos : np.ndarray :: Conjuntos
            de puntos que serán interpolados con
            la interpolación de Newton
        """
        valorDerivadaS1 , valorDerivadaSn = 0 , 0 
        super().__init__(conjuntoPuntos,valorDerivadaS1,valorDerivadaSn)